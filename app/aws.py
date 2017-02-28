import boto3
import os
import random
from pprint import pprint

try:
	REGION = os.getenv('REGION')
	if not REGION:
		print "MissingEnv - REGION"
	TAG = os.getenv('TAG')
	if not TAG:
		print "MissingEnv - TAG"
except Exception as e:
	print e
try:
	ec2 = boto3.client(
		'ec2',
		region_name=REGION
	)
except Exception as e:
	print e
	quit()


def pickRandomInstance():
	inst = []
	if not REGION or not TAG:
		return False
	try:
		response = ec2.describe_instances(
			Filters=[
		        {
		            'Name': 'tag-value',
		            'Values': [
		                TAG
		            ]
		        }
	    	]
	    )
	except Exception as e:
		print e 
		return False
	try:
		for i in range(len(response['Reservations'])):
			try:
				for j in range(len(response['Reservations'][i]['Instances'])):
					inst.insert(len(inst), response['Reservations'][i]['Instances'][j]['InstanceId'])
					#print response['Reservations'][i]['Instances'][j]['InstanceId']
			except Exception as e:
				print e
				return False
		if len(inst) > 0:
			return inst[random.randrange(len(inst) -1)]
		else:
			print "No instances matching tags found"
			return False
	except Exception as e:
		print e
		return False


def killInstance():
	id = pickRandomInstance()
	if id:
		print "George found an instance..."
		try:
			response = ec2.terminate_instances(
			    DryRun=False,
			    InstanceIds=[
			        id,
			    ]
			)
			print 'George accidentally killed an instance with id ' + id
		except Exception as e:
			print e

