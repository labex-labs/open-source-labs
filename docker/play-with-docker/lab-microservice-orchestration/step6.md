# Link Extractor API and Web Front End Services

Checkout the `step4` branch and list files in it.

```bash
git checkout step4
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
    └── index.php

2 directories, 7 files
```

In this step the following changes have been made since the last step:

- The link extractor JSON API service (written in Python) is moved in a separate `./api` folder that has the exact same code as in the previous step
- A web front-end application is written in PHP under `./www` folder that talks to the JSON API
- The PHP application is mounted inside the official `php:7-apache` Docker image for easier modification during the development
- The web application is made accessible at `http://<hostname>[:<prt>]/?url=<url-encoded-url>`
- An environment variable `API_ENDPOINT` is used inside the PHP application to configure it to talk to the JSON API server
- A `docker-compose.yml` file is written to build various components and glue them together

In this step we are planning to run two separate containers, one for the API and the other for the web interface.
The latter needs a way to talk to the API server.
For the two containers to be able to talk to each other, we can either map their ports on the host machine and use that for request routing or we can place the containers in a single private network and access directly.
Docker has excellent support for networking and provides helpful commands for dealing with networks.
Additionally, in a Docker network containers identify themselves using their names as hostnames to avoid hunting for their IP addresses in the private network.
However, we are not going to do any of this manually, instead we will be using Docker Compose to automate many of these tasks.

So let's look at the `docker-compose.yml` file we have:

```bash
cat docker-compose.yml
```

```yml
version: "3"

services:
  api:
    image: linkextractor-api:step4-python
    build: ./api
    ports:
      - "5000:5000"
  web:
    image: php:7-apache
    ports:
      - "80:80"
    environment:
      - API_ENDPOINT=http://api:5000/api/
    volumes:
      - ./www:/var/www/html
```

This is a simple YAML file that describes the two services `api` and `web`.
The `api` service will use the `linkextractor-api:step4-python` image that is not built yet, but will be built on-demand using the `Dockerfile` from the `./api` directory.
This service will be exposed on the port `5000` of the host.

The second service named `web` will use official `php:7-apache` image directly from the DockerHub, that's why we do not have a `Dockerfile` for it.
The service will be exposed on the default HTTP port (i.e., `80`).
We will supply an environment variable named `API_ENDPOINT` with the value `http://api:5000/api/` to tell the PHP script where to connect to for the API access.
Notice that we are not using an IP address here, instead, `api:5000` is being used because we will have a dynamic hostname entry in the private network for the API service matching its service name.
Finally, we will bind mount the `./www` folder to make the `index.php` file available inside of the `web` service container at `/var/www/html`, which is the default web root for the Apache web server.

Now, let's have a look at the user-facing `www/index.php` file:

```bash
cat www/index.php
```

This is a long file that mainly contains all the markup and styles of the page.
However, the important block of code is in the beginning of the file as illustrated below:

```php
$api_endpoint = $_ENV["API_ENDPOINT"] ?: "http://localhost:5000/api/";
$url = "";
if(isset($_GET["url"]) && $_GET["url"] != "") {
  $url = $_GET["url"];
  $json = @file_get_contents($api_endpoint . $url);
  if($json == false) {
    $err = "Something is wrong with the URL: " . $url;
  } else {
    $links = json_decode($json, true);
    $domains = [];
    foreach($links as $link) {
      array_push($domains, parse_url($link["href"], PHP_URL_HOST));
    }
    $domainct = @array_count_values($domains);
    arsort($domainct);
  }
}
```

The `$api_endpoint` variable is initialized with the value of the environment variable supplied from the `docker-compose.yml` file as `$_ENV["API_ENDPOINT"]` (otherwise falls back to a default value of `http://localhost:5000/api/`).
The request is made using `file_get_contents` function that uses the `$api_endpoint` variable and user supplied URL from `$_GET["url"]`.
Some analysis and transformations are performed on the received response that are later used in the markup to populate the page.

Let's bring these services up in detached mode using `docker-compose` utility:

```bash
docker-compose up -d --build
```

```
Creating network "linkextractor_default" with the default driver
Pulling web (php:7-apache)...
7-apache: Pulling from library/php

... [OUTPUT REDACTED] ...

Status: Downloaded newer image for php:7-apache
Building api
Step 1/8 : FROM       python:3

... [OUTPUT REDACTED] ...

Successfully built 1f419be1c2bf
Successfully tagged linkextractor-api:step4-python
Creating linkextractor_web_1 ... done
Creating linkextractor_api_1 ... done
```

This output shows that Docker Compose automatically created a network named `linkextractor_default`, pulled `php:7-apache` image from DockerHub, built `api:python` image using our local `Dockerfile`, and finally, spun two containers `linkextractor_web_1` and `linkextractor_api_1` that correspond to the two services we have defined in the YAML file above.

Checking for the list of running containers confirms that the two services are indeed running:

```bash
docker container ls
```

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS   PORTS                    NAMES
268b021b5a2c        php:7-apache                     "docker-php-entrypoi…"   3 minutes ago       Up 3 minutes        0.0.0.0:80->80/tcp       linkextractor_web_1
5bc266b4e43d        linkextractor-api:step4-python   "./main.py"              3 minutes ago       Up 3 minutes        0.0.0.0:5000->5000/tcp   linkextractor_api_1
```

We should now be able to talk to the API service as before:

```bash
curl -i http://localhost:5000/api/http://example.com/
```

To access the web interface [click to open the Link Extractor](/){:data-term=".term1"}{:data-port="80"}.
Then fill the form with `https://training.play-with-docker.com/` (or any HTML page URL of your choice) and submit to extract links from it.

We have just created an application with microservice architecture, isolating individual tasks in separate services as opposed to monolithic applications where everything is put together in a single unit.
Microservice applications are relatively easier to scale, maintains, and move around.
They also allow easy swapping of components with an equivalent service.
More on that later.

Now, let's modify the `www/index.php` file to replace all occurrences of `Link Extractor` with `Super Link Extractor`:

```bash
sed -i 's/Link Extractor/Super Link Extractor/g' www/index.php
```

Reloading the web interface of the application (or [clicking here](/){:data-term=".term1"}{:data-port="80"}) should now reflect this change in the title, header, and footer.
This is happening because the `./www` folder is bind mounted inside of the container, so any changes made outside will reflect inside the container or the vice versa.
This approach is very helpful in development, but in the production environment we would prefer our Docker images to be self-contained.
Let's revert these changes now to clean the Git tracking:

```bash
git reset --hard
```

Before we move on to the next step we need to shut these services down, but Docker Compose can help us take care of it very easily:

```bash
docker-compose down
```

```
Stopping linkextractor_api_1 ... done
Stopping linkextractor_web_1 ... done
Removing linkextractor_api_1 ... done
Removing linkextractor_web_1 ... done
Removing network linkextractor_default
```

In the next step we will add one more service to our stack and will build a self-contained custom image for our web interface service.
