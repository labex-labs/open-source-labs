# Initialize Your Swarm

First thing we need to do is tell our Docker hosts we want to use Docker Swarm Mode. Swarms _can_ be just a single node, but that is unusual as you would have no high availability capabilities and you would severely limit your scalability. Most production swarms have at least three _manager_ nodes in them and many _worker_ nodes. Three managers is the minimum to have a true high-availability cluster with quorum. Note that manager nodes can run your container tasks the same as a worker node, but this functionality can also be separated so that managers only perform the management tasks.

Initializing Docker Swarm Mode is easy. In the first terminal window labeled [node1] enter the following:

```bash
docker swarm init --advertise-addr $(hostname -i)
```

That's it - you now have your first Swarm manager and it is listening on the IP address returned by the (hostname -i) command. You should see some output that looks like this:

```
Swarm initialized: current node (tjocs7ul557phkmp6mkpjmu3f) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token <token> <host>

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

In the output of your swarm init, you are given a command in the middle that looks like `docker swarm join -token SWMTKN-X-abcdef.....` which you use to join workers nodes to the swarm. You are also given a second command `docker swarm join-token manager` for adding additional managers.

We are going to add a worker. Copy the "docker swarm join..." command from your manager's output and paste it in the 2nd terminal window on your screen. _Make sure to copy the entire command - it's likely to break across multiple lines - and do not copy the sample command above because your token will be different_.

You now officially have a Docker Swarm! Currently, you have one manager and one worker. As hinted at above, you would almost always have 3 or more manager nodes and several worker nodes in order to maintain high availability and scalability, but one of each is enough to get started.
