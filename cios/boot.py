#!/usr/bin/python3

"""Module run at boot time

bootstrap() is the main function, and is called as soon as the module is loaded."""

import stackless
import importlib
import sys
import os

from .config import config
import .util

def bootstrap(*args, **kwargs):
  loc = config["Boot"].get("ModuleLocation", "/etc/cios.d/")
  sys.path.append(loc)
  
  modules = []
  
  for name in os.listdir(loc):
    if name.endswith(".py"):
      module = importlib.import_module( module[:-3] )
      module.bootstrap(*args, **kwargs)
      modules.append(module)
  
  stackless.run()