"""Rebuild the proposed shared diagram after editing classification-flow.flow.json.

Requires the installed acetate-flow skill. Does not start a server or call AI.
"""
import argparse
import copy
import json
from pathlib import Path
import runpy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill-dir', type=Path, default=Path.home() / '.codex/skills/acetate-flow')
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    builder = runpy.run_path(str(args.skill_dir / 'scripts/create_flow.py'))
    # Person and Interface are extra visual types for this correction-flow viewer.
    builder['KINDS'].update({'human', 'ui'})
    config = json.loads((folder / 'classification-flow.flow.json').read_text())
    builder['validate'](copy.deepcopy(config))
    template = (folder / 'classification-flow.renderer.html').read_text()
    if template.count('{{FLOW_JSON}}') != 1:
        raise ValueError('Expected exactly one JSON slot')
    payload = json.dumps(config, ensure_ascii=True, allow_nan=False, separators=(',', ':'))
    payload = payload.replace('&', r'\u0026').replace('<', r'\u003c').replace('>', r'\u003e')
    destination = folder / 'classification-flow.html'
    destination.write_text(template.replace('{{FLOW_JSON}}', payload))
    print(destination)


if __name__ == '__main__':
    main()
