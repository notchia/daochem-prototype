import os
import time
import json
import subprocess
import argh
import numpy as np
from datetime import datetime

from config import TMPDIR, DATADIR, TRUEBLOCKS_URL

RPS_LIMIT = 10 # requests per second rate limit from ArchiveNode.io
SLEEP = 1 # second

CACHE = "--cache"
JSON = "--format json"


def pipe_chifra_call(command, mode='w', fpath=None):
    """Call chifra command and save to JSON file"""
    if fpath is None:
        fpath = os.path.join(TMPDIR, 'trueblocks.json')

    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        with open(fpath, mode) as f:
            lines = [line.decode("utf-8") for line in process.stdout]
            if 'w' in mode:
                f.writelines(lines)
            elif 'a' in mode:
                line = " ".join(lines)
                f.write(line)
    except Exception as e:
        print(e)

    return fpath


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
                    r.append[r_tmp]
        except json.decoder.JSONDecodeError:
            r = {}

    return r


def pipe_chifra_call_with_sleep(cmd, fpath=None):
    """Batch the API call to prevent the archive node rate limit from being exceeded"""

    if fpath is None:
        fpath = os.path.join(TMPDIR, 'trueblocks.json')

    flags = {'max': 1}
    r = '{}'
    totalCount = 0
    batchCount = 0
    t0 = time.now().time()
    with open(fpath, 'a') as f:
        while len(r) > 0:
            # Get API response and save to file/append to list
            flags['first'] = totalCount
            _cmd = cmd + f"--first_record={flags['first']}" + f"--max_records={flags['max']}"
            pipe_chifra_call(_cmd, mode='a', fpath=fpath)

            # Pause if RPS_LIMIT is about to be exceeded
            batchCount += 1
            totalCount += 1
            if (batchCount > RPS_LIMIT - 1):
                time.sleep(SLEEP)
            t1 = time.now().time()
            if (t1 - t0) > 1:
                t0 = t1
                batchCount = 0
            print(batchCount)

    r_all = load_json(fpath)

    return r_all


def chifra_list(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """    
    return " ".join["chifra", "list", JSON, CACHE, address]


def chifra_blocks(block):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return " ".join["chifra", "blocks", JSON, CACHE, block]


def chifra_abi(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return " ".join["chifra", "abi", JSON, address]


def chifra_export(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return " ".join["chifra", "export", "--factory", JSON, address]


def chifra_export_logs(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return " ".join["chifra", "export", "--factory",  "--logs", "--articulate", "--relevant", JSON, address]


def test_address_export(address):
    # Create monitor
    cmd = chifra_list(address)
    fpath = os.path.join(TMPDIR, 'trueblocks_test_list.json')
    pipe_chifra_call(cmd, fpath=fpath)
    r = load_json(fpath)
    print("successfully loaded `chifra list` results")

    # Export transaction history
    cmd = chifra_export(address)
    fpath = os.path.join(TMPDIR, 'trueblocks_test_export.json')
    pipe_chifra_call(cmd, fpath=fpath)  
    r = load_json(fpath)
    print("successfully loaded `chifra export` results")


if __name__ == "__main__":
    argh.dispatch(test_address_export)