# Scaling up

We will be performing these actions in the first terminal. Next let's inspect the service:

```bash
docker service inspect web
```

That's lots of info! Now, let's scale the service:

```bash
docker service scale web=15
```

Docker has spread the 15 services evenly over all of the nodes

```bash
docker service ps web
```
