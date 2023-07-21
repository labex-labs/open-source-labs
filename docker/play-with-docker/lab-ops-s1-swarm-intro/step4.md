# Deploy a Stack

A **_stack_** is a group of **_services_** that are deployed together: multiple containerized components of an application that run in separate instances. Each individual _service_ can actually be made up of one or more containers, called **_tasks_** and then all the tasks & services together make up a _stack_.

As with Dockerfiles and the Compose files, the file that defines a stack is a plain text file that is easy to edit and track. In our exercise, there is a file called `docker-stack.yml` in the current folder which will be used to deploy the voting app as a stack. Enter the following to investigate the `docker-stack.yml` file:

```bash
cat docker-stack.yml
```

This YAML file defines our entire stack: the architecture of the services, number of instances, how everything is wired together, how to handle updates to each service. It is the source code for our application design. A few items of particular note:

- Near the top of the file you will see the line "services:". These are the individual application components. In the voting app we have redis, db, vote, result, worker, and visualizer as our services.
- Beneath each service are lines that specify how that service should run:
  - Notice the familiar term _image_ from earlier labs? Same idea here: this is the container image to use for a particular service.
  - _Ports_ and _networks_ are mostly self-explanatory although it is worth pointing out that these networks and ports can be privately used within the stack or they can allow external communication to and from a stack.<sup id="a2">[2](#fn-network)</sup>
  - Note that some services have a line labeled _replicas_: this indicates the number of instances, or tasks, of this service that the Swarm managers should start when the stack is brought up. The Docker engine is intelligent enough to automatically load balance between multiple replicas using built-in load balancers. (The built-in load balancer can, of course, be swapped out for something else.)

Ensure you are in the [node1] manager terminal and do the following:

```bash
docker stack deploy --compose-file=docker-stack.yml voting_stack
```

You can see if the stack deployed from the [node1] manager terminal

```bash
docker stack ls
```

The output should be the following. It indicates the 6 services of the voting app's stack (named voting_stack) have been deployed.

```
NAME          SERVICES
voting_stack  6
```

We can get details on each service within the stack with the following:

```bash
docker stack services voting_stack
```

The output should be similar to the following, although naturally your IDs will be unique:

```
ID            NAME                     MODE        REPLICAS  IMAGE
10rt1wczotze  voting_stack_visualizer  replicated  1/1       dockersample
s/visualizer:stable
8lqj31k3q5ek  voting_stack_redis       replicated  1/1       redis:alpine
nhb4igkkyg4y  voting_stack_result      replicated  1/1       dockersample
s/examplevotingapp_result:before
nv8d2z2qhlx4  voting_stack_db          replicated  1/1       postgres:9.4
ou47zdyf6cd0  voting_stack_vote        replicated  2/2       dockersample
s/examplevotingapp_vote:before
rpnxwmoipagq  voting_stack_worker      replicated  1/1       dockersample
s/examplevotingapp_worker:latest
```

If you see that there are 0 replicas just wait a few seconds and enter the command again. The Swarm will eventually get all the replicas running for you. Just like our `docker-stack` file specified, there are two replicas of the _voting_stack_vote_ service and one of each of the others.

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

From the NODE column, we can see one task is running on each node. This app happens to have a built-in [SWARM VISUALIZER](/){:data-term=".term1"}{:data-port="8080"} to show you how the app is setup and running. You can also access the [front-end web UI](/){:data-term=".term1"}{:data-port="5000"} of the app to cast your vote for dogs or cats, and track how the votes are going on the [result](/){:data-term=".term1"}{:data-port="5001"} page. Try opening the front-end several times so you can cast multiple votes. You should see that the "container ID" listed at the bottom of the voting page changes since we have two replicas running.

The [SWARM VISUALIZER](/){:data-term=".term1"}{:data-port="8080"} gives you the physical layout of the stack, but here is a logical interpretation of how stacks, services and tasks are inter-related:
![Stack, services and tasks](/images/ops-swarm-stack-service-task.svg)
