# Init your swarm

Let's create a Docker Swarm first. Open up the first instance and initiate Swarm mode cluster.

```bash
docker swarm init --advertise-addr $(hostname -i)
```

This node becomes a master node. The output displays a command to add a worker node to this swarm as shown below:

```
Swarm initialized: current node (xf323rkhg80qy2pywkjkxqusp) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-089phhmfamjor1o1qj8s0l4wdhyvegphg6vtt9p3s8c35upltk-eecvhhtz1f2vpjhvc70v6v
vzb \
    10.0.50.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructi
ons.
```

The above token ID is unique for every swarm mode cluster and hence might differ for your setup.
From the output above, copy the join command (_watch out for newlines_).

Next, Open up the new instance and paste the below command. This should join the new node to the swarm mode cluster and this new node becomes a worker node. In my case, the command would look something like this:

```
 docker swarm join \
    --token SWMTKN-1-089phhmfamjor1o1qj8s0l4wdhyvegphg6vtt9p3s8c35upltk-eecvhhtz1f2vpjhvc70v6v
vzb \
    10.0.50.3:2377
```

Output:

```
$ docker swarm join --token SWMTKN-1-089phhmfamjor1o1qj8s0l4wdhyvegphg6vtt9p3s8c35upltk-eecvhh
tz1f2vpjhvc70v6vvzb 10.0.50.3:2377
This node joined a swarm as a worker.
```
