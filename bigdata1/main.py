from sys import argv
from src.bigdata1.opcvapi import call_opcv
import os

if __name__ == "__main__":
	YOUR_APP_KEY = os.getenv('APP_KEY')
	page_size = int(argv[1])
	num_pages = int(argv[2])
	output = argv[3]

	data = call_opcv(YOUR_APP_KEY, page_size, num_pages, output)
	print(data)