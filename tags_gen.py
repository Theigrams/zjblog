import requests
import os

tags_get = requests.get('http://localhost:4000/zjblog/api/tags.json')
tags = tags_get.json()

# for tag in tags:
#     print(tag+':',tags[tag])

build_tags = [tag for tag in tags]

for root, dirs, files in os.walk('./tag'):
    for file_name in files:
        tag = file_name[:-3]
        if tag in tags and tag in build_tags:
            build_tags.remove(tag)
print("Building new tags:", build_tags)

tag_pattern = '---\n'
tag_pattern += 'layout: tagpage\n'
tag_pattern += 'title: "Tag: %s"\n'
tag_pattern += 'tag: %s\n'
tag_pattern += '---\n'

for tag in build_tags:
    with open('./tag/'+tag+'.md', 'w') as f:
        f.write(tag_pattern % (tag, tag))
