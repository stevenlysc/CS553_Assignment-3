#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
import os
import urllib

from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import memcache
from google.appengine.api import files
from GAEAppHandler import *


try:
    files.gs
except AttributeError:
    import gs
    files.gs = gs

app = webapp2.WSGIApplication([('/', MainHandler),
                                   ('/upload', UploadHandler),
                                   ('/uploadurl', UploadURLHandler),
                                   ('/list', ListHandler),
                                   ('/check', CheckHandler),
                                   ('/download', DownloadHandler),
                                   ('/remove', RemoveHandler),
                                   ('/checkcache', CheckCacheHandler),
                                   ('/removeallcache', RemoveAllCacheHandler),
                                   ('/removeall', RemoveAllHandler),
                                   ('/cachesizeelem', CacheSizeElemHandler),
                                   ('/storagesizeelem', StorageSizeElemHandler),
                                   ('/findinfile', FindInFileHandler),
                                   ('/listing', ListingHandler),
                                   ('/checkcloudstorage', CheckCloudStorageHandler)],
                                debug = True)
