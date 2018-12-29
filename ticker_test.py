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
        print(emojify(':train: :boom: This is the MVG ticker!:boom: :train:'))
        print(' ')
        self.station_name = None
        self.station = None
        self.departures = None

        var = 'Theresienstraße'#input("Please enter the station name: ")
        self.set_station(var)
        self.set_mvg()

    def set_station(self,station_name):
        self.station_name = station_name
        print('Departure station is: ',self.station_name)

    def set_mvg(self):
        try:
            self.station = mvg.Station(self.station_name)
        except NameError:
            print('I don´t know this station!')

    def get_departures_times(self, nr = 4):
        self.departures = self.station.get_departures()[:nr]

        # set empty array
        #destination = np.zeros(nr)
        #departure_times = np.zeros(nr)
        #time_diff_min = []

        this_time = time.time()

        for i in range(0,nr):
            destination = self.departures[i]['destination']
            departure_times = self.departures[i]['departureTimeMinutes']
            label = self.departures[i]['label']
            back_color = self.departures[i]['lineBackgroundColor'][-7:]
            label_color = color(label, fore="#fff", back=back_color)

            '''
            if departure_times < 1:
                try:
                    destination = self.departures[i+nr]['destination']
                    departure_times = self.departures[i+nr]['departureTimeMinutes']
                    label = self.departures[i+nr]['label']
                    back_color = self.departures[i+nr]['lineBackgroundColor']
                    label_color = color(label, fore="#fff", back=back_color)
                except IndexError:
                    pass
            '''

            out_text = label_color+' to '+destination+ ' in:\t'+ str(departure_times)+' min.'
            print(out_text)

if __name__ == '__main__':
    ticker = mvg_ticker()
    ticker.get_departures_times()
