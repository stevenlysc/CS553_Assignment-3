#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from FileKey import FileKey, fileKeyList
from google.appengine.ext import blobstore
from google.appengine.api import memcache
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import files

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	
	# We don't want to override __init__()

	# Upload is a post function in HTTP
	def post(self):

		# Small file size <= 100KB
		# Big file size > 100KB
		BIGFILEBASE = 100 * 1024

		# Bucket name
		BUCKETPATH = '/gs/hxt-001'

		# 'file' is the file upload field in the form
		uploadFiles = self.get_uploads('file')

		for blobInfo in uploadFiles:
			# Store the key of file and blobInfoKey into the Datastore
			mykey = self.request.get('filekey')
			if mykey == '':
				mykey = blobInfo.filename
			filekey = FileKey(key_name = mykey, parent = fileKeyList())

			# Output the key of the file onto the web page
			self.response.out.write('File key: ')
			self.response.out.write(filekey.key().id_or_name())

			# Get the blobInfoKey of the file
			filekey.blobInfoKey = str(blobInfo.key())

			# Output the blob information onto the web page
			self.response.out.write('<br />Blob Info Key: ')
			self.response.out.write(blobInfo.key())
			self.response.out.write('<br />Blob Info Size: ')
			self.response.out.write(blobInfo.size)

			# Save file into memcache if the size is less than 100KB
			if blobInfo.size <= BIGFILEBASE:
				memcache.add(mykey, blobInfo)
				filekey.fileLocation = 'memcache'
				self.response.out.write('<br />File Saved to Memcache Successfully!')
				self.response.out.write('<br /><div></div>')
			# Save file into cloud storage if the size is large than 100KB
			else:
				writePath = files.gs.create(BUCKETPATH + '/' + filekey.key().id_or_name(), mime_type = 'text/plain', acl = 'public-read')
				with files.open(writePath, 'a') as fstream:
					fstart, fsize = 0, blobInfo.size
					fetchSize = blobstore.MAX_BLOB_FETCH_SIZE - 1
					while fstart < fsize:
						fstream.write(blobstore.fetch_data(blobInfo, fstart, fstart + fetchSize))
						fstart += fetchSize

				# Finalize the file to make the file readable in the Google Cloud Storage
				files.finalize(writePath)
				filekey.fileLocation = 'cloudStorage'
				self.response.out.write('<br />File Saved to Google Cloud Storage Successfully!')
				self.response.out.write('<br /><div></div>')

			# Store the file instance in the Datastore
			filekey.put()
			
class UploadURLHandler(webapp2.RequestHandler):
	def get(self):
		uploadURL = blobstore.create_upload_url('/upload')
		self.response.out.write(uploadURL)

if __name__ == '__main__':
	pass
