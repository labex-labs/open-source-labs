# Deploy a stack

A stack is a group of services that are deployed together.
The docker-stack.yml in the current folder will be used to deploy the voting app as a stack.

Ensure you are in the first terminal and do the below:

```bash
docker stack deploy --compose-file=docker-stack.yml voting_stack
```

Note: being able to create a stack from a docker compose file is a great feature added in Docker 1.13.

Check the stack deployed from the first terminal

```bash
docker stack ls
```

The output should be the following one. It indicates the 6 services of the voting app's stack (named voting_stack) have been deployed.

```
NAME          SERVICES
voting_stack  6
```

Let's check the service within the stack

```bash
docker stack services voting_stack
```

The output should be like the following one (your ID should be different though).

```
ID            NAME                     MODE        REPLICAS  IMAGE
10rt1wczotze  voting_stack_visualizer  replicated  1/1       dockersample
s/visualizer:stable
8lqj31k3q5ek  voting_stack_redis       replicated  2/2       redis:alpine
nhb4igkkyg4y  voting_stack_result      replicated  2/2       dockersample
s/examplevotingapp_result:before
nv8d2z2qhlx4  voting_stack_db          replicated  1/1       postgres:9.4
ou47zdyf6cd0  voting_stack_vote        replicated  2/2       dockersample
s/examplevotingapp_vote:before
rpnxwmoipagq  voting_stack_worker      replicated  1/1       dockersample
s/examplevotingapp_worker:latest
```

Let's list the tasks of the vote service.

```bash
docker service ps voting_stack_vote
```

You should get an output like the following one where the 2 tasks (replicas) of the service are listed.

```
ID            NAME                 IMAGE
      NODE   DESIRED STATE  CURRENT STATE           ERROR  PORTS
my7jqgze7pgg  voting_stack_vote.1  dockersamples/examplevotingapp_vote:be
fore  node1  Running        Running 56 seconds ago
3jzgk39dyr6d  voting_stack_vote.2  dockersamples/examplevotingapp_vote:be
fore  node2  Running        Running 58 seconds ago
```

From the NODE column, we can see one task is running on each node.

Finally, we can check that our [APP](/){:data-term=".term1"}{:data-port="5000"} is running, the [RESULT](/){:data-term=".term1"}{:data-port="5001"} page is also available as well as [SWARM VISUALIZER](/){:data-term=".term1"}{:data-port="8080"}
