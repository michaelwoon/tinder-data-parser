#fb-info-parser
# -*- coding: utf-8 -*-
import json
from datetime import datetime
from collections import Counter
import sys
import matplotlib.pyplot as plt
import numpy as np

#open json file
with open('tinderdata.json', 'r') as f:
    data = json.load(f)

#for app_opens, swipes_likes, swipes_passes, messages_sent, messages_received
def usage(category):
    sum = 0
    for day in data['Usage'][category]:
        sum += data['Usage'][category][day]
    return sum

print(usage('swipes_likes'))
print(usage('messages_sent'))
print(usage('messages_received'))

#TODO messages section
