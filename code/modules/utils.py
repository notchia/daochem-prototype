import json
import requests
import pandas as pd
import numpy as np

API_URL = 'https://ethdenver.azurewebsites.net/api/BoardRoom/protocols'


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


def print_groupby(gb):
    """Print pandas groupby object"""
    for key, item in gb:
        print(gb.get_group(key), "\n")


def normalize_name(s):
    s_norm = s.strip().lower()
    s_norm = s_norm.replace(" ", "")
    s_norm = s_norm.removesuffix('dao')
    return s_norm


def load_db():
    
    # Import database as dataframe
    db_json = requests.get(API_URL).json()
    df_db = pd.json_normalize(db_json)

    # Clean
    df_db['daoName'] = df_db['name'].apply(normalize_name)
    df_db['framework'] = df_db['framework'].apply(lambda s: s if (s is not None) or (s != '') else None)
    df_db = df_db[['daoName', 'name', 'framework', 'category', 'followerCount']].reset_index()
    df_db = df_db.replace(np.nan, None, regex=True)
    df_db = df_db.replace('', None, regex=True)

    return df_db