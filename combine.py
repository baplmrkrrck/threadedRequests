import csv, threading, json, os


table_headers = ["prod_id","prod_sku","prod_cat","prod_name"]
f = open("combine.csv", mode='w')
writer = csv.DictWriter(f, fieldnames=table_headers)
writer.writerow({"prod_id": "prod_id","prod_sku": "prod_sku","prod_cat": "prod_cat","prod_name": "prod_name"})

temp = []
for root,dirs, files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn

        f = open(fp, 'r')
        print(fp)
        for line in f:
            l = json.loads(line)["data"]
            writer.writerow({"prod_id": l["prod_id"],"prod_sku": l["prod_sku"],"prod_cat": l["prod_cat"],"prod_name": l["prod_name"]})
