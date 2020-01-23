#!/usr/bin/env python3.7

import os
import sys
import yaml

# x11 lib
from Xlib import X, XK, display

# Open event handler yaml
with open('config/event_handler.yaml') as conf:
    config = yaml.safe_load(conf)

class initX(object):
    def __init__(self):
        # Initialize X classes
        # X server display and screen
        
        self.display = display.Display()
        self.screen = self.display.screen()
        self.colormap = self.screen.default_colormap
        
    def kh_handler(self):
        print(config)
    
    
if __name__ == "__main__":
    x = initX()
    x.kh_handler()
    
    