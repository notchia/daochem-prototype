import os
import web3
import pandas as pd

from ens.auto import ns

from modules.config import TMPDIR, DATADIR
from modules.utils import load_json, print_groupby

## Load DeepDAO data
df = pd.read_csv(os.path.join(TMPDIR, 'deepdao.csv'))
df['cleanAddress'] = None

for i, row in df.iterrows():
    address = row['governance_address']
    if web3.utils.isAddress(address):
        df.at[i, 'cleanAddress'] = address
    else:
        try:
            df.at[i, 'cleanAddress'] = ns.address(address)
        except Exception as e:
            print(e)

print(df)