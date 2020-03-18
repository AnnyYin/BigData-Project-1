from datetime import datetime, date
from elasticsearch import Elasticsearch

def create_index(index_name):
	es = Elasticsearch()
	try:
		es.indices.create(index = index_name)
	except:
		pass
	return es

def push_record(record, es, index_name):
	for key, value in record.items():
		if '_amount' in key:
			record[key] = float(value)
		elif '_date' in key:
			try:
				record[key] = datetime.strptime(value,'%m/%d/%Y').date()
			except:
				try:
					date = [int(i) for i in record[key].split('/')]
					if date[0]==2 and date[1]==29 and date[2]%4==0:
						date[0]=3
						date[1]=1
						record[key] = datetime.date(date[2], date[0], date[1])
				except:
					pass
	es.index(index=index_name, id=record['summons_number'], body=record)
