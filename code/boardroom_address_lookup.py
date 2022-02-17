import os
import requests
import pandas as pd

from modules.trueblocks import chifra_blocks, get_chifra_as_json
from config import CWD, TMPDIR, DATADIR

os.chdir(CWD)

# Load proposer-block pairs for each DAO found on boardroom
df_lookup = pd.read_csv(os.path.join(DATADIR, 'boardroom_address_lookup.csv'), index_col=False)

df_lookup['contractAddress'] = None
sesh = requests.Session
for i, row in df_lookup.iterrows():
    # Get all transactions in the block
    url = chifra_blocks(row['blockNumber'])
    r = get_chifra_as_json(url, session=sesh)
    transactions = r['transactions']

    # Find transaction(s) with proposer as 'from' address and get corresponding 'to' address, if any
    to_addresses = [t['to'] for t in transactions if transactions['from'] == row['proposer']]
    if len(to_addresses) == 0:
        print(f"No contract address found for {row['cname']}")
        to_address = None
    else:
        if len(to_addresses) > 1:
            print(f"Warning: found more than one address for {row['cname']}")
        to_address = to_addresses[0]

    # Add to df
    df_lookup.iat[i, 'contractAddress'] = to_address

# Save to new file
df_lookup.drop(columns=['blockNumber', 'proposer'])
df_lookup.to_csv('boardroom_contract_addresses.csv')
