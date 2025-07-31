# Programming for the ADALM1000 in Python
# EE1103L Electronics Lab - Addon Module
# BS in Electronic Systems - IIT Madras
# Course Instructor : Dr.Janakiraman Viraraghavan
# Control Code by Aditya Rao, 23f3000019@es.study.iitm.ac.in
# April 2024
# Github : https://github.com/aditya-rao-iit-m/adalm1000
# GNU GPL v3.0

from signal import signal, SIG_DFL, SIGINT
import sys
import time, tempfile, os
from random import randrange
from pysmu import Session, LED
from ar_iitm import *

info = 'This is an RGB LED + Clock test for the ADALM1000'
terminate = 'Press Ctrl-C to end this program'

ar_iitm_adalm1000_info.show_message(info,terminate)

if __name__ == '__main__':
    signal(SIGINT, SIG_DFL)
    instance = Session()
    if not instance.devices:
        sys.exit(1)

for usb_smu in instance.devices:
    while True:
        #control the notification leds
        ar_iitm_adalm1000_pin.red_led_high(usb_smu,0.1)
        ar_iitm_adalm1000_pin.red_led_low(usb_smu,0.1)
        ar_iitm_adalm1000_pin.green_led_high(usb_smu,0.1)
        ar_iitm_adalm1000_pin.green_led_low(usb_smu,0.1)
        ar_iitm_adalm1000_pin.blue_led_high(usb_smu,0.1)
        ar_iitm_adalm1000_pin.blue_led_low(usb_smu,0.1)
        #control the pio digital pins
        ar_iitm_adalm1000_pin.pio0_high(usb_smu,0)
        ar_iitm_adalm1000_pin.pio1_high(usb_smu,0)
        ar_iitm_adalm1000_pin.pio2_high(usb_smu,0)
        ar_iitm_adalm1000_pin.pio3_high(usb_smu,0.5)
        ar_iitm_adalm1000_pin.pio0_low(usb_smu,0)
        ar_iitm_adalm1000_pin.pio1_low(usb_smu,0)
        ar_iitm_adalm1000_pin.pio2_low(usb_smu,0)
        ar_iitm_adalm1000_pin.pio3_low(usb_smu,0.5)
            
            
            
            
