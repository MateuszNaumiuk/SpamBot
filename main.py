import pyautogui as pg
import time

################################################
# Title: Simple Spam application               #
# Author: Mateusz Naumiuk 3.14.2022            #
# Date: 03.14.2022                             #
################################################

# all inputs from user
sentence = input("Write sentence: ")
how_much = int(input("How many times: "))
timeint = int(input("How many time wait to run spam: "))

# user sleep time
time.sleep(timeint)

# main loop
for i in range (how_much):
    pg.write(sentence, interval=0.03)