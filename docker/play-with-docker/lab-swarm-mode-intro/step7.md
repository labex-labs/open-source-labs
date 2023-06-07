# Scaling down

You can also scale down the service

```bash
docker service scale web=10
```

Lets check our service status

```bash
docker service ps web
```

Now bring `node2` back online and show it's new availability

```bash
docker node update --availability active node2
```

```bash
docker node inspect node2 --pretty
```

{:.quiz}
Which of these can you do with Docker Swarm Mode?

- [x] add a node
- [x] start a service
- [x] end a service
- [x] list all service
- [x] scale up the number of replicas of a service
- [x] take a node out of the swarm