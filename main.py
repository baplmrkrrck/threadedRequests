import requests, json, threading

file = open("json.txt", "w")

def worker(n):
    r = requests.get("https://clarksonmsda.org/api/get_product.php?pid=" + str(n))

    if "pid" in r.text:
        file.write(r.text + "\n")
        print(str(n))

i = 0

while i <= 200:
    w = threading.Thread(name='tid_' + str(i), target=worker, args=(i,))
    w.start()

    i += 1
