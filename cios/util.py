#!/usr/bin/python3

"""Utility functions for CIOS"""

import stackless
import sys
import os

def instant_args(*args, **kwargs):
  def decorator(func):
    f = stackless.tasklet(func)(*args, **kwargs)
    return f
  
def instant(func):
  f = stackless.tasklet(func)()
  return f