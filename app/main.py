import os
import time
from probability import shouldKill
from aws import killInstance
from welcome import welcome

try:
	TIMEOUT = int(os.getenv('TIMEOUT'))
	if not TIMEOUT:
		print "TIMEOUT not defined default to 600s"
		TIMEOUT = 600
	if TIMEOUT < 15:
		print "TIMEOUT must be at least 60s (will default to 15)"
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
	print "George is tired and will sleep for " + str(TIMEOUT) + " seconds..."
	time.sleep(TIMEOUT)







