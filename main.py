import requests, json, threading, os
path = "data/"
def worker(n):
    r = requests.get("https://clarksonmsda.org/api/get_product.php?pid=" + str(n))

    if "prod_id" in r.text:

        file = open(path + str(n) + ".txt", "w")
        file.write(r.text + "\n")
        file.close
        print(str(n))


for root,dirs, files in os.walk(path):
    for fn in files:
        fp = root+os.sep+fn
        os.remove(fp)

if os.path.isdir(path) == False:
    os.makedirs(path)
i = 0

while i <= 200:
    w = threading.Thread(name='tid_' + str(i), target=worker, args=(i,))
    w.start()

    i += 1
