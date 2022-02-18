import json


def load_json(fpath):
    """Load JSON or JSONL files"""
    try:
        with open(fpath, 'r') as f:
            r = json.load(f)
    except json.decoder.JSONDecodeError:
        try:
            with open(fpath, 'r') as f:
                r = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            r = {}

    return r
