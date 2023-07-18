# Show members of swarm

Type the below command in the first terminal:

```bash
docker node ls
```

The output shows you both the manager and worker node indicating 2-node cluster:

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
xf323rkhg80qy2pywkjkxqusp *  node1     Ready   Active        Leader
za75md1p0hpc2qswefj8uyktk    node2     Ready   Active
```

If you try to execute an administrative command in a non-leader node `worker`, you'll get an error. Try it here:

```.term2
docker node ls
```
