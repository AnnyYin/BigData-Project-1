from sodapy import Socrata
from requests import get
import json
import pprint

def call_opcv(YOUR_APP_KEY, page_size, num_pages, output):
	client = Socrata("data.cityofnewyork.us", YOUR_APP_KEY)
	count_rows = int(client.get("nc67-uf89", select='COUNT(*)')[0]['COUNT'])
	if not num_pages:
		num_pages = count_rows // page_size + 1
	if output:
		results = open(output, 'w')
	for i in range(num_pages):
		page = client.get("nc67-uf89", limit = page_size, offset = i*page_size)
		if output:
			results.write(json.dumps(page) + '\n')
		else:
			pprint.pprint(page)
	if output:
		print(results)