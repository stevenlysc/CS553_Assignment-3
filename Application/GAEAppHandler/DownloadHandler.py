#! /usr/bin/python
# -*- coding: utf-8 -*-


from FileKey import FileKey, fileKeyList
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore
from google.appengine.api import memcache
from google.appengine.api import files
from google.appengine.ext import db

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
	
	# We don't want to override __init__()

	# Download file is a 'Post' function
	def post(self):
		# Bucket name
		BUCKETPATH = '/gs/hxt-001'
		# Get keyboard input from web page
		keyInput = self.request.get('filekey')
		if keyInput == '':
			self.response.out.write("File Key cannot be empty.")
			return None
		# Return a query object that represents all entities
		fileKeys = FileKey.all()

		# Get the key by using the given keyInput
		fileKeys.filter('__key__ =', db.Key.from_path('FileKey', keyInput, parent = fileKeyList()))

		# Write file onto web page
		if fileKeys.count == 0:
			self.response.out.write('Key: {}, does not exist.' .format(keyInput))
		else:
			for fileKey in fileKeys:
				# File stored in Memcache
				if fileKey.fileLocation == 'memcache':
					blobInfo = memcache.get(fileKey.key().id_or_name())
					self.send_blob(blobInfo,save_as = True)
					self.response.out.write('<br />From Memcache: ' + str(fileKey.key().id_or_name()))
				# File stored in Google Cloud Storage
				else:
					with files.open(BUCKETPATH + '/' + fileKey.key().id_or_name(), 'r') as fstream:
						buf = fstream.read(1000000)
						limitCount = 1000000
						while buf:
							self.response.out.write(buf)
							buf = fstream.read(1000000)
							limitCount += 1000000
							if limitCount < 25000000:
								break
					self.response.out.write('<br />From Google Cloud Storage: ' + str(fileKey.key().id_or_name()))


if __name__ == '__main__':
	pass
