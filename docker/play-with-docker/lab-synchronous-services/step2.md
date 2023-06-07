# Creating a synchronous service

Initialize your swarm

```bash
docker swarm init --advertise-addr eth1
```

Create a new synchronous serivce using the new `-d` flag

```bash
docker service create -d=false --name top --replicas 5 busybox top
```

You should an output similar to the following in the terminal:

```
mmsdrpbigre7ls9vp6mhig3vz
overall progress: 5 out of 5 tasks
1/5: running   [==================================================>]
2/5: running   [==================================================>]
3/5: running   [==================================================>]
4/5: running   [==================================================>]
5/5: running   [==================================================>]
verify: Waiting 1 seconds to verify that tasks are stable...
```

As you can see, a nice progress bar will display the status of the overall deployment.

> **Note:** If you press Ctrl+C while the service is being created, it will be sent to background automatically

We'll check how `update` also works with the `--detach` paramter now.

```bash
docker service update -d=false --force --update-parallelism 0 top
```