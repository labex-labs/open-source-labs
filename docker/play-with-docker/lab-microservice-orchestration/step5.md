# Step 3: Link Extractor API Service

Checkout the `step3` branch and list files in it.

```bash
git checkout step3
tree
```

```
.
├── Dockerfile
├── README.md
├── linkextractor.py
├── main.py
└── requirements.txt

0 directories, 5 files
```

The following changes have been made in this step:

- Added a server script `main.py` that utilizes the link extraction module written in the last step
- The `Dockerfile` is updated to refer to the `main.py` file instead
- Server is accessible as a WEB API at `http://<hostname>[:<prt>]/api/<url>`
- Dependencies are moved to the `requirements.txt` file
- Needs port mapping to make the service accessible outside of the container (the `Flask` server used here listens on port `5000` by default)

Let's first look at the `Dockerfile` for changes:

```bash
cat Dockerfile
```

```dockerfile
FROM python:3
LABEL maintainer="Sawood Alam <@ibnesayeed>"

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY *.py /app/
RUN chmod a+x *.py

CMD ["./main.py"]
```

Since we have started using `requirements.txt` for dependencies, we no longer need to run `pip install` command for individual packages.
The `ENTRYPOINT` directive is replaced with the `CMD` and it is referring to the `main.py` script that has the server code it because we do not want to use this image for one-off commands now.

The `linkextractor.py` module remains unchanged in this step, so let's look into the newly added `main.py` file:

```bash
cat main.py
```

```python
#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify
from linkextractor import extract_links

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<url>"

@app.route("/api/<path:url>")
def api(url):
    qs = request.query_string.decode("utf-8")
    if qs != "":
        url += "?" + qs
    links = extract_links(url)
    return jsonify(links)

app.run(host="0.0.0.0")
```

Here, we are importing `extract_links` function from the `linkextractor` module and converting the returned list of objects into a JSON response.

It's time to build a new image with these changes in place:

```bash
docker image build -t linkextractor:step3 .
```

Then run the container in detached mode (`-d` flag) so that the terminal is available for other commands while the container is still running.
Note that we are mapping the port `5000` of the container with the `5000` of the host (using `-p 5000:5000` argument) to make it accessible from the host.
We are also assigning a name (`--name=linkextractor`) to the container to make it easier to see logs and kill or remove the container.

```bash
docker container run -d -p 5000:5000 --name=linkextractor linkextractor:step3
```

If things go well, we should be able to see the container being listed in `Up` condition:

```bash
docker container ls
```

```
CONTAINER ID        IMAGE                 COMMAND             CREATED             STATUSPORTS                    NAMES
d69c0150a754        linkextractor:step3   "./main.py"         9 seconds ago       Up 8 seconds0.0.0.0:5000->5000/tcp   linkextractor
```

We can now make an HTTP request in the form `/api/<url>` to talk to this server and fetch the response containing extracted links:

```bash
curl -i http://localhost:5000/api/http://example.com/
```

```json
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 78
Server: Werkzeug/0.14.1 Python/3.7.0
Date: Sun, 23 Sep 2018 20:52:56 GMT

[{"href":"http://www.iana.org/domains/example","text":"More information..."}]
```

Now, we have the API service running that accepts requests in the form `/api/<url>` and responds with a JSON containing hyperlinks and anchor texts of all the links present in the web page at give `<url>`.

Since the container is running in detached mode, so we can't see what's happening inside, but we can see logs using the name `linkextractor` we assigned to our container:

```bash
docker container logs linkextractor
```

```
* Serving Flask app "main" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [23/Sep/2018 20:52:56] "GET /api/http://example.com/ HTTP/1.1" 200 -
```

We can see the messages logged when the server came up, and an entry of the request log when we ran the `curl` command.
Now we can kill and remove this container:

```bash
docker container rm -f linkextractor
```

In this step we have successfully ran an API service listening on port `5000`.
This is great, but APIs and JSON responses are for machines, so in the next step we will run a web service with a human-friendly web interface in addition to this API service.
