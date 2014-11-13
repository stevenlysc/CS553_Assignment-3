#! /usr/bin/python
# -*- coding: utf-8 -*-

from google.appengine.ext import db

class FileKey(db.Model):
	'''
	The keys of files in memcache and cloud stroage
	'''
	# We don't override __init__(), just use db.Model.__init__()

	# blobInfoKey
	blobInfoKey = db.StringProperty()

	# location of the file: memcache or cloud storage
	fileLocation = db.StringProperty()

def fileKeyList():
    return db.Key.from_path('Filelist', 'default_filelist')


if __name__ == '__main__':
	pass
