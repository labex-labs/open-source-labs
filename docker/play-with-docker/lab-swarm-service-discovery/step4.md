# Creating WordPress service

```bash
docker service create \
  --replicas 4 \
  --name wordpressapp \
  --network net1 \
  --env WORDPRESS_DB_HOST=wordpressdb \
  --env WORDPRESS_DB_PASSWORD=mysql123 \
  wordpress:latest
```

The above command creates a service named "wordpressapp" which belongs to "net1" network which runs 4 copies of wordpressapp container.
As output, this command displays a service ID as:

```
m4hca6rliz8wer2aojayv01r5
```

Listing out the services:

```bash
docker service ls
```

Output:

```
ID                  NAME                MODE                REPLICAS            IMAGE
ID                  NAME                MODE                REPLICAS            IMAGE
ip9a8zl9rke2        wordpressdb         replicated          1/1                 mysql:latest
m4hca6rliz8w        wordpressapp        replicated          4/4                 wordpress:late
st
```

You can list the tasks of the wordpressapp service using the command:

```bash
docker service ps wordpressapp
```

Output:

```
ID                  NAME                IMAGE               NODE                DESIRED STATE
      CURRENT STATE                ERROR               PORTS
zg7wpvs1rbki        wordpressapp.1      wordpress:latest    node2               Running
      Running 58 seconds ago
8rybe5m4urik        wordpressapp.2      wordpress:latest    node1               Running
      Running about a minute ago
scia4v5i1znj        wordpressapp.3      wordpress:latest    node2               Running
      Running 58 seconds ago
4avyixggcb8n        wordpressapp.4      wordpress:latest    node1               Running
      Running about a minute ago

```
