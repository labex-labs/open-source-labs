# Defining a volume at runtime

We have seen volume defined in a Dockerfile, we will see they can also be defined at runtime using the **-v** flag of the **docker container run** command.

Let's create a container from the alpine image, we'll use the -d option so it runs in background and also define a volume on /data as we've done previously.
In order the PID 1 process remains active, we use the following command that pings Google DNS and log the output in a file within the /data folder.

```
ping 8.8.8.8 > /data/ping.txt
```

The container is ran that way:

```bash
docker container run --name c3 -d -v /data alpine sh -c 'ping 8.8.8.8 > /data/ping.txt'
```

Let's inspect the container and get the **Mounts** key using the Go template notation.

```bash
docker container inspect -f "{{ "{{ json .Mounts "}}}}" c3 | jq
```

We have pretty much the same output as we had when we defined the volume in the Dockerfile.

```
[
  {
    "Type": "volume",
    "Name": "af621cde2717307e5bf91be850c5a00474d58b8cdc8d6e37f2e373631c2f1331",
    "Source": "/var/lib/docker/volumes/af621cde2717307e5bf91be850c5a00474d58b8cdc8d6e37f2e373631c2f1331/_data",
    "Destination": "/data",
    "Driver": "local",
    "Mode": "",
    "RW": true,
    "Propagation": ""
  }
]
```

If we use the folder defined in the **Source** key, and check the content of the ping.txt within the /data folder, we get something similar to the following.

```
tail -f /var/lib/docker/volumes/OUR_ID/_data/ping.txt
64 bytes from 8.8.8.8: seq=34 ttl=37 time=0.462 ms
64 bytes from 8.8.8.8: seq=35 ttl=37 time=0.436 ms
64 bytes from 8.8.8.8: seq=36 ttl=37 time=0.512 ms
64 bytes from 8.8.8.8: seq=37 ttl=37 time=0.487 ms
64 bytes from 8.8.8.8: seq=38 ttl=37 time=0.409 ms
64 bytes from 8.8.8.8: seq=39 ttl=37 time=0.438 ms
64 bytes from 8.8.8.8: seq=40 ttl=37 time=0.477 ms
...
```

The ping.txt file is updated regularly by the command running in the **c3** container.

Stopping and removing the container will obviously stop the ping command but the /data/ping.txt file will still be there. Give it a try :)
