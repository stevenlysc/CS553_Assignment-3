#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from FileKey import FileKey

# Retrieve all the keys
class ListHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Retrive all file keys as a list is a 'Get' function
	def get(self):
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Output the file
		self.response.out.write('<b>List: </b>' + str(fileKeys.count()))
		for fileKey in fileKeys:
			self.response.out.write('<br />' + fileKey.key().id_or_name())

# Retrieve all the keys contains a given input
class ListingHandler(webapp2.RequestHandler):
	
	# We don't want to override __init__()

	# Retrive all file keys as a list is a 'Post' function
	def post(self):
		
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Get the keyboard input from web page
		reStr = self.request.get('regexp')
		if reStr == '':
			self.response.out.write("Expression cannot be empty.")
			return None

		self.response.out.write('<b>List with {}: </b>' .format(reStr))

		# Find all keys and output the result onto the web page
		for fileKey in fileKeys:
			if reStr in fileKey.key().id_or_name():
				self.response.out.write('<br />' + str(fileKey.key().id_or_name()))

if __name__ == '__main__':
	pass
