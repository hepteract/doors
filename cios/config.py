#!/usr/bin/python3

"""Configuration handling"""

import configparser

def get_config(location = "/etc/doors.ini"):
  config = configparser.ConfigParser()
  config.read(location)
  
  return config

config = get_config()