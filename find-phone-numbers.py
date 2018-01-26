import re
import glob
import os

path = os.path.abspath('*.txt')

Files = glob.glob(path)

phoneNumber_regex = re.compile(r'\+*[\d{2}]*\-*\d{10}')

for file in Files:
	with open(file) as f:
		extracted_numbers = phoneNumber_regex.findall(f.read())
		print(extracted_numbers)