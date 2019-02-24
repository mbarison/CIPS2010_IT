#!/usr/bin/env python3

import csv, json, os

data_struct = []

with open(os.path.expanduser("~/Downloads/CIPCode2010_IT_v2.csv")) as f:
    r = csv.DictReader(f)
    
    for i in r:
        if len(i['CIPCode']) == 2:
            group = {'text': i['CIPTitle'].strip('.'), 'children': []}
            data_struct.append(group)
        elif len(i['CIPCode']) == 7:
            cip = {'id': i['CIPCode'], 'text': i['CIPTitle'].strip('.')}
            data_struct[-1]['children'].append(cip)
            
            

with open("cips2010_data.js", "w") as o_f:            
    o_f.write("cips2010_data = %s;" % json.dumps(data_struct))
            