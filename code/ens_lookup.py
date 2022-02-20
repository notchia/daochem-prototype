import os
import pandas as pd
from web3 import Web3, HTTPProvider
from ens import ENS

from modules.config import TMPDIR, DATADIR, API_KEY
from modules.utils import load_json, print_groupby

## Load DeepDAO data
df = pd.read_csv(os.path.join(DATADIR, 'deepdao.csv'))
df['cleanAddress'] = None

provider = HTTPProvider(API_KEY)
w3 = Web3(provider)
ns = ENS(provider)

for i, row in df.iterrows():
    address = row['governance_address']
    if w3.isAddress(address):
        df.at[i, 'cleanAddress'] = address
    else:
        try:
            df.at[i, 'cleanAddress'] = ns.address(address)
        except Exception as e:
            print(e)

print(df)
df.to_csv(os.path.join(DATADIR, 'deepdao_cleaned.csv'))
