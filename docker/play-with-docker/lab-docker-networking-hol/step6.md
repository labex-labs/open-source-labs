# Overlay Networking

## Step 3: Create a service

Now that we have a Swarm initialized and an overlay network, it's time to create a service that uses the network.

Execute the following command from the first terminal to create a new service called _myservice_ on the _overnet_ network with two tasks/replicas.

```.term1
docker service create --name myservice \
--network overnet \
--replicas 2 \
ubuntu sleep infinity
```

```
ov30itv6t2n7axy2goqbfqt5e
```

Verify that the service is created and both replicas are up by running `docker service ls`.

```.term1
docker service ls
```

```
ID            NAME       MODE        REPLICAS  IMAGE
ov30itv6t2n7  myservice  replicated  2/2       ubuntu:latest
```

The `2/2` in the `REPLICAS` column shows that both tasks in the service are up and running.

Verify that a single task (replica) is running on each of the two nodes in the Swarm by running `docker service ps myservice`.

```.term1
docker service ps myservice
```

```
ID            NAME         IMAGE          NODE     DESIRED STATE  CURRENT STATE               ERROR  PORTS
riicggj5tuta  myservice.1  ubuntu:latest  node2  Running        Running about a minute ago
nlozn82wsttv  myservice.2  ubuntu:latest  node1  Running        Running about a minute ago
```

The `ID` and `NODE` values might be different in your output. The important thing to note is that each task/replica is running on a different node.

Now that the second node is running a task on the "overnet" network it will be able to see the "overnet" network. Lets run `docker network ls` from the second terminal to verify this.

```.term2
docker network ls
```

```
NETWORK ID          NAME                DRIVER              SCOPE
55f10b3fb8ed        bridge              bridge              local
b7b30433a639        docker_gwbridge     bridge              local
a7449465c379        host                host                local
8hq1n8nak54x        ingress             overlay             swarm
06c349b9cc77        none                null                local
wlqnvajmmzsk        overnet             overlay             swarm
```

We can also run `docker network inspect overnet` on the second terminal to get more detailed information about the "overnet" network and obtain the IP address of the task running on the second terminal.

```.term2
docker network inspect overnet
```

```
[
    {
        "Name": "overnet",
        "Id": "wlqnvajmmzskn84bqbdi1ytuy",
        "Created": "2017-04-04T09:35:47.526642642Z",
        "Scope": "swarm",
        "Driver": "overlay",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "10.0.0.0/24",
                    "Gateway": "10.0.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Containers": {
            "fbc8bb0834429a68b2ccef25d3c90135dbda41e08b300f07845cb7f082bcdf01": {
                "Name": "myservice.1.riicggj5tutar7h7sgsvqg72r",
                "EndpointID": "8edf83ebce77aed6d0193295c80c6aa7a5b76a08880a166002ecda3a2099bb6c",
                "MacAddress": "02:42:0a:00:00:03",
                "IPv4Address": "10.0.0.3/24",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.driver.overlay.vxlanid_list": "4097"
        },
        "Labels": {},
        "Peers": [
            {
                "Name": "node1-f6a6f8e18a9d",
                "IP": "10.0.0.5"
            },
            {
                "Name": "node2-507a763bed93",
                "IP": "10.0.0.6"
            }
        ]
    }
]
```

You should note that as of Docker 1.12, `docker network inspect` only shows containers/tasks running on the local node. This means that `10.0.0.3` is the IPv4 address of the container running on the second node. Make a note of this IP address for the next step (the IP address in your lab might be different than the one shown here in the lab guide).
