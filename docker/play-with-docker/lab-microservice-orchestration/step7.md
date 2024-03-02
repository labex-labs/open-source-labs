# Redis Service for Caching

Checkout the `step5` branch and list files in it.

```bash
git checkout step5
tree
```

```
.
├── README.md
├── api
│   ├── Dockerfile
│   ├── linkextractor.py
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
└── www
    ├── Dockerfile
    └── index.php

2 directories, 8 files
```

Some noticeable changes from the previous step are as following:

- Another `Dockerfile` is added in the `./www` folder for the PHP web application to build a self-contained image and avoid live file mounting
- A Redis container is added for caching using the official Redis Docker image
- The API service talks to the Redis service to avoid downloading and parsing pages that were already scraped before
- A `REDIS_URL` environment variable is added to the API service to allow it to connect to the Redis cache

Let's first inspect the newly added `Dockerfile` under the `./www` folder:

```bash
cat www/Dockerfile
```

```dockerfile
FROM php:7-apache
LABEL maintainer="Sawood Alam <@ibnesayeed>"

ENV API_ENDPOINT="http://localhost:5000/api/"

COPY . /var/www/html/
```

This is a rather simple `Dockerfile` that uses the official `php:7-apache` image as the base and copies all the files from the `./www` folder into the `/var/www/html/` folder of the image.
This is exactly what was happening in the previous step, but that was bind mounted using a volume, while here we are making the code part of the self-contained image.
We have also added the `API_ENDPOINT` environment variable here with a default value, which implicitly suggests that this is an important information that needs to be present in order for the service to function properly (and should be customized at run time with an appropriate value).

Next, we will look at the API server's `api/main.py` file where we are utilizing the Redis cache:

```bash
cat api/main.py
```

The file has many lines, but the important bits are as illustrated below:

```python
redis_conn = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
# ...
    jsonlinks = redis.get(url)
    if not jsonlinks:
        links = extract_links(url)
        jsonlinks = json.dumps(links, indent=2)
        redis.set(url, jsonlinks)
```

This time the API service needs to know how to connect to the Redis instance as it is going to use it for caching.
This information can be made available at run time using the `REDIS_URL` environment variable.
A corresponding `ENV` entry is also added in the `Dockerfile` of the API service with a default value.

A `redis` client instance is created using the hostname `redis` (same as the name of the service as we will see later) and the default Redis port `6379`.
We are first trying to see if a cache is present in the Redis store for a given URL, if not then we use the `extract_links` function as before and populate the cache for future attempts.

Now, let's look into the updated `docker-compose.yml` file:

```bash
cat docker-compose.yml
```

```yml
version: "3"

services:
  api:
    image: linkextractor-api:step5-python
    build: ./api
    ports:
      - "5000:5000"
    environment:
      - REDIS_URL=redis://redis:6379
  web:
    image: linkextractor-web:step5-php
    build: ./www
    ports:
      - "80:80"
    environment:
      - API_ENDPOINT=http://api:5000/api/
  redis:
    image: redis
```

The `api` service configuration largely remains the same as before, except the updated image tag and added environment variable `REDIS_URL` that points to the Redis service.
For the `web` service, we are using the custom `linkextractor-web:step5-php` image that will be built using the newly added `Dockerfile` in the `./www` folder.
We are no longer mounting the `./www` folder using the `volumes` config.
Finally, a new service named `redis` is added that will use the official image from DockerHub and needs no specific configurations for now.
This service is accessible to the Python API using its service name, the same way the API service is accessible to the PHP front-end service.

Let's boot these services up:

```bash
docker-compose up -d --build
```

```
... [OUTPUT REDACTED] ...

Creating linkextractor_web_1   ... done
Creating linkextractor_api_1   ... done
Creating linkextractor_redis_1 ... done
```

Now, that all three services are up, access the web interface by [clicking the Link Extractor](/){:data-term=".term1"}{:data-port="80"}.
There should be no visual difference from the previous step.
However, if you extract links from a page with a lot of links, the first time it should take longer, but the successive attempts to the same page should return the response fairly quickly.
To check whether or not the Redis service is being utilized, we can use `docker-compose exec` followed by the `redis` service name and the Redis CLI's [monitor](https://redis.io/commands/monitor) command:

```bash
docker-compose exec redis redis-cli monitor
```

Now, try to extract links from some web pages using the web interface and see the difference in Redis log entries for pages that are scraped the first time and those that are repeated.
Before continuing further with the tutorial, stop the interactive `monitor` stream as a result of the above `redis-cli` command by pressing `Ctrl + C` keys while the interactive terminal is in focus.

Now that we are not mounting the `/www` folder inside the container, local changes should not reflect in the running service:

```bash
sed -i 's/Link Extractor/Super Link Extractor/g' www/index.php
```

Verify that the changes made locally do not reflect in the running service by reloading the web interface and then revert changes:

```bash
git reset --hard
```

Now, shut these services down and get ready for the next step:

```bash
docker-compose down
```

```
Stopping linkextractor_web_1   ... done
Stopping linkextractor_redis_1 ... done
Stopping linkextractor_api_1   ... done
Removing linkextractor_web_1   ... done
Removing linkextractor_redis_1 ... done
Removing linkextractor_api_1   ... done
Removing network linkextractor_default
```

We have successfully orchestrated three microservices to compose our Link Extractor application.
We now have an application stack that represents the architecture illustrated in the figure shown in the introduction of this tutorial.
In the next step we will explore how easy it is to swap components from an application with the microservice architecture.
