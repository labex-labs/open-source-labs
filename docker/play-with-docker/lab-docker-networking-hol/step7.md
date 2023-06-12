# Overlay Networking

## Step 4: Test the network

To complete this step you will need the IP address of the service task running on **node2** that you saw in the previous step (`10.0.0.3`).

Execute the following commands from the first terminal.

```.term1
docker network inspect overnet
```

```
[
    {
        "Name": "overnet",
        "Id": "wlqnvajmmzskn84bqbdi1ytuy",
        "Created": "2017-04-04T09:35:47.362263887Z",
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
            "d676496d18f76c34d3b79fbf6573a5672a81d725d7c8704b49b4f797f6426454": {
                "Name": "myservice.2.nlozn82wsttv75cs9vs3ju7vs",
                "EndpointID": "36638a55fcf4ada2989650d0dde193bc2f81e0e9e3c153d3e9d1d85e89a642e6",
                "MacAddress": "02:42:0a:00:00:04",
                "IPv4Address": "10.0.0.4/24",
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

Notice that the IP address listed for the service task (container) running is different to the IP address for the service task running on the second node. Note also that they are on the same "overnet" network.

Run a `docker ps` command to get the ID of the service task so that you can log in to it in the next step.

```.term1
docker ps
```

```
CONTAINER ID        IMAGE                                                                            COMMAND                  CREATED             STATUS              PORTS                           NAMES
d676496d18f7        ubuntu@sha256:dd7808d8792c9841d0b460122f1acf0a2dd1f56404f8d1e56298048885e45535   "sleep infinity"         10 minutes ago      Up 10 minutes                                       myservice.2.nlozn82wsttv75cs9vs3ju7vs
<Snip>
```

Log on to the service task. Be sure to use the container `ID` from your environment as it will be different from the example shown below. We can do this by running `docker exec -it <CONTAINER ID> /bin/bash`.

```
docker exec -it yourcontainerid /bin/bash
root@d676496d18f7:/#
```

Install the ping command and ping the service task running on the second node where it had a IP address of `10.0.0.3` from the `docker network inspect overnet` command.

```.term1
apt-get update && apt-get install -y iputils-ping
```

Now, lets ping `10.0.0.3`.

```
root@d676496d18f7:/# ping -c5 10.0.0.3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
^C
--- 10.0.0.3 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 2998ms
```

The output above shows that both tasks from the **myservice** service are on the same overlay network spanning both nodes and that they can use this network to communicate.
