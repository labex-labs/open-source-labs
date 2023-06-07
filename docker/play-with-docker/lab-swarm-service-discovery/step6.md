# Create an overlay network

```bash
docker network create -d overlay net1
```

The above command generates an ID:

```
4md6wyy0pdpdzku6dj2z7yxjf
```

### List out the newly created overlay network using the below command:

```bash
docker network ls
```

The output should show the newly added network called "net1" holding swarm scope .

```
NETWORK ID          NAME                DRIVER              SCOPE
c30f13d9c242        bridge              bridge              local
990fa0ad6ab6        docker_gwbridge     bridge              local
c60123ff7abf        host                host                local
v7sp7ev6xfoo        ingress             overlay             swarm
4md6wyy0pdpd        net1                overlay             swarm
333c7d045239        none                null
```

### Creating MYSQL service

```bash
docker service create \
           --replicas 1 \
           --name wordpressdb \
           --network net1 \
           --env MYSQL_ROOT_PASSWORD=mysql123 \
           --env MYSQL_DATABASE=wordpress \
          mysql:latest
```

The above command creates a service named "wordpressdb" which belongs to "net1" network which runs a single replica of the container. It displays service ID as an output as shown:

```
ip9a8zl9rke256q92itgrm8ov
```

Run the below command to list out the service:

```bash
docker service ls
```

The output should be like the following one (your ID will display different though).

```
ID                  NAME                MODE                REPLICAS            IMAGE
ip9a8zl9rke2        wordpressdb         replicated          1/1                 mysql:latest
```

Let's list the tasks of the wordpressdb service.

```bash
docker service ps wordpressdb
```

You should get an output like the following one where the 1 task of the service are listed.

```
ID                  NAME                IMAGE               NODE                DESIRED STATE
      CURRENT STATE                ERROR               PORTS
puoe9lvfkcia        wordpressdb.1       mysql:latest        node1               Running
      Running about a minute ago
```
