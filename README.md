# 021 — Zero to One

Artificial Milieu · MIT · v0.3.1

Ask your agent to use 021 to evaluate an idea, plan validation, review a release
or diagnose customer acquisition. The instructions are in [SKILL.md](SKILL.md);
they point to the references and templates needed for each task.

Install this entire folder, including its resources. For substantial work, copy
the relevant templates into your project. Keep customer data and project records
out of the installed skill.

## Optional checks

Python 3.11+ and PyYAML 6.0.3 are needed for these helpers. From this folder:

```bash
python3 -B scripts/validate_021.py .
python3 -B -m unittest discover -s tests -v
python3 -B scripts/assess_context_packet.py examples/filled-context-packet.yaml
```

These checks validate structure and field types. They do not verify that a
statement is true, an action is authorized or a customer outcome occurred.
See [behavioral evaluation](evaluations/README.md) for tests of agent responses.

## Attribution and support

MIT — [LICENSE](LICENSE). [NOTICE.md](NOTICE.md) credits external sources. The
book notes are secondary interpretations; verify exact claims against an
authorized original. Contact: support@artificialmilieu.com.
