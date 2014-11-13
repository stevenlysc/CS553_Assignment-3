#! /usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext import blobstore

class MainHandler(webapp2.RequestHandler):
	
	# We don't want to override __inti__()
	
	
	def get(self):
		
		# Upload URL
		uploadURL = blobstore.create_upload_url('/upload')
		
		'''
		Import HTML
		'''
		self.response.out.write('''
			<!DOCTYPE html>
			<html>
			<head>
			<meta charset="UTF-8">
			<title>Assignment 3</title>
			<style>
				body {background-color:rgb(250, 255, 240)}
				h2	 {color:rgb(102, 51, 255)}
				h4	 {color:rgb(153, 102, 102)}
			</style>
			</head>
			<body>
				<!--Standard Credit Part-->
				<div>
					<h2>Operation</h2>
					<br />
					<hr>
				</div>
				<div>
					<h4>Insert/Upload File</h4>
					<form action="%s" method="POST" enctype="multipart/form-data">File Key: 
						<input type="text" name="filekey">UploadFile: 
						<input type="file" name="file" multiple>
						<input type="submit" name="submit" value="Submit"> 
			     		</form>
				</div>
				<div>
					<h4>Check</h4>
					<form action="/check" method="post">
						<table>
							<tr>
								<td>File Key:</td>
								<td><input type="text" name="filekey"></td>
								<td><input type="submit" value="Check"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Remove/Delete</h4>
					<form action="/remove" method="post">
						<table>
							<tr>
								<td>File Key:</td>
								<td><input type="text" name="filekey"></td>
								<td><input type="submit" value="Remove"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Find/Download</h4>
					<form action="/download" method="post">
						<table>
							<tr>
								<td>File Key: </td>
								<td>
									<input type="text" name="filekey">
								</td>
								<td>
									<input type = "submit" value="Download">
								</td>
							</tr>
						</table>
					</form>
				</div>
				<div>
					<h4>List Files</h4>
					<form action="/list" method="get">
						<table>
							<tr>
								<td>List All Files: </td>
								<td><input type="submit" value="List"></td>
							</tr>
						</table>
					</form>
				</div>

				<!--Extra Credit Part-->
				<div>
					<br />
					<h2>Extra Credit</h2>
					<br />
					<hr>
				</div>		
				<div>
					<h4>Check in Storage</h4>
					<form action="/checkcloudstorage" method="post">
						<table>
							<tr>
								<td>File Key:</td>
								<td><input type="text" name="filekey"></td>
								<td><input type="submit" value="Check"></td>
							</tr>
						</table>
					</form>
				</div>
				<div>
					<h4>Check in Cache</h4>
					<form action="/checkcache" method="post">
						<table>
							<tr>
								<td>File Key:</td>
								<td><input type="text" name="filekey"></td>
								<td><input type="submit" value="Check"></td>
							</tr>
						</table>
					</form>
				</div>
				<div>
					<h4>Remove All Cache</h4>
					<form action="/removeallcache" method="post">
						<table>
							<tr>
								<td>Click the button, and remove all cache</td>
								<td><input type="submit" value="Remove"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Remove All</h4>
					<form action="/removeall" method="post">
						<table>
							<tr>
								<td>Click the button, and remove all</td>
								<td><input type="submit" value="Remove"></td>
							</tr>
						</table>
					</form>
				</div>
				<div>
					<h4>Cache Size Element</h4>
					<form action="/cachesizeelem" method="post">
						<table>
							<tr>
								<td>Click the button, and retrieve elements</td>
								<td><input type="submit" value="Retrieve"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Storage Size Element</h4>
					<form action="/storagesizeelem" method="post">
						<table>
							<tr>
								<td>Click the button, and retrieve elements</td>
								<td><input type="submit" value="Retrieve"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Find in File</h4>
					<form action="/findinfile" method="post">
						<table>
							<tr>
								<td>File Key:</td>
								<td><input type="text" name="filekey"></td>
							</tr>
							<tr>
								<td>Expression:</td>
								<td><input type="text" name="regexp"></td>
								<td><input type="submit" value="Find"></td>
							</tr>
						</table>
					</form>
				</div>	
				<div>
					<h4>Listing</h4>
					<form action="/listing" method="post">
						<table>
							<tr>
								<td>Expression:</td>
								<td><input type="text" name="regexp"></td>
								<td><input type="submit" value="List"></td>
							</tr>
						</table>
					</form>
					<br />
				</div>
			</body>
			</html>''' % uploadURL)

if __name__ == '__main__':
	pass
