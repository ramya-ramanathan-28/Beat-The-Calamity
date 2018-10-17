

import folium
import pandas
import numpy as np
def renderMap():
    
    colnames = ['Filename']
    data = pandas.read_csv('people.csv', names=colnames)

    lat_long = data.Filename.tolist()
    lat_long = lat_long[1:]
    #print(lat_long)

    lat_long_new = [x[:-4] for x in lat_long]
    ll = [tuple(s.split('_')) for s in lat_long_new]
    new_ll = []
    for item in ll:
        l = []
        l.append(float(item[0]))
        l.append(float(item[1]))
        new_ll.append(tuple(l))
    print(new_ll)
    print(len(ll))

    newList = np.unique(new_ll, axis=0)
    final = [] 
    for i in newList:
        final.append(tuple(i))

    print(final)
    print(len(final))
    latlon = final
    mapit = folium.Map( location=[13, 51], zoom_start=5)
    for coord in latlon:
        folium.Marker( location=[ coord[0], coord[1] ]).add_to( mapit )
    mapit.save( './templates/map.html')

renderMap()
