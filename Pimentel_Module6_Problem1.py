### Module 6: Time (Problem 1) ###

import sys
import time
from datetime import datetime
from datetime import timedelta

# 1.  Try the code below and revise it to current time. 
#import sys
current_time = datetime.now()

for line in sys.stdin:
   data = line.strip().split("\t")
   if len(data) == 5:
      data, store, item, cost, payment = data
      print(f"I bought a(n) {item} for {cost} on {current_time}")
      break
