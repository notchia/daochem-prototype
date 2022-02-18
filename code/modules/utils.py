import json


def load_json(fpath):
    """Load JSON or JSONL files"""
    try:
        with open(fpath, 'r') as f:
            r = json.load(f)
    except json.decoder.JSONDecodeError:
        try:
            r = []
            with open(fpath, 'r') as f:
                for line in f.readlines():
                    r_tmp = json.load(f)
                    r.append(r_tmp)
        except json.decoder.JSONDecodeError:
            r = {}

    return r