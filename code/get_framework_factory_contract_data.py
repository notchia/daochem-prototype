import os
import json
import pandas as pd

from modules.config import CWD, TMPDIR, DATADIR
import modules.trueblocks as tb
from modules.utils import load_json

os.chdir(CWD)

# Load factory contract addresses for each DAO framework
df_factories = pd.read_csv(os.path.join(DATADIR, 'framework_factory_contract_addresses.csv'), index_col=False)

# Run chifra list for all addresses to generate monitors
addresses = list(df_factories['factoryAddress'])
addresses_str = " ".join(addresses)
cmd = tb.chifra_list(addresses)
tb.pipe_chifra_call(cmd)

# Run chifra export for each address
for i, row in df_factories.iterrows():
    version = row['version']
    print(version)
    files = os.listdir(TMPDIR)
    matching = [f for f in files if (version in f)]
    addr = row['factoryAddress']
    fpath = os.path.join(DATADIR, f'trueblocks_export_{version}.json')

    if not any(matching):
        try:
            cmd = tb.chifra_export(addr)
            r = tb.pipe_chifra_call_with_sleep(cmd, label=f"trueblocks_factory_{row['version']}_full")
            for j in r:
                with open(f"trueblocks_factory_{row['version']}.json", "a") as outfile:
                    json.dump(j, outfile)
        except Exception as e:
            print(e)
    else:
        print(f"using {len(matching)} previous files")
        transactions = {}
        matching.sort(key=lambda s: int(os.path.splitext(s)[0].split('_')[-1]))
        for f in matching:
            count = os.path.splitext(f)[0].split('_')[-1]
            t = load_json(os.path.join(TMPDIR, f))
            t_cut = tb.get_minimal_transaction_info(t)
            transactions[int(count)] = t_cut
            
        with open(fpath, 'w') as out:
            json.dump(transactions, out, indent=4)
