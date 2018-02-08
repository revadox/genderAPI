import json
import urllib2

first_list = ["darshan","kiran","vijay","aniruddh","hemant","divy","divya","sabina"]

myKey = "SVlpDsZvjtJXjjzxCH"
names = ""
data = []

names = '; '.join(first_list)

data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + myKey + "&name=" + names))

for person in data["result"]:
    print "name: " + person["name"] + " gender: " + person["gender"]
