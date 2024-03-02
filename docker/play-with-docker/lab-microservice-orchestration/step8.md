# Swap Python API Service with Ruby

Checkout the `step6` branch and list files in it.

```bash
git checkout step6
tree
```

```
.
├── README.md
├── api
│   ├── Dockerfile
│   ├── Gemfile
│   └── linkextractor.rb
├── docker-compose.yml
├── logs
└── www
    ├── Dockerfile
    └── index.php

3 directories, 7 files
```

Some significant changes from the previous step include:

- The API service written in Python is replaced with a similar Ruby implementation
- The `API_ENDPOINT` environment variable is updated to point to the new Ruby API service
- The link extraction cache event (HIT/MISS) is logged and is persisted using volumes

Notice that the `./api` folder does not contain any Python scripts, instead, it now has a Ruby file and a `Gemfile` to manage dependencies.

Let's have a quick walk through the changed files:

```bash
cat api/linkextractor.rb
```

```rb
#!/usr/bin/env ruby
# encoding: utf-8

require "sinatra"
require "open-uri"
require "uri"
require "nokogiri"
require "json"
require "redis"

set :protection, :except=>:path_traversal

redis = Redis.new(url: ENV["REDIS_URL"] || "redis://localhost:6379")

Dir.mkdir("logs") unless Dir.exist?("logs")

get "/" do
  "Usage: http://<hostname>[:<prt>]/api/<url>"
end

get "/api/*" do
  url = [params['splat'].first, request.query_string].reject(&:empty?).join("?")
  cache_status = "HIT"
  jsonlinks = redis.get(url)
  if jsonlinks.nil?
    cache_status = "MISS"
    jsonlinks = JSON.pretty_generate(extract_links(url))
    redis.set(url, jsonlinks)
  end

  cache_log = File.open("logs/extraction.log", "a")
  cache_log.puts "#{Time.now.to_i}\t#{cache_status}\t#{url}"
  cache_log.close

  status 200
  headers "content-type" => "application/json"
  body jsonlinks
end

def extract_links(url)
  links = []
  doc = Nokogiri::HTML(open(url))
  doc.css("a").each do |link|
    text = link.text.strip.split.join(" ")
    begin
      links.push({
        text: text.empty? ? "[IMG]" : text,
        href: URI.join(url, link["href"])
      })
    rescue
    end
  end
  links
end
```

This Ruby file is almost equivalent to what we had in Python before, except, in addition to that it also logs the link extraction requests and corresponding cache events.
In a microservice architecture application swapping components with an equivalent one is easy as long as the expectations of consumers of the component are maintained.

```bash
cat api/Dockerfile
```

```dockerfile
FROM ruby:2.6
LABEL maintainer="Sawood Alam <@ibnesayeed>"

ENV LANG C.UTF-8
ENV REDIS_URL="redis://localhost:6379"

WORKDIR /app
COPY Gemfile /app/
RUN bundle install

COPY linkextractor.rb /app/
RUN chmod a+x linkextractor.rb

CMD ["./linkextractor.rb", "-o", "0.0.0.0"]
```

Above `Dockerfile` is written for the Ruby script and it is pretty much self-explanatory.

```bash
cat docker-compose.yml
```

```yml
version: "3"

services:
  api:
    image: linkextractor-api:step6-ruby
    build: ./api
    ports:
      - "4567:4567"
    environment:
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./logs:/app/logs
  web:
    image: linkextractor-web:step6-php
    build: ./www
    ports:
      - "80:80"
    environment:
      - API_ENDPOINT=http://api:4567/api/
  redis:
    image: redis
```

The `docker-compose.yml` file has a few minor changes in it.
The `api` service image is now named `linkextractor-api:step6-ruby`, the port mapping is changed from `5000` to `4567` (which is the default port for Sinatra server), and the `API_ENDPOINT` environment variable in the `web` service is updated accordingly so that the PHP code can talk to it.

With these in place, let's boot our service stack:

```bash
docker-compose up -d --build
```

```
... [OUTPUT REDACTED] ...

Successfully built b713eef49f55
Successfully tagged linkextractor-api:step6-ruby
Creating linkextractor_web_1   ... done
Creating linkextractor_api_1   ... done
Creating linkextractor_redis_1 ... done
```

We should now be able to access the API (using the updated port number):

```bash
curl -i http://localhost:4567/api/http://example.com/
```

```json
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 96
X-Content-Type-Options: nosniff
Server: WEBrick/1.4.2 (Ruby/2.5.1/2018-03-29)
Date: Mon, 24 Sep 2018 01:41:35 GMT
Connection: Keep-Alive

[
  {
    "text": "More information...",
    "href": "http://www.iana.org/domains/example"
  }
]
```

Now, open the web interface by [clicking the Link Extractor](/){:data-term=".term1"}{:data-port="80"} and extract links of a few URLs.
Also, try to repeat these attempts for some URLs.
If everything is alright, the web application should behave as before without noticing any changes in the API service (which is completely replaced).

We can use the `tail` command with the `-f` or `--follow` option to follow the log output live.

```bash
tail -f logs/extraction.log
```

Try a few more URLs in the web interface. You should see the new log entries appear in the terminal.

To stop following the log, press `Ctrl + C` keys while the interactive terminal is in focus.

We can shut the stack down now:

```bash
docker-compose down
```

Since we have persisted logs, they should still be available after the services are gone:

```bash
cat logs/extraction.log
```

```
1537753295      MISS    http://example.com/
1537753600      HIT     http://example.com/
1537753635      MISS    https://training.play-with-docker.com/
```

This illustrates that the caching is functional as the second attempt to the `http://example.com/` resulted in a cache `HIT`.

In this step we explored the possibility of swapping components of an application with microservice architecture with their equivalents without impacting rest of the parts of the stack.
We have also explored data persistence using bind mount volumes that persists even after the containers writing to the volume are gone.

So far, we have used `docker-compose` utility to orchestrate the application stack, which is good for development environment, but for production environment we use `docker stack deploy` command to run the application in a [Docker Swarm Cluster](/swarm-stack-intro).
It is left for you as an assignment to deploy this application in a Docker Swarm Cluster.
