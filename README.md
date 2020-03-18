# BigData-Project#1
course project#1 for STA9760 Big Data
* For this project, we will leverage a python client of the Socrata API to connect to the Open Parking and Camera Violations (OPCV) API, load all the data into an ElasticSearch instance, and visualize / analyze with Kibana.


## Part 1 Python Scripting
In part 1 work, we are developing python scripts that can connect to OPCV API and are able to run within docker, with parameters specified by user through the command line, and give users the option to print results out to a file.

### How to use this Dockerfile
1. Build an image from our dockerfile on your computer:

        $ docker build -t bigdata1:1.0 . 
2. Create a container and run our script locally. The command line supported should be:

        $ docker run -v $(pwd):/app -e APP_KEY=...your_API_token... -t bigdata1:1.0 python main.py --page_size=1000 --num_page=4 --output=results.json
        
        #--page_size: This command line argument is required. It will ask for how many records to request from the API per call.
        #--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
        #--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).

3. Deploying via Docker Hub:

        $ docker push your_username/bigdata1
4. Try to pull this image from dockerhub and run in your AWS EC2 instance:

        ~$ sudo docker pull bigdata1:1.0
        ~$ sudo docker run -it annyy/bigdata1:1.0 /bin/bash
        ~$ sudo docker run -e APP_KEY=...your_API_token... -it annyy/bigdata1:1.0 python main.py --page_size=1000 --num_page=4 --output=results.json

### About the python scripts
> Part 1/src/opcvapi.py

Python script to intertact with the OPCV API and manage API response.

> Part 1/main.py

Python script to get the API response based on provided API token [APP_KEY] and parameters [page_size, num_pages, output].

### Output example running in AWS EC2

        ubuntu@ip-172-31-30-59:~$ sudo docker pull annyy/bigdata1:1.0
        1.0: Pulling from annyy/bigdata1
        dc65f448a2e2: Already exists 
        346ffb2b67d7: Already exists 
        dea4ecac934f: Already exists 
        8ac92ddf84b3: Already exists 
        a3ca60abc08a: Already exists 
        9253bd2ee3f6: Already exists 
        27f3323f0a58: Already exists 
        ea74ff1569e8: Already exists 
        6df39ee1cdde: Already exists 
        c6e91fb72e51: Already exists 
        bfba8d413007: Pull complete 
        4f6111906126: Pull complete 
        Digest: sha256:34f3051fae61b86d523f238add7c20ec566ffaf235ae1936c4416f528b0f0679
        Status: Downloaded newer image for annyy/bigdata1:1.0
        
        ubuntu@ip-172-31-30-59:~$ sudo docker run -e APP_KEY=...your_api_token... -it annyy/bigdata1:1.0 python main.py --page_size=1000 --num_page=4 --output=results.json
        <_io.TextIOWrapper name='results.json' mode='w' encoding='UTF-8'>

***

## Part 2 Loading into Elasticsearch
In part 2, we'll leverage docker-compose to bring up a service that encapsulates the 'bigdata1' container and an elasticsearch container and ensures that they are able to interact; Also we'll update the python scripts in part 1, to make it able to load data into elasticsearch instance.

### Leverage the docker-compose
>Part 2/docker-compose.yml

The docker-compose file with pyth, elasticsearch/kibana services allowes us to run several containers at the same time and interact between containers.

### Update to python scripts
> Part 2/requirements.txt

Add elasticsearch

> Part 2/main.py

Add a push_es argument to enable user to choose whether to push dateset to the elasticsearch service:

        parser.add_argument('--push_es', default=False, type=bool)

> Part 2/src/bigdata1/es.py

Script to define functions that create index in elasticsearch instance, and function to format and push record to instance:

        # Formatting results of calling opcv api
        if '_amount' in key:
                record[key] = float(value)
        # Formatting the date 
        elif '_date' in key:
		try:
		        record[key] = datetime.strptime(value,'%m/%d/%Y').date()
		except:
                        # to exclude error resulting from leap year
			try:
				date = [int(i) for i in record[key].split('/')]
				if date[0]==2 and date[1]==29 and date[2]%4==0:
					date[0]=3
					date[1]=1
					record[key] = datetime.date(date[2], date[0], date[1])
			except:
				pass

> Part 2/src/bigdata1/opcvapi.py

Add the option of push_es to original script, using function defined in es.py to interact with dataset from opcv api:

        # create index in instance
        if push_es:
		es = create_index('opcv')
        # push record to instance
        if push_es:
		for record in page:
			push_record(record, es, 'opcv')
                     
### How to use
1. Build docker-compose:

        $ docker-compose build pyth
2. Launch the entire service:

        $ docker-compose up -d
3. Run our script locally. The command line supported should be:

        $ docker-compose run -e APP_KEY=...your_API_token... -v ${PWD}:/app pyth python -m main --page_size=1000 --num_pages=10 --output=results.json --push_es=True 
        # --push_es=True: set the push_es argument to true means to push dataset from api to elasticsearch instance
4. Query elasticsearch

        $ curl -o output.txt http://localhost:9200/opcv/_search?q=state:NY&size=5
        
        # return 5 records where state is NY
        # querying result will be ouput to the file output.txt (my output file is located in Part 2)


***

## Part 3
