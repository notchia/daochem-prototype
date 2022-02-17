import os
import json
import time
import requests
import subprocess
import pandas as pd

from modules.trueblocks import chifra_blocks, get_chifra_as_json
from config import CWD, TMPDIR, DATADIR

os.chdir(CWD)


# command => chifra transactions --articulate --fmt json 303300.\* 303301.\* 303302.\* 303303.\*
def process_blocks_as_stream(command):
    file_name = os.path.join(TMPDIR, 'trueblocks.json')
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        with open(file_name, "w") as f:
            for line in process.stdout:
                f.write(line.decode("utf-8"))
    except Exception as e:
        print("process_blocks_as_stream: Exception raised [{}]".format(e))

    try:
        with open(file_name, 'r') as f:
            r = json.load(f)
    except json.decoder.JSONDecodeError:
        r = {}

    return r


def chifra_blocks_cmd(block):
    return f'chifra blocks {block}'


# Load proposer-block pairs for each DAO found on boardroom
df_lookup = pd.read_csv(os.path.join(DATADIR, 'boardroom_address_lookup.csv'), index_col=False)

df_lookup['contractAddress'] = None
sesh = requests.Session
for i, row in df_lookup.iterrows():
    # Get all transactions in the block
    print(f"Processing {row['protocol']}...")
    cmd = chifra_blocks_cmd(row['blockNumber'])
    r = process_blocks_as_stream(cmd)

    try:
        transactions = r['data'][0]['transactions']

        # Find transaction(s) with proposer as 'from' address and get corresponding 'to' address, if any
        to_addresses = [t['to'] for t in transactions if t['from'] == row['proposer']]
        if len(to_addresses) > 1:
            print(f"Warning: found more than one address for {row['protocol']}")
        try:
            to_address = to_addresses[0]
        except IndexError:
            print(f"No contract address found for {row['protocol']}")
            to_address = None
    except KeyError:
        print(f"No contract address found for {row['protocol']}")
        to_address = None        

    # Add to df
    df_lookup.at[i, 'contractAddress'] = to_address

    time.sleep(2)

# Save to new file
df_lookup.drop(columns=['blockNumber', 'proposer'])
df_lookup.to_csv('boardroom_contract_addresses.csv')