from __future__ import division
import sys
from math import ceil
import requests

''' User goes here'''
user = "#user_name"

def events(user):

	base_url = 'https://api.github.com/users/{0}/events'.format(user)
	response = requests.get(base_url)
	content = response.json()

	for i in content:
		if i["type"] == "PushEvent":
			print user + " pushed to " + i["repo"]["name"]
		elif i["type"] == "CreateEvent":
			print user + " created " + i["repo"]["name"]


'''call events method'''
events(user)