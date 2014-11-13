#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from FileKey import FileKey

class CacheSizeElemHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Retrieve the number of files in Memcache is a 'Post' function
	def post(self):
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Get all keys stored in Memcache and output onto web page
		fileKeys.filter('fileLocation =', 'memcache')
		self.response.out.write('<b>Number of files in Memcache: </b>')
		self.response.out.write(fileKeys.count())

class StorageSizeElemHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Retrieve the number of files in Google Cloud Storage is a 'Post' function
	def post(self):
		
		# Return a query objct that represents all entities
		fileKeys = FileKey.all()

		# Get all keys stored in Google Cloud Storage and output onto web page
		fileKeys.filter('fileLocation =', 'cloudStorage')
		self.response.out.write('<b>Number of files in Google Cloud Storage: </b>')
		self.response.out.write(fileKeys.count())


if __name__ == '__main__':
	pass
