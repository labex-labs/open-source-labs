# Show members of swarm

Type the below command in the first terminal:

```bash
docker node ls
```

That last line will show you a list of all the nodes, something like this:

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGE
R STATUS
kytp4gq5mrvmdbb0qpifdxeiv *  node1     Ready   Active        Leader
lz1j4d6290j8lityk4w0cxls5    node2     Ready   Active
```

If you try to execute an administrative command in a non-leader node `worker`, you'll get an error. Try it here:

```.term2
docker node ls
```
