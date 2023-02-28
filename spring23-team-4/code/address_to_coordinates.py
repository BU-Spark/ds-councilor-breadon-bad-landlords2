#
# Simple address to coordinates code
# Author: Francesco Ciraolo
# Note: improved version of https://stackoverflow.com/a/32333188
#

from geopy.geocoders import Nominatim


class AddressToCoordinates:

    def __init__(self, user_agent='undefined'):
        self.user_agent = user_agent
        self.geolocator = Nominatim(user_agent=user_agent)

    def get_coordinates(self, address):
        location = self.geolocator.geocode(address)
        return location.latitude, location.longitude if location else None, None
