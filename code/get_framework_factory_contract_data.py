import os
import requests
import pandas as pd

from modules.trueblocks import chifra_list, get_chifra_as_json
from config import CWD, TMPDIR, DATADIR

os.chdir(CWD)

# Load factory contract addresses for each DAO framework
df_factories = pd.read_csv(os.path.join(DATADIR, 'framework_factory_contract_addresses.csv'), index_col=False)

sesh = requests.session()
for i, row in df_factories.iterrows():
    url = chifra_list(row['factoryAddress'])
    print(url)
    r = get_chifra_as_json(url, session=sesh)
