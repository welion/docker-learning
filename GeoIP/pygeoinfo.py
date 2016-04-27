#!/usr/bin/python env

import os
import sys


if os.path.isfile('/opt/GeoIP/Geo.dat') == False :
        os.makedirs('/opt/GeoIP')
        os.chdir('/opt/GeoIP')
        os.system('wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz')
        os.syetem('tar -zvxf GeoLiteCity.dat.gz')
        os.system('mv GeoLiteCity.dat /opt/GeoIP/Geo.dat')




import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(target):
        rec = gi.record_by_name(target)
        city = rec['city']
#       region = rec['region_name']
        country = rec['country_name']
        longitude = rec['longitude']
        latitude = rec['latitude']
        print '[*] Target: ' + target + ' Geo-located.'
        print '[+] ' + str(city) + ' ' + ' ' + str(country) 
        print '[+] Latitude: ' + str(latitude) + ', Longitude: ' + str(longitude)

target = "101.245.201.147"
printRecord(target)
