import os
import time
from probability import shouldKill
from aws import killInstance
from welcome import welcome

try:
	LOOP_TIME = int(os.getenv('LOOP_TIME'))
	if not LOOP_TIME:
		print "LOOP_TIME not defined default to 600s"
		LOOP_TIME = 600
	if LOOP_TIME < 15:
		print "LOOP_TIME must be at least 60s (will default to 15)"
except Exception as e:
	print e

welcome()
print "Warming up..."
time.sleep(15)

while True:
	print "George is searching for instances..."
	if shouldKill():
		killInstance()
	else:
		print "George didn't touch anything this time..."
	print "George is tired and will sleep for " + str(LOOP_TIME) + " seconds..."
	time.sleep(LOOP_TIME)







