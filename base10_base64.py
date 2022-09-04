# ------------------------------------------------------------------------------
# Project : The Very First Daisi Hackathon
# File : base10_to_base64.py
# Create on :
# Purpose :
#    This python file is developed for The Very First Daisi Hackathon .
#    This function will convert the base10 to base64.
#    This is help us to encode the number and float value and we use this function for data compression algorithm
# ------------------------------------------------------------------------------
#!/usr/bin/env python
# coding: utf-8

# ------------------------------------------------------------------------------
# Call required packages
# ------------------------------------------------------------------------------
import datetime
import streamlit as st
import pandas as pd
import numpy as np
from pandas.errors import ParserError

def listToDict(b):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    if b=="b":
        return {s[i]:i for i in range(len(s))}
    else:
        return {i:s[i] for i in range(len(s))}

def base64_to_base10(b64dec,datatype=None):
    conversion_table = listToDict("b")

    if datatype == "f":
        x=b64dec.split(".")[0]
        y=b64dec.split(".")[1]

        x_dec=0
        x_power = len(x)-1
        for x_digit in x:
            x_dec += conversion_table[x_digit]*64**x_power
            x_power -= 1

        y_dec,z,f=0,0,0
        y_power = len(y)-1
        for y_digit in y:
            if y_digit=="0" and f==0:
                z=z+1
            else:
                f=1
            y_dec += conversion_table[y_digit]*64**y_power
            y_power -= 1

        return str(x_dec)+"."+str("").zfill(z)+str(y_dec)
    else:
        decimal = 0
        power = len(b64dec) -1
        for digit in b64dec:
            decimal += conversion_table[digit]*64**power
            power -= 1
        return decimal

def base10_to_base64(decimal,datatype=None):
    conversion_table = listToDict("d")

    if datatype == "f":
        x=int(str(decimal).split(".")[0])
        y=str(decimal).split(".")[1].strip()
        z=len(y)-len(str(int(y)))
        y=int(y)

        x_rem=0
        x_b64dec=''
        while(x > 0):
            x_rem = x % 64
            x_b64dec = conversion_table[x_rem] + x_b64dec
            x = x // 64

        y_rem=0
        y_b64dec=''
        while(y > 0):
            y_rem = y % 64
            y_b64dec = conversion_table[y_rem] + y_b64dec
            y = y // 64
        return x_b64dec+"."+str("").zfill(z)+y_b64dec
    else:
        b64dec = ''
        remainder=0
        decimal=int(decimal)
        while(decimal > 0):
            remainder = decimal % 64
            b64dec = conversion_table[remainder] + b64dec
            decimal = decimal // 64
        return b64dec

# ------------------------------------------------------------------------------
# Built WebUI
# This function is used for testing purpose from WebUI
# ------------------------------------------------------------------------------

def s_ui():
    print("")

# ------------------------------------------------------------------------------
# Call main function.
# This main function is used for testing purpose from local system
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        print("Started - DateTime:",datetime.datetime.now())

        #print("Enter any number:")
        #s=input()
        #if s in ".":
        #    base64=base10_to_base64(s,"f")
        #    base10=base64_to_base10(base64,"f")
        #else:
        #    base64=base10_to_base64(int(s))
        #    base10=base64_to_base10(base64)

        #print("Given Value:",str(s))
        #print("Base64:",base64)
        #print("Base10:",base10)

        s_ui()
        print("End - DateTime:",datetime.datetime.now())

    except Exception as msg:
        print(f'''Error {msg}''')
