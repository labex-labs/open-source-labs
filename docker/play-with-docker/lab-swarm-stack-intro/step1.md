# Init your swarm

There should be two terminals displayed. The first accesses the swarm `manager` node and the second accesses the swarm `worker` node once the swarm is created.

Let's create a Docker Swarm first. Copy the below command into the first terminal.

```bash
docker swarm init --advertise-addr $(hostname -i)
```

From the output above, copy the join command (_watch out for newlines_) and paste it in the other terminal.
