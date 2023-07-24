# Defining a volume in a Dockerfile

We will now see how volumes come into the picture to handle the data persistency.

We will start by creating a Dockerfile based on alpine and define the /data as a volume.
This means that anything written by a container in /data will be persisted outside of the Union filesystem.

Create a Dockerfile with the following content

```dockerfile
FROM alpine
VOLUME ["/data"]
ENTRYPOINT ["/bin/sh"]
```

Note: we specify **/bin/sh** as the ENTRYPOINT so that if no command is provided in interactive mode we will end up in a shell inside our container.

Let's build an image from this Dockerfile.

```bash
docker image build -t img1 .
```

We will then create a container in interactive mode (using -ti flags) from this image and name it c2.

```bash
docker container run --name c2 -ti img1
```

We should then end up in a shell within the container. From there, we will go into /data and create a hello.txt file.

```bash
cd /data
touch hello.txt
ls
```

Let's exit the container making sure it remains running: use the Control-P / Control-Q combination for this.
Use the following command to make sure it's still running.

```bash
docker container ls
```

Note: the container, named c2, should be listed there.

We will now inspect this container in order to get the location of the volume (defined on /data) on the host.
We can use the inspect command and then scroll into the output until we find the **Mounts** key...

```bash
docker container inspect c2
```

Or we can directly use the Go template notation and get the content of the **Mounts** keys right away.

```bash
docker container inspect -f "{{ "{{ json .Mounts "}}}}" c2 | jq
```

You should then get an output like the following (the ID will not be the same though)

```
[
    {
        "Destination": "/data",
        "Driver": "local",
        "Mode": "",
        "Name": "2f5b7c6b77494934293fc7a09198dd3c20406f05272121728632a4aab545401c",
        "Propagation": "",
        "RW": true,
        "Source": "/var/lib/docker/volumes/2f5b7c6b77494934293fc7a09198dd3c20406f05272121728632a4aab545401c/_data",
        "Type": "volume"
    }
]
```

This output shows that the volume defined in /data is stored in **/var/lib/docker/volumes/2f5...01c/\_data** on the host (removing part of the ID for a better readability).

Copy your own path (the one under the **Source** key) and make sure the **hello.txt** file we created (from within the container) is there.

We now remove the c2 container.

```bash
docker container stop c2 && docker container rm c2
```

Check that the folder defined under the **Source** key is still there and contains **hello.txt** file.

From the above, we can see that a volume bypasses the union filesystem and is not dependent on a container's lifecycle.
