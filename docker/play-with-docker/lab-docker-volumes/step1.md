# Data Persistency without a Volume

We will first illustrate how data is not persisted outside of a container by default.

Let's run an interactive shell within an `alpine` container named `c1`.

```bash
docker run --name c1 -it alpine sh
```

We will create the /data folder and a dummy `hello.txt` file in it.

```bash
mkdir /data && cd /data && touch hello.txt
```

We will then check how the read-write layer (container layer) is accessible from the host.

Let exit the container first.

```bash
exit
```

Let's inspect our container in order to get the location of the container's layer.
We can use the `inspect` command and then scroll into the output until the `GraphDriver` key, like the following.

```bash
docker inspect c1
```

Or we can directly use the Go template notation and get the content of the `GraphDriver` keys right away.

```bash
docker inspect -f "{{ json .GraphDriver }}" c1 | jq
```

You should then get an output like the following (the ID will not be the same though)

```
{
    "Data": {
        "LowerDir": "/var/lib/docker/overlay2/55922a6b646ba6681c5eca253a19e90270e3872329a239a82877b2f8c505c9a2-init/diff:/var/lib/docker/overlay2/30474f5fc34277d1d9e5ed5b48e2fb979eee9805a61a0b2c4bf33b766ba65a16/diff",
        "MergedDir": "/var/lib/docker/overlay2/55922a6b646ba6681c5eca253a19e90270e3872329a239a82877b2f8c505c9a2/merged",
        "UpperDir": "/var/lib/docker/overlay2/55922a6b646ba6681c5eca253a19e90270e3872329a239a82877b2f8c505c9a2/diff",
        "WorkDir": "/var/lib/docker/overlay2/55922a6b646ba6681c5eca253a19e90270e3872329a239a82877b2f8c505c9a2/work"
    },
    "Name": "overlay2"
}
```

From our host, if we inspect the folder which path is specified in `UpperDir`, we can see our `/data` and the `hello.txt` file we created are there.

Try the below command, to see the contents of the `/data` folder:

```
ls /var/lib/docker/overlay2/[YOUR_ID]/diff/data
```

What happen if we remove our `c1` container now ? Let's try.

```bash
docker rm c1
```

It seems the folder defined in the `UpperDir` above does not exist anymore. Do you confirm that ? Try running the `ls` command again and see the results.

This shows that data created in a container is not persisted. It's removed with the container's layer when the container is deleted.
