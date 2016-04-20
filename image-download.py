import urllib
import json
import time
# urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "a.jpg")
with open('final_results.json', 'r') as f:
    data = json.load(f)


for k, v in data.items():
    title, url = k, v

    try:
        urllib.urlretrieve(url, title)
    except IOError:
        'File does not exsist'
        
    time.sleep(1)