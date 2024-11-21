#!/usr/bin/env python3

import os
import sys
import subprocess
from config_map import config_map

program = sys.argv[0]
if len(sys.argv) < 2:
    print('What config module do you want?')
    print(f'For example, try "{program} {list(config_map.keys())[0]}".')
    print('List of modules:')
    print(*config_map.keys(), sep='\n')
elif len(sys.argv) > 2:
    print('Expect one module specify, receive', len(sys.argv) - 1)
    print('List of modules:')
    print(*config_map.keys(), sep='\n')
else: # len(sys.argv) must be 2 now ffs
    if sys.argv[1] in ['-l', 'list']:
        print(*config_map.keys(), sep='\n')
    else:
        config_file = config_map.get(sys.argv[1])
        if config_file:
            print('Open file', os.path.expanduser(config_file))
            subprocess.run([os.environ.get('VISUAL', 'nvim'),
                            os.path.expanduser(config_file)])
        else:
            print("Don't recognize module.")
            print('List of modules:')
            print(*config_map.keys(), sep='\n')
