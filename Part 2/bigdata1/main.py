from sys import argv
from src.bigdata1.opcvapi import call_opcv
import os
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--page_size', type = int)
	parser.add_argument('--num_pages', default = None, type = int)
	parser.add_argument('--output', default = None)
	parser.add_argument('--push_es', default=False, type=bool)
	args = parser.parse_args()

	YOUR_APP_KEY = os.getenv('APP_KEY')
	call_opcv(YOUR_APP_KEY, args.page_size, args.num_pages, args.output, args.push_es)