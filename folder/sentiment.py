import urllib.request
import urllib.response
import sys
import http.client, urllib
import json
import re

def TextAnalytics(documents):
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection(url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

accessKey = 'd83461db44e0491f95295d5f94f80e10'
#https://westcentralus.api.cognitive.microsoft.com/text/analytics
url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/Sentiment'

documents = { 'documents': []}
list_files = [ 'day1.txt','day2.txt', 'day3.txt', 'day4.txt', 'day5.txt', 'day6.txt']
dates = ['18 Aug', '19 Aug', '20 Aug', '21 Aug', '22 Aug', '25 Aug' ]
list_score = []
count = 1
for file in list_files:
    print(file)
    f = open(file,encoding="utf-8")

    line=f.readline()
    #print(line)
    #line = line[0:500]
    print(line)
    avg = 0
    n = 1
    
    while line:
        documents = { 'documents': []}
        documents.setdefault('documents').append({"language":"en","id":str(count),"text":line})#"id":str(count),
        count=count+1
        
        if count==900:
            break
        line=f.readline()
    result = TextAnalytics (documents)
    obj=json.dumps(json.loads(result.decode("utf-8")), indent=4)
    print(json.loads(result.decode("utf-8")))
        #avg = avg + json.loads(result.decode("utf-8"))['documents'][0]['score']
    #list_score.append(json.loads(result.decode("utf-8"))['documents'][0]['score'])
    print(obj)
    mini = 1
    for k in json.loads(result.decode("utf-8")).items():
        if k[0]=='documents':
            for items in k[1]:
                if int(items["score"])<mini:
                    mini = items["score"]
                avg = avg + items["score"]
                n = n + 1
    print(avg/n)
    list_score.append(avg/n)
    f.close()

   


    
#print(obj['documents'])


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
plt.plot(dates,list_score,'c',label='Emotion', linewidth=5)
plt.xlabel('Date')
plt.ylabel('Emotion')
plt.title('Trend of sentiment during Kerala Floods')
plt.legend()
plt.grid(True,color='k')
plt.savefig(r'trend2.jpg')


