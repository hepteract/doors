#!/usr/bin/python3

"""Utility functions for CIOS"""

import stackless
import sys
import os

def instant_args(*args, **kwargs):
  def decorator(func):
    f = stackless.tasklet(func)(*args, **kwargs)
    f.run()
    return f
  
def instant(func):
  f = stackless.tasklet(func)()
  f.run()
  return f