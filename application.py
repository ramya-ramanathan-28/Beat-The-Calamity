from flask import Flask, render_template, request, json, session, url_for, redirect, flash
#from passlib.hash import sha256_crypt
import time
import datetime
#from folder import image_diff
#from folder import flooded_area_road_detection
#from folder import items2
from pathlib import Path
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60
#import MySQLdb
'''
import math  
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist
#list_help = ["food", "blanket", "tent", "medicines"]
helpcenter_names = ["Bangalore", "Chennai", "Hyderabad"]
helpcenters = [[12.9716, 77.5946],[17.3850, 78.4867], [13.0827, 80.2707]]
flood = [10.1849, 76.3753]
min_dist = 99999
dist = []
for element in helpcenters:
    dist.append(calculateDistance(flood[0], flood[1], element[0], element[1]))

Z = [x for _,x in sorted(zip(dist,helpcenter_names))]

for item in Z:
    if len(list_help)== 0:
        break
    print(list_help)
    pos = input("Enter the index of things that can be supplied")
    list_help.pop(int(pos))

'''
items=['table', 'dal', 'rice', 'mug', 'diapers', 'water']
@app.route("/", methods = ['POST', 'GET'])
def trends():
        return render_template("road.html")

@app.route("/road", methods = ['POST', 'GET'])
def road():

        if request.method == 'POST' :
                
                if 'image' in request.form:
                        image = str(request.form['image'])
                        #flooded_area_road_detection.road_detection(image)
                        return render_template("road_results.html")
    
        return render_template("road.html")

@app.route("/damage", methods = ['POST', 'GET'])
def damage():

        if request.method == 'POST' :
                
                if 'before' in request.form and 'after' in request.form:
                        before = str(request.form['before'])
                        after = str(request.form['after'])
                        #image_diff.imageCompare(before, after)
                        return render_template("damage_results.html")
    
        return render_template("damage.html")


@app.route("/helpcenter", methods = ['POST', 'GET'])
def helpcenter():

        if request.method == 'POST' :
                
                if 'hashtag' in request.form:
                        hashtag = str(request.form['hashtag'])
                        #items = items2.fetch_items(hashtag)
                        return render_template("helpcenter.html",  items = items)
    
        
        return render_template("twitter.html")


@app.route("/map", methods = ['POST', 'GET'])
def map():
            return render_template("map.html")

                         
if __name__ == "__main__":
    app.run(debug = False)
