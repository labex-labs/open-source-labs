# Deploy a Microservice Application

We have see how we can leverage Docker labels to dynamically customize our LoadBalancing routing rules, and how docker-compose can be used to create and link services together.

Now let's try to launch a **more complicated** Microservice application.

We will uses **Docker's vote** microservice application with custom labels to be used within our Docker Flow Proxy loadbalancer.

<img src="https://github.com/allamand/example-voting-app/raw/master/proxy_voting.png" width="600">

The voting application is composed of :

- A Python webapp which lets you vote between two options
- A Redis queue which collects new votes
- A Java worker which consumes votes and stores them in…
- A Postgres database backed by a Docker volume
- A Node.js webapp which shows the results of the voting in real time

### Run voting microservice application

First you need to Retrieve voting-app application

```bash
git clone https://github.com/allamand/example-voting-app.git
```

Go to the stack directory

```bash
cd example-voting-app
```

and launch the app using docker-compose file, you can view the **docker-compose-flow-proxy.yml** file

```bash
docker stack deploy cloud -c docker-compose-flow-proxy.yml
```

> This command will build each part of the microservice from sources.
> It may take a little time to get all services up & running (time to download images..)
> You can take a coffee since this may take a little to finish ;)

#### Rewriting Paths

In this example, we need the incoming requests that starts with `/vote/` or `/result/` to be routed to the according services by the proxy.
But each of our service needs traffic to be send on `/`, so we need the Proxy to **rewrite** the Path while sending the request.

For that we are using specific docker-flow labels `reqPathSearch` and `reqPathReplace`:

```
      labels:
        - com.df.notify=true
        - com.df.distribute=true
        - com.df.servicePath=/vote/
        - com.df.reqPathSearch=/vote/
        - com.df.reqPathReplace=/
        - com.df.port=80

```

To monitor the setup state, you can use:

```bash
docker stack ps cloud
```

> Be carreful, the Output shows two state columns :

> - **Desired State** which represents what you are asking to swarm
> - **Current State** which is the current state of the container (which may be stuck in Preparing for a moment while downloading the images).

Once all containers are in the **Running** state, you can start test the application.

While the application is working you can take a look at the docker-compose file we are deploying :

```bash
cat docker-compose-flow-proxy.yml
```

We can view the updated configuration on the proxy API

```bash
curl http://localhost:8080/v1/docker-flow-proxy/config
```

#### You can now make your Vote!!

- [Link to vote service](/vote/){:data-term=".term1"}{:data-port="80"}

#### And See the results of votes

- [Link to result service](/result/){:data-term=".term1"}{:data-port="80"}

You can see the logs of the services :

```bash
docker service logs --tail=10 cloud_vote
```

> You are now able to deploy any stack on Docker Swarm Mode using docker-compose and **Docker Flow Proxy**!
