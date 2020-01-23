#!/usr/bin/env python3.7

import os
import sys
import yaml

from Xlib import X, XK, display


class initX(object):
    def __init__(self):
        # Initialize X classes
        # X server display and screen
        
        self.display = display.Display()
        self.screen = self.display.screen()
        self.colormap = self.screen.default_colormap
        
    def kh_handler(self):
        pass 
    
    
#if __name__ == "__main__":

    
    