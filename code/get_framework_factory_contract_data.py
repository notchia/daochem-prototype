import os
import pandas as pd

import  modules.trueblocks as tb
from config import CWD, DATADIR

os.chdir(CWD)

# Load factory contract addresses for each DAO framework
df_factories = pd.read_csv(os.path.join(DATADIR, 'framework_factory_contract_addresses.csv'), index_col=False)

# Run chifra list for all addresses to generate monitors
addresses = list(df_factories['factoryAddress'])
addresses_str = " ".join(list)
cmd = tb.chifra_list(addresses)
tb.pipe_chifra_call(cmd)

# Run chifra export for each address
for i, row in df_factories.iterrows():
    addr = row['factoryAddress']
    fpath = os.path.join(DATADIR, f'trueblocks_export_{addr}.json')
    cmd = tb.chifra_export(addr)
    tb.pipe_chifra_call(cmd)
