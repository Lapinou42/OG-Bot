import util
from mechanize import Browser
from bs4 import BeautifulSoup
import re
import logging


class Movement:
    def __init__(self, browser, universe):
        self.url_provider = util.UrlProvider(universe)
        self.logger = logging.getLogger('ogame-bot')
        self.browser = browser

    def get_fleet_movement(self):
        url = self.url_provider.get_page_url('movement')
        res = self.browser.open(url)
        soup = BeautifulSoup(res.read(), "lxml")
        movement_nodes = soup.findAll("div", { "class" : "fleetDetails detailsOpened" })
        fleet_movements = []
        for movement_node in movement_nodes:
            origin_planet_coords = self.parse_coords(movement_node.find("span", {"class": "originCoords"}).text)
            origin_planet_name = movement_node.find("span", {"class": "originPlanet"}).text.strip()
            destination_coords = self.parse_coords(movement_node.find("span", { "class" : "destinationCoords tooltip"}).text)
            movement = FleetMovement(origin_planet_coords, origin_planet_name,  destination_coords)
            fleet_movements.append(movement)
        return fleet_movements

    def parse_coords(self, text):
        return text.replace('[', '').replace(']', '')

    def get_fleet_slots_usage(self):
        url = self.url_provider.get_page_url('movement')
        res = self.browser.open(url)
        soup = BeautifulSoup(res.read())
        slots_info_node = soup.find("span", {"class", "fleetSlots"})
        if slots_info_node  != None:
            current_slots = int(slots_info_node.find("span", {"class", "current"}).text)
            all_slots = int(slots_info_node.find("span", {"class", "all"}).text)
        else:
            current_slots = 0
            all_slots = 1
        return (current_slots, all_slots)

class FleetMovement(object):
    def __init__(self, origin_coords, origin_name, destination_coords):
        self.origin_coords = origin_coords
        self.origin_name = origin_name
        self.destination_coords = destination_coords

    def __str__(self):
        return "Fleet from planet %s(%s) to planet %s" % (self.origin_name, self.origin_coords, self.destination_coords)
