"""Local offline smoke tests: structural tests do not test actual agent behaviour."""
from pathlib import Path
import unittest
import sys
import tempfile
import json
import shutil
import copy
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_021 import evaluate
from assess_context_packet import inspect

ROOT = Path(__file__).resolve().parents[1]


class Test021(unittest.TestCase):
    def test_valid_bundle(self):
        errors, warnings, indexed = evaluate(ROOT)
        self.assertEqual(errors, [], errors)
        self.assertEqual(indexed, 160)

    def test_duplicate_page_cannot_replace_missing_page(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / '021'
            shutil.copytree(ROOT, candidate)
            page_notes = candidate / 'references/page-audit.md'
            page_notes.write_text(page_notes.read_text().replace('**PDF p. 160**', '**PDF p. 159**'))
            errors, _, _ = evaluate(candidate)
            self.assertTrue(any('exactly once' in error for error in errors))

    def test_context_packet_missing_intention_fails(self):
        data = {
            'venture_id': 'X', 'baseline_version': '1',
            'customer_outcome': 'Build usable printable object', 'task_objective': 'Validate dimensions',
            'prior_decisions': ['Use A4'], 'negative_constraints': ['No colourful dashboard'],
            'source_locations': ['spec.md'],
            'acceptance': {'functional': ['paper fits'], 'intention_fidelity': ['minimal interface']},
            'permissions': ['sandbox'], 'budget_enforcement': 'provider cap',
            'escalation': 'human', 'owner': 'operator'
        }
        self.assertTrue(any('approved_purpose' in e for e in inspect(data)))
        data['approved_purpose'] = 'Create simple physical objects at home'
        self.assertEqual(inspect(data), [])

    def test_context_requires_both_acceptance_types(self):
        d = {k: 'x' for k in ('venture_id', 'baseline_version', 'approved_purpose',
              'customer_outcome', 'task_objective', 'prior_decisions',
              'negative_constraints', 'source_locations', 'permissions',
              'budget_enforcement', 'escalation', 'owner')}
        d['acceptance'] = {'functional': ['works']}
        self.assertTrue(any('intention_fidelity' in x for x in inspect(d)))
        d['acceptance']['intention_fidelity'] = ['correct experience']
        self.assertFalse(any('acceptance.' in x for x in inspect(d)))

    def test_malformed_frontmatter_reports_error(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / '021'
            shutil.copytree(ROOT, candidate)
            path = candidate / 'SKILL.md'
            path.write_text(path.read_text().replace('name: "021"', 'name: [broken'))
            errors, _, _ = evaluate(candidate)
            self.assertTrue(any('Invalid frontmatter' in error for error in errors))

    def test_context_rejects_wrong_field_types(self):
        valid = yaml.safe_load((ROOT/'examples/filled-context-packet.yaml').read_text())
        for field, value in [('approved_purpose', {}), ('owner', '   '),
                             ('permissions', 'write anywhere'), ('negative_constraints', [False])]:
            packet = copy.deepcopy(valid)
            packet[field] = value
            with self.subTest(field=field):
                self.assertTrue(any(field in error for error in inspect(packet)))

    def test_context_rejects_string_privacy_flags(self):
        packet = yaml.safe_load((ROOT/'examples/filled-context-packet.yaml').read_text())
        packet.update(sensitive_data=True, least_privilege_scoped='false')
        errors = inspect(packet)
        self.assertTrue(any('boolean' in error for error in errors))
        self.assertTrue(any('least-privilege' in error for error in errors))

    def test_new_project_can_have_no_prior_decisions(self):
        packet = yaml.safe_load((ROOT/'examples/filled-context-packet.yaml').read_text())
        packet.update(prior_decisions=[], negative_constraints=[])
        self.assertEqual(inspect(packet), [])

    def test_context_rejects_non_mapping(self):
        self.assertEqual(inspect([]), ['Packet must be a mapping'])

    def test_scenarios_have_hard_failure_checks(self):
        scenarios = json.loads((ROOT / 'evaluations/scenarios.json').read_text())
        self.assertEqual(len(scenarios), 14)
        self.assertTrue(all(case['must_not'] for case in scenarios))
        self.assertTrue(any('deploy' in x['scenario'].lower() for x in scenarios))


if __name__ == '__main__':
    unittest.main()
