#!/usr/bin/env python3
"""Offline structural/content checks for the portable 021 skill.

This validator does NOT measure agent behaviour, output correctness, or business outcomes.
"""
from pathlib import Path
import json
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

REQUIRED = [
    'SKILL.md', 'README.md', 'LICENSE', 'NOTICE.md',
    'references/book-audit.md', 'references/claim-audit.md',
    'references/page-audit.md', 'references/source-register.md',
    'references/source-use.md', 'references/context-and-intention.md',
    'references/agent-context-protocol.md', 'references/method.md',
    'references/build-and-agents.md', 'references/gtm-and-economics.md',
    'assets/opportunity-brief.md', 'assets/experiment-log.md',
    'assets/product-spec.md', 'assets/gtm-plan.md', 'assets/decision-memo.md',
    'assets/intention-brief.md', 'assets/context-ledger.md',
    'assets/context-handoff.md', 'assets/intent-change.md',
    'assets/outcome-verification.md', 'assets/launch-intention-check.md',
    'assets/agent-task-contract.yaml',
    'evaluations/README.md', 'evaluations/scenarios.json',
    'scripts/assess_context_packet.py', 'examples/task-results.md',
]
SEVEN = ('Engineering', 'Timing', 'Monopoly', 'People', 'Distribution', 'Durability', 'Secret')
REQUIRED_CASE_IDS = {'INTENT-001', 'INTENT-002', 'CONTEXT-003', 'SOURCE-004',
                     'DELIVERY-005', 'GTM-006', 'AUTH-007', 'ADAPT-008',
                     'STRATEGY-009', 'PORTFOLIO-010', 'GTMIN-011', 'CONTEXT-012',
                     'GTM-013', 'ADAPT-014'}


def evaluate(root: Path):
    problems = []
    warnings = []
    if yaml is None:
        return ['PyYAML missing: cannot validate YAML frontmatter/contracts'], warnings, 0
    for name in REQUIRED:
        if not (root / name).is_file():
            problems.append(f'Missing file: {name}')
    skill_path = root / 'SKILL.md'
    skill = skill_path.read_text(encoding='utf-8') if skill_path.exists() else ''
    if not skill.startswith('---\n'):
        problems.append('SKILL.md needs YAML frontmatter')
    else:
        try:
            header, body = skill[4:].split('\n---\n', 1)
            meta = yaml.safe_load(header) if yaml else {}
            if meta.get('name') != root.name:
                problems.append('SKILL.md name must match the folder name')
            if not isinstance(meta.get('description'), str) or not meta['description'].strip():
                problems.append('SKILL.md requires a non-empty description')
            elif len(meta['description']) > 1024:
                problems.append('Description exceeds 1024 characters')
            metadata = meta.get('metadata', {})
            if not isinstance(metadata, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()):
                problems.append('SKILL.md metadata must map strings to strings')
            if meta.get('license') != 'MIT':
                problems.append('SKILL.md must declare the selected MIT license')
            if len(body.splitlines()) > 500:
                warnings.append('SKILL.md >500 lines: current specification recommends progressive references; NOT a hard format error')
        except (ValueError, AttributeError, TypeError, yaml.YAMLError) as exc:
            problems.append(f'Invalid frontmatter: {exc}')
    for word in SEVEN:
        if not re.search(r'\b' + word + r'\b', skill):
            problems.append(f'Missing original seven-question category: {word}')
    for phrase in ('intention', 'negative constraints', 'context handoff', 'fidelity', 'revenue'):
        if phrase.lower() not in skill.lower():
            problems.append(f'Missing core concept: {phrase}')
    # Referenced local links must resolve. Avoid network requests for external links.
    markdown_link = re.compile(r'\]\(((?:references|assets|evaluations|scripts)/[^)]+)\)')
    all_refs = set(markdown_link.findall(skill))
    for p in root.rglob('*.md'):
        for ref in markdown_link.findall(p.read_text(encoding='utf-8')):
            all_refs.add(ref)
    for ref in sorted(all_refs):
        if not (root / ref).is_file():
            problems.append(f'Broken local reference: {ref}')
    indexed_pages = 0
    page_notes = root / 'references/page-audit.md'
    if page_notes.is_file():
        pages = [int(n) for n in re.findall(r'\*\*PDF p\. (\d{3})\*\*', page_notes.read_text(encoding='utf-8'))]
        indexed_pages = len(pages)
        if indexed_pages != 160 or set(pages) != set(range(1, 161)):
            problems.append('Book page notes must cover each of the 160 reference PDF pages exactly once')
    cases = root / 'evaluations/scenarios.json'
    if cases.is_file():
        try:
            data = json.loads(cases.read_text(encoding='utf-8'))
            ids = [x['id'] for x in data]
            if len(set(ids)) != len(ids): problems.append('Duplicate scenario IDs')
            if set(ids) != REQUIRED_CASE_IDS: problems.append('Missing/extra evaluation scenario IDs')
            for x in data:
                if not all(x.get(k) for k in ('id', 'name', 'scenario', 'must_do', 'must_not', 'references')):
                    problems.append(f'Incomplete scenario {x.get("id")}')
                for ref in x.get('references', []):
                    if not (root / ref).is_file(): problems.append(f'Bad case reference {x.get("id")}: {ref}')
        except Exception as exc:
            problems.append(f'Cannot parse evaluation scenarios: {exc}')
    task = root / 'assets/agent-task-contract.yaml'
    if task.is_file() and yaml:
        try:
            task_data = yaml.safe_load(task.read_text(encoding='utf-8'))
            for field in ('intention_baseline', 'negative_constraints', 'acceptance', 'limits', 'escalate_if'):
                if field not in task_data: problems.append(f'Task contract missing {field}')
            if task_data.get('limits', {}).get('hard_limit_enforced_by_runtime') is True:
                warnings.append('Example claims a hard runtime budget limit; verify enforcement rather than trusting the template')
        except Exception as exc:
            problems.append(f'Task YAML parse failed: {exc}')
    return problems, warnings, indexed_pages


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    problems, warnings, indexed_pages = evaluate(root)
    for warning in warnings: print('WARNING:', warning)
    if problems:
        print('021 VALIDATION FAILED')
        for p in problems: print(' -', p)
        return 1
    print(f'021 STRUCTURAL VALIDATION PASSED: {root.name}; {indexed_pages} book page notes; {len(REQUIRED_CASE_IDS)} evaluation scenarios.')
    print('This is NOT a behavioural evaluation of an LLM, nor a verification of commercial success.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
