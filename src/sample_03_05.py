import sqlitedatastore as datastore
import json

if __name__ == '__main__':
    datastore.connect()
    for doc_id in datastore.get_all_ids(limit=-1):
        row = datastore.get(doc_id,['id','content','meta_info'])
        print(row['id'], json.loads(row['meta_info']), row['content'][:100])
    datastore.close()

'''
1 {"url": "https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%A4%E3%82%B9%E3%83%A9%E3%83%B3%E3%83%89", "title": "\u30a2\u30a4\u30b9\u30e9\u30f3\u30c9"} アイスランド<__EOS__>
アイスランドは、北ヨーロッパの北大西洋上に位置する島国で、共和制を取る国家（アイスランド共和国[2]）である。首都はレイキャヴィーク。総人口は約35万5620人。島国で
1 {'url': 'https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%A4%E3%82%B9%E3%83%A9%E3%83%B3%E3%83%89', 'title': 'アイスランド'} アイスランド<__EOS__>
アイスランドは、北ヨーロッパの北大西洋上に位置する島国で、共和制を取る国家（アイスランド共和国[2]）である。首都はレイキャヴィーク。総人口は約35万5620人。島国で
'''

