#!/usr/bin/env python3
"""Check field types in a filled context handoff. Parsing YAML requires PyYAML.

This cannot verify truth, user approval, sufficiency or runtime permissions.
"""
from pathlib import Path
import sys
try:
    import yaml
except ImportError:
    yaml = None

TEXT_FIELDS = ('venture_id', 'baseline_version', 'approved_purpose', 'customer_outcome',
               'task_objective', 'budget_enforcement', 'escalation', 'owner')
LIST_FIELDS = ('prior_decisions', 'negative_constraints', 'source_locations', 'permissions')


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def string_list(value, allow_empty=False):
    return isinstance(value, list) and (allow_empty or bool(value)) and all(nonblank(v) for v in value)


def inspect(packet):
    if not isinstance(packet, dict):
        return ['Packet must be a mapping']
    errors = []
    for key in TEXT_FIELDS:
        if not nonblank(packet.get(key)):
            errors.append(f'{key} must be a nonblank string')
    for key in LIST_FIELDS:
        allow_empty = key in ('prior_decisions', 'negative_constraints')
        if not string_list(packet.get(key), allow_empty):
            errors.append(f'{key} must be a list of nonblank strings' + ('' if allow_empty else ' with at least one entry'))
    acceptance = packet.get('acceptance')
    for key in ('functional', 'intention_fidelity'):
        if not isinstance(acceptance, dict) or not string_list(acceptance.get(key)):
            errors.append(f'acceptance.{key} must list at least one nonblank criterion')
    for key in ('sensitive_data', 'least_privilege_scoped'):
        if key in packet and not isinstance(packet[key], bool):
            errors.append(f'{key} must be a boolean')
    if packet.get('sensitive_data') is True and packet.get('least_privilege_scoped') is not True:
        errors.append('Sensitive context requires explicit least-privilege scoping')
    return errors


def main():
    if len(sys.argv) != 2:
        print('Usage: assess_context_packet.py FILLED_CONTEXT.yaml', file=sys.stderr)
        return 2
    if yaml is None:
        print('PyYAML is required to read context handoff YAML', file=sys.stderr)
        return 2
    try:
        packet = yaml.safe_load(Path(sys.argv[1]).read_text(encoding='utf-8'))
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        print(f'Cannot read context packet: {error}', file=sys.stderr)
        return 2
    errors = inspect(packet)
    if errors:
        print('CONTEXT PACKET INVALID')
        for error in errors:
            print('-', error)
        return 1
    print('CONTEXT PACKET STRUCTURE PASSED. Truth, authority and runtime permissions remain unverified.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
