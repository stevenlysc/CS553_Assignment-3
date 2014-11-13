#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from FileKey import FileKey, fileKeyList
from google.appengine.ext import db

# Check both Memcache and Google Cloud Storage
class CheckHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Check whether a certain key exists or not is a 'Post' function
	def post(self):
		
		# Get keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Find keyInput with all the keys in the Datastore
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Output the result onto the web page
		if fileKeys.count() == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			self.response.out.write('Key: {}, exists.' .format(keyInput))

# Only check Memcache
class CheckCacheHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Check whether a certain key exits in Memcache or not is a 'Post' function
	def post(self):
		
		# Get keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None

		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Find keyInput within all the keys in the Datastore
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Find all results stored in Memcache
		fileKeys.filter('fileLocation = ', 'memcache')

		# Output the result onto the web page
		if fileKeys.count() == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			self.response.out.write('Key: {}, exists.' .format(keyInput))

# Only Check Google Cloud Storage
class CheckCloudStorageHandler(webapp2.RequestHandler):

	# We don't want to override __init__()

	# Check whether a certain key exits in Google Cloud Storage or not is a 'Post' function
	def post(self):
		
		# Get keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None

		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Find keyInput within all the keys in the Datastore
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Find all results stored in Google Cloud Storage
		fileKeys.filter('fileLocation = ', 'cloudStorage')

		# Output the result onto the web page
		if fileKeys.count() == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			self.response.out.write('Key: {}, exists.' .format(keyInput))


if __name__ == '__main__':
	pass
