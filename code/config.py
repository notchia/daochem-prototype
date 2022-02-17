import os

# Directories
CWD = os.path.dirname(os.path.abspath(__file__))
CWD = os.sep.join(CWD.split(os.sep)[:-1])
TMPDIR = os.path.join(CWD, 'tmp')
DATADIR = os.path.join(CWD, 'data')

# TrueBlocks
TRUEBLOCKS_URL = "http://localhost:8080/"