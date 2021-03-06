# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:13:21 2018

@author: Christine
"""

import datetime
import json
import urllib.request

import tweepy

# Create variables for each key, secret, token
consumer_key = 'xxxxxx'
consumer_secret = 'xxxxxx'
access_token = 'xxxxxx'
access_token_secret = 'xxxxxx'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '890c43989369982c4ad8225087de1dbe'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    #tweet ='Current weather in :'+data['city'],data['country']+''
     #tweet = 'Name : '+user.name+', User Id :'+user.id_str+''
    tweet ='Current weather in : {}, {},\nTemperature {} {} {}, \nMax: {}, Min: {}, \nWind Speed: {}, Degree: {}, \nHumidity: {}, \nCloud: {}, \nPressure: {}, \nSunrise at: {}, \nSunset at: {},\nLast update from the server: {}'.format(data['city'], data['country'], data['temp'], m_symbol, data['sky'],data['temp_max'], data['temp_min'],data['wind'], data['wind_deg'],data['humidity'],data['cloudiness'],data['pressure'],data['sunrise'],data['sunset'],data['dt'])  
    api.update_status(status=tweet)
   # print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
   # print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
   # print('---------------------------------------')
  
#taiwan id 1668284
    #indonesia id 1643084 australia id : 2058645

if __name__ == '__main__':
    try:
        # Write a tweet to push to our Twitter account
        data_output(data_organizer(data_fetch(url_builder(2058645))))
     
       
    except IOError:
        print('no internet')
        
        