import os
import re
import time
import psutil
from wxpy import *

def flow():
	return psutil.disk_io_counters()[3]

bot = Bot(cache_path=True)
count = 0
while True:
	fir = flow()
	time.sleep(1)
	last = flow()
	num = round((last-fir)/1024**2, 2)
	time.sleep(1)
	if num <0.3:
		count +=1
		if count >10:
			try:
				print(num)
				my_friend = bot.friends().search('I am 乔。')[0]
				my_friend.send('监控网络好像挂了，快来看看吧。')
				count = 0
				time.sleep(3600)
			except Exception as e:
				time.sleep(60)
				continue	
	else:
		count = 0
	time.sleep(10)
bot.join() 

