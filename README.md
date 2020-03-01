# BigData-Project-1
course project#1 for STA9760 Big Data

## Part 1

In part 1 work, I built a docker image on my computer and pushed it to docker hub, and ran the image in my AWS EC2 instance.

### How to use this Dockerfile
Take my command line as example:
1. Build an image from our dockerfile on your computer:

        $ docker build -t bigdata1:1.0 . 
2. Create a container and run our script. The command line supported should be:

        # On your local machine: 
        $ docker run -v $(pwd):/app -e APP_KEY=...your API token... -t local_image:tag python -m main page_size num_pages output
        # Or, in EC2 instance: 
        $ sudo docker run -e APP_KEY=...your API token... -it docker_hub_image:tag python main.py page_size num_pages output

### About the python scripts
>bigdata1/src/opcvapi.py 
Python script to intertact with the OPCV API and manage API response.

>bigdata1/main.py
Python script to get the API response based on provided API token [APP_KEY] and parameters [page_size, num_pages, output] and print results to a .json file
