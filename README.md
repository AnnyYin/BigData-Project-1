# BigData-Project-1
course project#1 for STA9760 Big Data

## Part 1

In part 1 work, I built a docker image on my computer and pushed it to docker hub, and ran the image in my AWS EC2 instance.

### How to use this Dockerfile
1. Build an image from our dockerfile on your computer:

        $ docker build -t bigdata1:1.0 . 
2. Create a container and run our script. The command line supported should be:

        # On your local machine
        $ docker run -v $(pwd):/app -e APP_KEY=...your API token... -t bigdata1:1.0 python -m main page_size num_pages output
3. Deploying via Docker Hub:

        $ docker push your_username/bigdata1
4. Try to pull this image from dockerhub and run in your AWS EC2 instance:

        ~$ sudo docker pull bigdata1:1.0
        ~$ sudo docker run -it annyy/bigdata1:1.0 /bin/bash
        ~$ sudo docker run -e APP_KEY=...your API token... -it bigdata1:1.0 python main.py page_size num_pages output

### About the python scripts
>bigdata1/src/opcvapi.py

Python script to intertact with the OPCV API and manage API response.

>bigdata1/main.py

Python script to get the API response based on provided API token [APP_KEY] and parameters [page_size, num_pages, output] and print results to a .json file.

### Output example running in AWS EC2

        ubuntu@ip-172-31-30-59:~$ sudo docker pull annyy/bigdata1:1.0
        1.0: Pulling from annyy/bigdata1
        ......
        Status: Downloaded newer image for annyy/bigdata1:1.0

        ubuntu@ip-172-31-30-59:~$ sudo docker run -it annyy/bigdata1:1.0 /bin/bash
        root@e53966c1a7a2:/app# ls -ahl
        total 32K
        drwxr-xr-x 1 root root 4.0K Mar  1 10:20 .
        drwxr-xr-x 1 root root 4.0K Mar  1 10:24 ..
        -rw-r--r-- 1 root root 6.1K Mar  1 10:15 .DS_Store
        -rw-r--r-- 1 root root   76 Feb 28 21:39 dockerfile
        -rw-r--r-- 1 root root  284 Feb 29 04:37 main.py
        -rw-r--r-- 1 root root  106 Feb 28 21:39 requirements.txt
        drwxr-xr-x 3 root root 4.0K Mar  1 10:15 src
        
        ubuntu@ip-172-31-30-59:~$ sudo docker run -e APP_KEY=...your_api_token... -it annyy/bigdata1:1.0 python main.py 1000 4 results.json
        <_io.TextIOWrapper name='results.json' mode='w' encoding='UTF-8'>
        # the results.json file should be in the root folder

***
