# Service Discovery

Let us try to discover wordpressdb service from within one of wordpressapp container. Open up the manager node instance and run the below command:

Open up instance of worker node and verify what containers are running:

```.term2
docker ps
```

This should display number of tasks(containers) running on the worker node locally:

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS
           PORTS               NAMES
52f16028e12c        wordpress:latest    "docker-entrypoint..."   2 minutes ago       Up 2 minu
tes        80/tcp              wordpressapp.1.zg7wpvs1rbkiy4zwo71yk031i
f3271e89d54e        wordpress:latest    "docker-entrypoint..."   2 minutes ago       Up 2 minu
tes        80/tcp              wordpressapp.3.scia4v5i1znj378gujluad2ku

```

As shown above, there are 2 instances of wordpressapp task(container) running on the worker node.

Now, Open up manager node and confirm what task are running:

```bash
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS
           PORTS               NAMES
b68d99cad3da        wordpress:latest    "docker-entrypoint..."   5 minutes ago       Up 4 minu
tes        80/tcp              wordpressapp.2.8rybe5m4urikqsqje6hcpou9t
657cff3e37d5        wordpress:latest    "docker-entrypoint..."   5 minutes ago       Up 4 minu
tes        80/tcp              wordpressapp.4.4avyixggcb8neej1h395ognt2
e71c164c36b3        mysql:latest        "docker-entrypoint..."   10 minutes ago      Up 10 min
utes       3306/tcp            wordpressdb.1.puoe9lvfkciavkrzrkbrhrl6e
```

As we notice, there are 2 instances of wordpressapp task(container) running on the manager node(shown above) and 1 instance of wordpressdb.

Let's pick up the wordpressdb task running on the manager node and try to reach out to wordpressapp running on the remote worker node. Because the container is missing the `ping` command we need to install it first:

```bash
docker exec -it e71 bash -c "apt update && apt -y install iputils-ping"
```

Once installed, we can ping wordpressapp as shown below:

```bash
docker exec -it e71 ping wordpressapp
```

This should work successfully and be able to ping the wordpressapp as service name.

```
PING wordpressapp (10.0.0.4): 56 data bytes
64 bytes from 10.0.0.4: icmp_seq=0 ttl=64 time=0.052 ms
^C
```
