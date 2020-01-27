import pandas as pd
import os
import gpxpy


in_dir = './data_rename/'
out_dir = './data_rename_csv/'
files = os.listdir(in_dir)


def parsegpx(f):
    #Parse a GPX file into a list of dictoinaries.  
    #Each dict is one row of the final dataset
    
    points2 = []
    with open(f, 'r') as gpxfile:
        # print f
        gpx = gpxpy.parse(gpxfile)
        data = gpx.tracks[0].segments[0].points
        dff = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
        for point in data:
            dff = dff.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)
    return dff   


for f in files:
    df = parsegpx(in_dir + f)
    df.to_csv(out_dir + f[:-4] +'.csv')
    print('file ' + f + ' complete')



#test_df = parsegpx('data_rename/2019-04-06 17:37:07.gpx')