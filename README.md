# Beat-The-Calamity
</br>
Team : Beat The Calamity <br/>
College : R.V. College of Engineering, Bangalore <br/>
Team Members : Ramya Ramanathan, Sindhu B Dinesh, Malika Makker <br/>

### Topic : Disaster Management using Satellite Images and Social Media Posts

#### Problem Statement : To build a robust disaster management system, which can be used to analyse an area post disaster and to assist the people in distress, by drawing helpful insights from the satellite images and the social media posts of people regarding their state.

### Components:
#### 1. Tracing Usable Roads in a Damaged Area
Post a natural disaster, roads are often blocked and authorities have a hard time reaching out to people in need of help. Using satellite images, roads can be traced out which are safe and in a condition to be used

#### 2. Distinguishing areas based on the level of damage
Using satellite images of the damaged areas, various areas can be put in different categories based on the extent of damage. This data can be then used by the authorities to prioritise their assistance to different areas and analyse the kind of assistance that might be required by an area. The areas with low level of damage can be used to set up medical camps or to provide any other kind of assistance.

#### 3.  Analysing areas where people could be stranded
Using satellite images, areas where people could be stranded and in need of help can be analysed. Also, if network continues to persist, people   might ask for help on social media and should be brought out to the authorities immediately.   

#### 4.  Quantifying items to be delivered to different areas
Based on the number of requests received and the level of damage of a particular area, the resources available at hand can be divided and sent to different areas by the NGOs, which collected those resources. The number of requests can be gathered through social media posts.

#### 5.  Locating closest help centers
The nearest help centers can be identified and if none are found in the immediate neighbourhood, radius can be extended to locate the next closest center. The location of the help centers will be fed to the system and based on the user location, the closest help center would be suggested.

### How to run our application : 
-Install all the required dependencies and execute python application.py and the application runs on localhost <br/>
-It is also hosted at beat-the-calamity.azurewebsites.net <br/>

### Find our documentation : 
-beat the calamity.pptx and beat-the-calamity.docx <br/>
-Youtube link: https://youtu.be/kmBXSR86L1Q  <br/>

### Find in our repository : 
application.py - a python flask based 
date.py - fetches tweets for a given duration and hashtag <br/>
flooded_area_road_detection.py - used to identify roads during floods <br/>
image_diff.py - used to identify damages areas <br/>
tensorflow-human-detection.py - uses object detection to identify people <br/>
map.py - used to plot stranded people <br/>
items2.py - used to identify necessary items <br/> 
week.py and sentiment.py - used to render sentiment trend <br/> 
templates folder - contains all the front end HTML files <br/>
 

