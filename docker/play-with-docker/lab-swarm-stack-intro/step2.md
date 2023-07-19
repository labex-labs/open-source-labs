# Show members of swarm

From the first terminal, check the number of nodes in the swarm (running this command from the second terminal `worker` will fail as swarm related commands need to be issued against a swarm manager).

```bash
docker node ls
```

The above command should output 2 nodes, the first one being the `manager`, and the second one a `worker`.
