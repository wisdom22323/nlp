import json
import urllib.parse
import urllib.request

solr_url = 'http://localhost:8983/solr'
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def load(collection, data):
    req = urllib.request.Request(
        url='{0}/{1}/update'.format(solr_url, collection),
        data = json.dumps(data).encode('utf-8'),
        headers = {'content-type':'application/json'})

    with opener.open(req) as res:
        print(res.read().decode('utf-8'))

    url = '{0}/{1}/update?softCommit=true'.format(solr_url, collection)
    req = urllib.request.Request(url)
    with opener.open(req) as res :
        print(res.read().decode('utf-8'))