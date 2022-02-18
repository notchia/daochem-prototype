import os
import time
import json
import subprocess
import argh
import numpy as np
from datetime import datetime

from config import TMPDIR, DATADIR

RPS_LIMIT = 10 # requests per second rate limit from ArchiveNode.io
SLEEP = 1 # second

CACHE = "--cache"
JSON = "--fmt json"


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
                    r.append(r_tmp)
        except json.decoder.JSONDecodeError:
            r = {}

    return r


def pipe_chifra_call_with_sleep(cmd, label=None):
    """Batch the API call to prevent the archive node rate limit from being exceeded"""

    if label is None:
        label = 'trueblocks'
        dir = TMPDIR
    else:
        dir = DATADIR

    flags = {'max': 1}
    r_all = []
    r = {'data': {}}
    totalCount = 0
    batchCount = 0
    t0 = datetime.now()
    while len(r) > 0:
        # Get API response and save to file/append to list
        flags['first'] = totalCount
        cmd_items = cmd.split(' ')
        cmd_items.insert(2, f"--first_record={flags['first']}")
        cmd_items.insert(3, f"--max_records={flags['max']}")
        _cmd = " ".join(cmd_items)
        fpath = os.path.join(dir, f"{label}_{totalCount}.json")
        pipe_chifra_call(_cmd, fpath=fpath)
        r = load_json(fpath)
        r_all.append(r)

        # Pause if RPS_LIMIT is about to be exceeded
        batchCount += 1
        totalCount += 1
        if (batchCount > RPS_LIMIT - 1):
            time.sleep(SLEEP)
        t1 = datetime.now()
        if (t1 - t0).total_seconds() > 1:
            t0 = t1
            batchCount = 0
        print(batchCount)

    return r_all


def chifra_list(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """    
    return " ".join(["chifra", "list", JSON, address])


def chifra_blocks(block):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return " ".join(["chifra", "blocks", JSON, CACHE, block])


def chifra_abi(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return " ".join(["chifra", "abi", JSON, address])


def chifra_export(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return " ".join(["chifra", "export", "--articulate", CACHE, JSON, address])


def chifra_export_logs(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return " ".join(["chifra", "export", "--factory",  "--logs", "--articulate", "--relevant", JSON, address])


def test_address_export(address):
    # Create monitor
    cmd = chifra_list(address)
    fpath = os.path.join(TMPDIR, 'trueblocks_test_list.json')
    pipe_chifra_call(cmd, fpath=fpath)
    r = load_json(fpath)
    print("successfully loaded `chifra list` results")

    # Export transaction history
    cmd = chifra_export(address)
    label = 'trueblocks_test_export'
    r = pipe_chifra_call_with_sleep(cmd, label=label)  
    print(f"successfully got {len(r)} `chifra export` results")


if __name__ == "__main__":
    argh.dispatch_command(test_address_export)
