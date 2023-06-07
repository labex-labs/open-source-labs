# In this lab you will play around with the container orchestration features of Docker. You will deploy a simple application to a single host and learn how that works. Then, you will configure Docker Swarm Mode, and learn to deploy the same simple application across multiple hosts. You will then see how to scale the application and move the workload across different hosts easily.

> **Difficulty**: Beginner

> **Time**: Approximately 30 minutes

> **Tasks**:
>
> - [Section #1 - What is Orchestration](#basics)
> - [Section #2 - Configure Swarm Mode](#start-cluster)
> - [Section #3 - Deploy applications across multiple hosts](#multi-application)
> - [Section #4 - Scale the application](#scale-application)
> - [Section #5 - Drain a node and reschedule the containers](#recover-application)
> - [Cleaning Up](#cleanup)

# Section 1: What is Orchestration

So, what is Orchestration anyways? Well, Orchestration is probably best described using an example. Let's say that you have an application that has high traffic along with high-availability requirements. Due to these requirements, you typically want to deploy across at least 3+ machines, so that in the event a host fails, your application will still be accessible from at least two others. Obviously, this is just an example and your use-case will likely have its own requirements, but you get the idea.

Deploying your application without Orchestration is typically very time consuming and error prone, because you would have to manually SSH into each machine, start up your application, and then continually keep tabs on things to make sure it is running as you expect.

But, with Orchestration tooling, you can typically off-load much of this manual work and let automation do the heavy lifting. One cool feature of Orchestration with Docker Swarm, is that you can deploy an application across many hosts with only a single command (once Swarm mode is enabled). Plus, if one of the supporting nodes dies in your Docker Swarm, other nodes will automatically pick up load, and your application will continue to hum along as usual.

If you are typically only using `docker run` to deploy your applications, then you could likely really benefit from using Docker Compose, Docker Swarm mode, or both Docker Compose and Swarm.

# Section 2: Configure Swarm Mode

Real-world applications are typically deployed across multiple hosts as discussed earlier. This improves application performance and availability, as well as allowing individual application components to scale independently. Docker has powerful native tools to help you do this.

An example of running things manually and on a single host would be to create a new container on **node1** by running `docker run -dt ubuntu sleep infinity`.

```bash
docker run -dt ubuntu sleep infinity
```

```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
d54efb8db41d: Pull complete
f8b845f45a87: Pull complete
e8db7bf7c39f: Pull complete
9654c40e9079: Pull complete
6d9ef359eaaa: Pull complete
Digest: sha256:dd7808d8792c9841d0b460122f1acf0a2dd1f56404f8d1e56298048885e45535
Status: Downloaded newer image for ubuntu:latest
846af8479944d406843c90a39cba68373c619d1feaa932719260a5f5afddbf71
```

This command will create a new container based on the `ubuntu:latest` image and will run the `sleep` command to keep the container running in the background. You can verify our example container is up by running `docker ps` on **node1**.

```bash
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
044bea1c2277        ubuntu              "sleep infinity"    2 seconds ago       Up 1 second                             distracted_mayer
```

But, this is only on a single node. What happens if this node goes down? Well, our application just dies and it is never restarted. To restore service, we would have to manually log into this machine, and start tweaking things to get it back up and running. So, it would be helpful if we had some type of system that would allow us to run this "sleep" application/service across many machines.

In this section you will configure _Swarm Mode_. This is a new optional mode in which multiple Docker hosts form a self-orchestrating group of engines called a _swarm_. Swarm mode enables new features such as _services_ and _bundles_ that help you deploy and manage multi-container apps across multiple Docker hosts.

You will complete the following:

- Configure _Swarm mode_
- Run the app
- Scale the app
- Drain nodes for maintenance and reschedule containers

For the remainder of this lab we will refer to _Docker native clustering_ as **_Swarm mode_**. The collection of Docker engines configured for Swarm mode will be referred to as the _swarm_.

A swarm comprises one or more _Manager Nodes_ and one or more _Worker Nodes_. The manager nodes maintain the state of swarm and schedule application containers. The worker nodes run the application containers. As of Docker 1.12, no external backend, or 3rd party components, are required for a fully functioning swarm - everything is built-in!

In this part of the demo you will use all three of the nodes in your lab. **node1** will be the Swarm manager, while **node2** and **node3** will be worker nodes. Swarm mode supports highly available redundant manager nodes, but for the purposes of this lab you will only deploy a single manager node.
