import csv, threading, json


table_headers = ["prod_id","prod_sku","prod_cat","prod_name"]
f = open("combine.csv", mode='w')
writer = csv.DictWriter(f, fieldnames=table_headers)
writer.writerow({"prod_id": "prod_id","prod_sku": "prod_sku","prod_cat": "prod_cat","prod_name": "prod_name"})

temp = []
reader = open("json.txt", "r")
for line in reader:
    if "prod_id" in line:
        l = json.loads(line)["data"]
        writer.writerow({"prod_id": l["prod_id"],"prod_sku": l["prod_sku"],"prod_cat": l["prod_cat"],"prod_name": l["prod_name"]})
