# python3.8

import csv
import os
from pathlib import Path
import json

if __name__ == "__main__":
    filename = './data.csv'
    directory = 'result'
    keys = ['name', 'description', 'image', 'external_url']

    Path(directory).mkdir(parents=True, exist_ok=True)

    with open(filename, encoding='UTF-8-sig') as f:
        data = csv.DictReader(f)

        for i, line in enumerate(data):
            if 'ID' not in line:
                print(f'error: line {i+1} have no ID')
            output = os.path.join(directory, line.get('ID'))
            with open(output, 'w') as o:
                print('==================================>')
                print(line)
                meta = {
                    'attributes': []
                }
                for k, v in line.items():
                    if k in keys:
                        meta.setdefault(k, v)
                    else:
                        meta['attributes'].append({"trait_type": k,
                                                   "value": v})
                    print(meta)
                json.dump(meta, o)
