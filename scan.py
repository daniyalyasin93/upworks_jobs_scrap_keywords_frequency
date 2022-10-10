from reader import make_reader

import json
import re

def unique_list(input_list):
    output_list = []
    for word in input_list:
        if word not in output_list:
            new_word = re.sub(r'[^\w]', '', word).strip()
            if '' != new_word:
                output_list.append(new_word)
    return output_list

reader = make_reader('db.sqlite')
upworks_url = 'XXXX'
reader.add_feed(upworks_url)
reader.update_feeds()


with open('statistics.dump', 'r') as f:
    statistics = json.load(f)
    
with open('ignored.dump', 'r') as f: 
    ignored = json.load(f)


for item in ignored:
    if item in statistics:
        statistics[item] = 0
        

for entry in entries:
    txt = entry
    content = re.search(r"VALUE='([^\']+)'", str(txt.content).upper())
    #dir(content)
    #content
    list_of_words = content.group(1).split(' ');

    list_of_words = unique_list(list_of_words)
    for word in list_of_words:
        if word not in ignored:
            if word not in statistics:
                statistics[word] = 1
            else:
                statistics[word] = statistics[word] + 1
                
# e.g. file = './data.json' 
with open('statistics.dump', 'w') as f: 
    json.dump(statistics, f)
    
with open('ignored.dump', 'w') as f: 
    json.dump(ignored, f)
