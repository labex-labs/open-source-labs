# Bridge Networking

## The Basics

Every clean installation of Docker comes with a pre-built network called **bridge**. Verify this with the `docker network ls`.

```bash
docker network ls
```

```
NETWORK ID          NAME                DRIVER              SCOPE
3430ad6f20bf        bridge              bridge              local
a7449465c379        host                host                local
06c349b9cc77        none                null                local
```

The output above shows that the **bridge** network is associated with the _bridge_ driver. It's important to note that the network and the driver are connected, but they are not the same. In this example the network and the driver have the same name - but they are not the same thing!

The output above also shows that the **bridge** network is scoped locally. This means that the network only exists on this Docker host. This is true of all networks using the _bridge_ driver - the _bridge_ driver provides single-host networking.

All networks created with the _bridge_ driver are based on a Linux bridge (a.k.a. a virtual switch).

Install the `brctl` command and use it to list the Linux bridges on your Docker host. You can do this by running `sudo apt-get install bridge-utils`.

```bash
apk update
apk add bridge
```

Then, list the bridges on your Docker host, by running `brctl show`.

```bash
brctl show
```

```
bridge name	bridge id		STP enabled	interfaces
docker0		8000.024252ed52f7	no
```

The output above shows a single Linux bridge called **docker0**. This is the bridge that was automatically created for the **bridge** network. You can see that it has no interfaces currently connected to it.

You can also use the `ip a` command to view details of the **docker0** bridge.

```bash
ip a
```

```
<Snip>
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:52:ed:52:f7 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
```
