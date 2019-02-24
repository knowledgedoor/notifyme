import urllib.request
import re
import winsound

url=urllib.request.urlopen('http://www.ignou.ac.in/ignou/studentzone/results/2')

# in case you need a session
#cd = { 'sessionid': '123..'}

#r = requests.get(url, cookies=cd)
# or without a session: r = requests.get(url)
#r.content
#print ("result code:" + str (url.getcode()))

data = url.read()
#print(data)

paragraphs = re.findall(r'<u>(.*?)</u>', str(data))

#print(paragraphs)
match = "['Updated on 15 Feb, 2019']"
constr = str(paragraphs)
if match != constr:
    winsound.PlaySound("smokedetector1", winsound.SND_FILENAME)

