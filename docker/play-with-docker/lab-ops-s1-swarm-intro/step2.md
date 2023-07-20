# Show Swarm Members

From the first terminal window, check the number of nodes in the swarm (running this command from the second terminal worker node will fail as swarm related commands need to be issued against a swarm manager).

```bash
docker node ls
```

The above command should output 2 nodes, the first one being the manager, and the second one a worker. You should see that your manager node is also the "Leader". This is because you only have one manager node. The Leader is just what it sounds like: the main control node for all the managers. If your Leader node goes down for some reason, the other manager nodes will elect a new leader; just one reason why you would always have multiple manager nodes in true production.

Here is a view of managers and workers in Docker Swarm Mode. In our exercise, we have just one manager and one worker, but you can see how multiple managers and workers interact in the diagram:
![Swarm architecture](/images/ops-swarm-arch.svg)
