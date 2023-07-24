# Add monitoring and an application dashboard

Docker swarm makes it super easy to scale containers, but before you go to production witrh a Dockerized application, you'll want monitoring in place so you can see what all those containers are doing.

Two open-source technologies are very popular in the Docker ecosystem for monitoring containers. [Prometheus](https://prometheus.io) is an instrumentation server that collects and stores metrics from your containers, and [Grafana](https://grafana.com) is an analytics UI that plugs into Prometheus to show dashboards.

In this part you'll add Prometheus and Grafana to your application.

First switch to the v5 code branch:

```bash
git checkout v5
```

Now build the application, which will build images from [the Prometheus Dockerfile](https://github.com/dockersamples/node-bulletin-board/blob/v5/bulletin-board-metrics/Dockerfile) and [the Grafana Dockerfile](https://github.com/dockersamples/node-bulletin-board/blob/v5/bulletin-board-dashboard/Dockerfile):

```bash
docker-compose build
```

You have `v5` images for all the application components now. Upgrade the stack to the v5 [docker-stack.yml](https://github.com/dockersamples/node-bulletin-board/blob/v5/docker-stack.yml) file:

```
docker stack deploy -c docker-stack.yml bb
```

[Click here for v5 of the app](/){:data-term=".term1"}{:data-port="80"}

The UX is the same, but now the Prometheus container is scraping metrics from the Node.js container, every 5 seconds.

To see the application metrics in Grafana, you need to configure the dashboard:

[Click here for Grafana](/){:data-term=".term1"}{:data-port="3000"}

Log in to Grafana with the credentials `admin` / `admin`.

Add a new data source with the following details:

- Name: **prometheus**

- Type: **Prometheus**

- URL: **http://bb-metrics:9090**

![Grafana data source](../images/node-sql-server-docker-grafana-data-source.jpg)

From the Grafana icon, click _Dashboards... Import_ and load the JSON dashboard file from [v5 /dashboard.json](https://github.com/dockersamples/node-bulletin-board/blob/v5/bulletin-board-dashboard/dashboard.json). Select the Prometheus data store.

You'll now see the application dashboard - send some load into the app by refreshing the browser, and the graphs will be populated:

![Grafana dashboard](img/grafana-dashboard.jpg)
