# Containerized Link Extractor Script

Checkout the `step1` branch and list files in it.

```bash
git checkout step1
tree
```

```
.
├── Dockerfile
├── README.md
└── linkextractor.py

0 directories, 3 files
```

We have added one new file (i.e., `Dockerfile`) in this step.
Let's look into its contents:

```bash
cat Dockerfile
```

```dockerfile
FROM python:3
LABEL maintainer="Sawood Alam <@ibnesayeed>"

RUN pip install beautifulsoup4
RUN pip install requests

WORKDIR /app
COPY linkextractor.py /app/
RUN chmod a+x linkextractor.py

ENTRYPOINT ["./linkextractor.py"]
```

Using this `Dockerfile` we can prepare a Docker image for this script.
We start from the official `python` Docker image that contains Python's run-time environment as well as necessary tools to install Python packages and dependencies.
We then add some metadata as labels (this step is not essential, but is a good practice nonetheless).
Next two instructions run the `pip install` command to install the two third-party packages needed for the script to function properly.
We then create a working directory `/app`, copy the `linkextractor.py` file in it, and change its permissions to make it an executable script.
Finally, we set the script as the entrypoint for the image.

So far, we have just described how we want our Docker image to be like, but didn't really build one.
So let's do just that:

```bash
docker image build -t linkextractor:step1 .
```

This command should yield an output as illustrated below:

```
Sending build context to Docker daemon  171.5kB
Step 1/8 : FROM       python:3

... [OUTPUT REDACTED] ...

Successfully built 226196ada9ab
Successfully tagged linkextractor:step1
```

We have created a Docker image named `linkextractor:step1` based on the `Dockerfile` illustrated above.
If the build was successful, we should be able to see it in the list of image:

```bash
docker image ls
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
linkextractor       step1               e067c677be37        2 seconds ago       931MB
python              3                   a9d071760c82        2 weeks ago         923MB
```

This image should have all the necessary ingredients packaged in it to run the script anywhere on a machine that supports Docker.
Now, let's run a one-off container with this image and extract links from some live web pages:

```bash
docker container run -it --rm linkextractor:step1 http://example.com/
```

This outputs a single link that is present in the simple [example.com](http://example.com/) web page:

```
http://www.iana.org/domains/example
```

Let's try it on a web page with more links in it:

```bash
docker container run -it --rm linkextractor:step1 https://training.play-with-docker.com/
```

```
/
/about/
#ops
#dev
/ops-stage1
/ops-stage2
/ops-stage3
/dev-stage1
/dev-stage2
/dev-stage3
/alacart
https://twitter.com/intent/tweet?text=Play with Docker Classroom&url=https://training.play-with-docker.com/&via=docker&related=docker
https://facebook.com/sharer.php?u=https://training.play-with-docker.com/
https://plus.google.com/share?url=https://training.play-with-docker.com/
http://www.linkedin.com/shareArticle?mini=true&url=https://training.play-with-docker.com/&title=Play%20with%20Docker%20Classroom&source=https://training.play-with-docker.com
https://2018.dockercon.com/
https://2018.dockercon.com/
https://success.docker.com/training/
https://community.docker.com/registrations/groups/4316
https://docker.com
https://www.docker.com
https://www.facebook.com/docker.run
https://twitter.com/docker
https://www.github.com/play-with-docker/play-with-docker.github.io
```

This looks good, but we can improve the output.
For example, some links are relative, we can convert them into full URLs and also provide the anchor text they are linked to.
In the next step we will make these changes and some other improvements to the script.
