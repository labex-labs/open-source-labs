# Updating nodes

You can also drain a particular node, that is remove all services from that node. The services will automatically be rescheduled on other nodes.

```bash
docker node update --availability drain node2
```

```bash
docker service ps web
```

You can check out the nodes and see that `node2` is still active but drained.

```bash
docker node ls
```
