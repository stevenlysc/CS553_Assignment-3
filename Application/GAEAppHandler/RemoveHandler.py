#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from FileKey import FileKey, fileKeyList
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import files

# Bucket name
BUCKETPATH = '/gs/hxt-001'

# Remove all files in both Memcache and Google Cloud Storage
class RemoveAllHandler(webapp2.RequestHandler):

	# We don't want to override __init__()

	# Remove all files is a 'Post' funtion
	def post(self):
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		self.response.out.write('<b>Removed All:</b>')

		# Delete and output onto the web page
		for fileKey in fileKeys:
			self.response.out.write('<br />' + str(fileKey.key().id_or_name()))
			
			# Delete keys in Memcache
			if fileKey.fileLocation == 'memcache':
				memcache.delete(fileKey.key().id_or_name())
			# Delete keys in Google Cloud Storage
			else:
				files.delete(BUCKETPATH + '/' + str(fileKey.key().id_or_name()))

		# Delete keys
		for fileKey in fileKeys:
			db.delete(fileKey.key())

# Remove all files in Memcache
class RemoveAllCacheHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Remove all files in Memcache is a 'Post' function
	def post(self):
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()
		self.response.out.write('<b>Removed All Cache:</b>')
		# Find all keys in Memcache
		fileKeys.filter('fileLocation =', 'memcache')

#self.response.out.write(fileKeys.key().id_or_name())

		# Delete and ouput onto the web page
		for fileKey in fileKeys:
			self.response.out.write('<br />' + str(fileKey.key().id_or_name()))
			memcache.delete(fileKey.key().id_or_name())

		# Delete keys
		for fileKey in fileKeys:
			db.delete(fileKey.key())

# Remove a certain file with a given key
class RemoveHandler(webapp2.RequestHandler):

	# We don't want to override __init__()

	# Remove a file is a 'Post' function
	def post(self):

		# Get keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None

		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Find the given key
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Delete the file and output onto web page
		if fileKeys.count() == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			fk = db.get(db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

			# File stored in Memcache
			if fk.fileLocation == 'memcache':
				memcache.delete(fk.key().id_or_name())
				self.response.out.write('Deleted from Memcache')
			else:
				files.delete(BUCKETPATH + '/' + str(fk.key().id_or_name()))
				self.response.out.write('Deleted from Google Cloud Storage')
			db.delete(db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))
			self.response.out.write('<br />Key: {} removed.' .format(keyInput))


if __name__ == '__main__':
	pass
