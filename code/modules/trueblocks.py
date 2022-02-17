import os
import time
import json
import requests
import argh
import numpy as np
from datetime import datetime

from config import TMPDIR, DATADIR, TRUEBLOCKS_URL

RPS_LIMIT = 10 # requests per second rate limit from ArchiveNode.io
SLEEP = 1 # second

CACHE = "&cache=true"
JSON = "&format=json"


def get_chifra_as_json(url, session=None):
    """Return result of TrueBlocks API call as JSON"""

    if session is None:
        session = requests.Session()

    if 'json' not in url:
        url = url + JSON

    r = session.get(url)
    try:
        r = r.json()
    except json.decoder.JSONDecodeError:
        r = {}

    return r


def get_chifra_as_json_with_sleep(url, label=None):
    """Batch the API call to prevent the archive node rate limit from being exceeded
    Saves result to individual files """

    if label is None:
        label = 'trueblocks'

    flags = {'maxRecords': 1}
    r = '{}'
    totalCount = 0
    batchCount = 0
    t0 = time.now().time()
    session = requests.Session
    fname = f"{label}_{totalCount}.json"
    fpath = os.path.join(os.path.join(TMPDIR, fname))
    r_all = []
    with open(fpath, 'a') as f:
        while len(r) > 0:
            # Get API response and save to file/append to list
            flags['firstRecord'] = totalCount
            _url = url + f"&firstRecord={flags['firstRecord']}" + f"&maxRecords={flags['maxRecords']}"
            r = get_chifra_as_json(_url, session=session)
            json.dump(r, f)
            r_all.append(r)

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

    return r_all


def chifra_list(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """    
    return TRUEBLOCKS_URL + "list=" + address


def chifra_blocks(block):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return TRUEBLOCKS_URL + "blocks=" + block + JSON


def chifra_abi(address):
    """Retrieve a smart contract's ABI file
    https://trueblocks.io/docs/chifra/accounts/#chifra-abis
    """
    return TRUEBLOCKS_URL + "abi=" + address + JSON


def chifra_list(address):
    """Query index of apperances and build monitors
    https://trueblocks.io/docs/chifra/accounts/#chifra-list
    """
    return TRUEBLOCKS_URL + "list=" + address + JSON


def chifra_export(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return TRUEBLOCKS_URL + "export=" + address + JSON


def chifra_export_logs(address):
    """Export all transactions involving this account:
    command line: chifra export --fmt json <address>
    https://trueblocks.io/docs/chifra/accounts/#chifra-export
    """

    return TRUEBLOCKS_URL + "export=" + address + "&logs=true" + "&articulate=true" + "&relevant=true" + JSON

if __name__ == "__main__":
    url = argh.dispatch(chifra_export)
    r = get_chifra_as_json_with_sleep(url)
