from __future__ import division
from random import random
import os

try:
	PROBABILITY = int(os.getenv('PROBABILITY'))
	if not PROBABILITY:
		print "PROBABILITY not defined"
		PROBABILITY = False
except Exception as e:
	if not PROBABILITY:
		print "PROBABILITY not defined"
	print e

def shouldKill():
	if PROBABILITY and PROBABILITY <= 100:
		return random() < PROBABILITY/100
	else:
		print "Probability not defined or invalid"