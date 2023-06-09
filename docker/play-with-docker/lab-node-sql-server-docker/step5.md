# Add a reverse proxy to improve performance

[Node.js](https://nodejs.org/en/) is a good server platform, but it's easy to improve performance by putting a reverse proxy in front of the Node.js application. The proxy is the public entrypoint to the app, and it handles requests from users.

[Nginx](http://nginx.org) is a popular open source web server which you can easily configure as a reverse proxy. The [Nginx configuration](https://github.com/dockersamples/node-bulletin-board/blob/v4/bulletin-board-proxy/nginx.conf) in this part makes use of browser and server caching, which reduces the load on the web application and improves performance.

Switch to the v4 code branch:

```bash
git checkout v4
```

And use Docker Compose to build the application:

```bash
docker-compose build
```

Now you have `v4` Docker images for all the application parts, you can upgrade the running stack using the new [docker-stack.yml](https://github.com/dockersamples/node-bulletin-board/blob/v4/docker-stack.yml) file:

```bash
docker stack deploy -c docker-stack.yml bb
```

Version 4 adds a proxy server to the stack which publishes port `80`, so now you can browse to the app on the standard HTTP port:

[Click here for v4 of the app](/){:data-term=".term1"}{:data-port="80"}

The web application looks the same, but behind the scenes all the hard work is being done by the Nginx proxy. You can open developer tools on your browser and inspect the network responses - Nginx has added browser caching hints, and it's also using a local cache to reduce traffic to the Node.js app.

There are also several instances of the proxy container running - Docker swarm load-balances incoming requests between those containers. If you had multiple servers in the swarm, you would be able to scale up to handle your incoming workload.

In the final part you'll add monitoring to the application, so you can see what the Node.js container is doing.
