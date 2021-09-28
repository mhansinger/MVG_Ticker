'''
This is a test version for the MVG Ticker
@author: mhansinger
'''

import numpy as np
import time
import mvg_api as mvg
from pyemojify import emojify
from colr import color

class mvg_ticker(object):
    def __init__(self):
        print(' ')
        print(emojify(':train: :boom: This is the MVG ticker!:boom: :train: :skull:'))
        print(' ')
        self.station_name = None
        self.station = None
        self.departures = None

        name = 'Theresienstrasse'
        self.set_station(name)


    def set_station(self,station_name):
        self.station_name = station_name
        self.set_mvg()
        print('Departure station is: ',self.station_name)

    def set_mvg(self):
        try:
            self.station = mvg.Station(self.station_name)
        except NameError:
            print('I don´t know this station!')

    def get_departures_times(self, station_name,nr = 4):

        self.set_station(station_name=station_name)

        self.departures = self.station.get_departures()[:nr]

        this_time = time.time()

        for i in range(0,nr):
            destination = self.departures[i]['destination']
            departure_times = self.departures[i]['departureTimeMinutes']
            label = self.departures[i]['label']
            back_color = self.departures[i]['lineBackgroundColor'][-7:]
            label_color = color(label, fore="#fff", back=back_color)

            if departure_times < 1:
                try:
                    destination = self.departures[i+nr]['destination']
                    departure_times = self.departures[i+nr]['departureTimeMinutes']
                    label = self.departures[i+nr]['label']
                    back_color = self.departures[i+nr]['lineBackgroundColor']
                    label_color = color(label, fore="#fff", back=back_color)

                    out_text = label_color + ' to ' + destination + ' in:\t' + str(departure_times) + ' min.'
                    print(out_text)

                except IndexError:
                    print('Index Error')
                    pass
            elif departure_times > 100:
                pass
            else:
                out_text = label_color + ' to ' + destination + ' in:\t' + str(departure_times) + ' min.'
                print(out_text)


if __name__ == '__main__':
    ticker = mvg_ticker()
    ticker.get_departures_times(station_name='Theresienstrasse',nr = 4)
