#! /usr/bin/python
# -*- coding: utf-8 -*-

from FileKey import FileKey, fileKeyList
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import memcache
from google.appengine.api import files
from google.appengine.ext import db

# Bucket name
BUCKETPATH = '/gs/hxt-001'

class FindInFileHandler(blobstore_handlers.BlobstoreDownloadHandler):
	
	# We don't want to override __init__()

	# Find files is a 'Post' function
	def post(self):

		# Get the keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None
		reStr = self.request.get('regexp')

		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Find all files with the given keyInput
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Find the contents and output the result onto web page
		if fileKeys.count() == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			for fileKey in fileKeys:
				self.response.out.write('Matching contents <br />')
				
				# File stored in Memcache
				if fileKey.fileLocation == 'memcache':
					blobInfo = memcache.get(fileKey.key().id_or_name())
					# write content to web page
					blobReader = blobInfo.open()
					for line in blobReader:
						if reStr in line:
							self.response.out.write(line)

				# File stored in Google Cloud Storage
				else:
					with files.open(BUCKETPATH + '/' + fileKey.key().id_or_name(), 'r') as fstream:
						buf = fstream.read(1000)
						while buf:
							if reStr in buf:
								self.response.out.write(buf)
							buf = fstream.read(1000000)


if __name__ == '__main__':
	pass
