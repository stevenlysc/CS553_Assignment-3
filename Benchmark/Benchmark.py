#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os, sys, time
import threading
from datetime import datetime

LASTFILENUM = -1
appURL = 'http://li-hu-zhang.appspot.com'
threadLock = threading.Lock()
threads = list()

class BenchmarkThread(threading.Thread):
	"""docstring for BenchmarkThread"""
	def __init__(self, operation):
		super(BenchmarkThread, self).__init__()
		self.operation = operation.upper()
		self.results = list()

	def run(self):
		global LASTFILENUM

		# Initialization
		execTime = 0

		# Get all files from the folder
		fileList = os.listdir('testfiles/')

		try:
			# Proceed operation on every file in the folder
			while True:
				# Update LASTFILENUM
				threadLock.acquire()
				LASTFILENUM += 1
				threadLock.release()

				if LASTFILENUM == len(fileList):
					break
				# Skip the invisible files
				if fileList[LASTFILENUM][0:1] == '.':
					pass
				# Insert
				if self.operation == 'INSERT':
					execTime = self.insert(fileList[LASTFILENUM], 'testfiles/' + fileList[LASTFILENUM])
				# Find
				elif self.operation == 'FIND':
					execTime = self.find(str(fileList[LASTFILENUM]))
				# Remove
				elif self.operation == 'REMOVE':
					execTime = self.remove(fileList[LASTFILENUM])
				else:
					pass

				# Add result to the list
				self.results.append([execTime, fileList[LASTFILENUM]])
		except Exception, e:
			pass


	def insert(self, fileKey, filePath):
		start = datetime.now()
		# Get uploadURL
		uploadURL = requests.get(appURL + '/uploadurl').text
		dataFlow = {'filekey': fileKey}
		files = {'file': open(filePath, 'r')}
		insertReq = requests.post(uploadURL, data = dataFlow, files = files)
		execTime = (datetime.now() - start).total_seconds()
		# Output result
		print 'Inserting:  {}' .format(fileKey)
		return execTime

	def find(self, fileKey):
		start = datetime.now()
		dataFlow = {'filekey': fileKey}
		findReq = requests.post(appURL + '/download', data = dataFlow)
		execTime = (datetime.now() - start).total_seconds()
		# Output result
		print 'Finding:  {}' .format(fileKey)
		return execTime

	def check(self, fileKey):
		start = datetime.now()
		dataFlow = {'filekey': fileKey}
		checkReq = requests.post(appURL + '/check', data = dataFlow)
		execTime = (datetime.now() - start).total_seconds()
		# Output result
		print 'Checking:  {}' .format(fileKey)
		return execTime

	def remove(self, fileKey):
		start = datetime.now()
		dataFlow = {'filekey': fileKey}
		removeReq = requests.post(appURL + '/remove', data = dataFlow)
		execTime = (datetime.now() - start).total_seconds()
		# Output result
		print 'Removing:  {}' .format(fileKey)
		return execTime

if __name__ == '__main__':
	# Get the arguments from pipe
	if len(sys.argv) != 3:
		print 'Usage:  {}  ThreadNum  Operations' .format(sys.argv[0])
		sys.exit(0)

	# Initialization
	start = datetime.now()
	threadNum = int(sys.argv[1])
	operation = sys.argv[2]

	# Running threads
	for tid in xrange(threadNum):
		myThread = BenchmarkThread(operation)
		myThread.start()
		threads.append(myThread)
	for thread in threads:
		thread.join()

	# Gather all the results
	allResults = list()
	for thread in threads:
		allResults += thread.results

	# Total running time
	execTime = (datetime.now() - start).total_seconds()
	print 'Elapsed: {} s.' .format(execTime)
	# Output result
	fstream = open(operation + '_thread_' + str(threadNum), 'w')
	fstream.write('With {} thread/threads, doing {}, the total time is {} seconds  ------------  All Operations.\n' .format(threadNum, operation, execTime))
	for result in allResults:
		sigleExecTime = result[0]
		fileName = result[1]
		fstream.write('\t{}\tRunning time:  {} seconds  ------------  Single Operation.\n' .format(fileName, sigleExecTime))
	fstream.flush()
	fstream.close()
	# Sleep for consistency
	time.sleep(60)