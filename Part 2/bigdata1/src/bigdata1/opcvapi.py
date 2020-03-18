from sodapy import Socrata
from requests import get
import json
import pprint
from src.bigdata1.es import create_index, push_record

def call_opcv(YOUR_APP_KEY, page_size, num_pages, output, push_es):
	client = Socrata("data.cityofnewyork.us", YOUR_APP_KEY)
	count_rows = int(client.get("nc67-uf89", select='COUNT(*)')[0]['COUNT'])
	if not num_pages:
		num_pages = count_rows // page_size + 1
	if output:
		results = open(output, 'w')
	if push_es:
		es = create_index('opcv')
	for i in range(num_pages):
		page = client.get("nc67-uf89", limit = page_size, offset = i*page_size)
		if output:
			results.write(json.dumps(page) + '\n')
		else:
			pprint.pprint(page)
		if push_es:
			for record in page:
				push_record(record, es, 'opcv')
	if output:
		print(results)