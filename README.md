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
>bigdata1/src/opcvapi.py

Python script to intertact with the OPCV API and manage API response.

>bigdata1/main.py

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
        
        ubuntu@ip-172-31-30-59:~$ sudo docker run -e APP_KEY=...your_api_token -it annyy/bigdata1:1.0 python main.py --page_size=1000 --num_page=4 --output=results.json
        <_io.TextIOWrapper name='results.json' mode='w' encoding='UTF-8'>

***

## Part 2
_TBC_
