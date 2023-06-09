# ENTRYPOINT vs COMMAND

In the 2 previous Dockerfile, we used CMD to define the command to be ran when a container is launched. As we have seen, there are several ways to define the command, using ENTRYPOINT and/or CMD.
We will illustrate this on a new Dockerfile, named Dockerfile-v3, that as the following content.

```dockerfile
FROM alpine
ENTRYPOINT ["ping"]
CMD ["localhost"]
```

Here, we define the **ping** command as the ENTRYPOINT and the **localhost** as the CMD, the command that will be ran by default is the concatenation of ENTRYPOINT and CMD: **ping localhost**. This command can be seen as a wrapper around the **ping** utility to which we can change the address we provide as a parameter.

Let's create an image based on this new file.

```bash
docker image build -f Dockerfile-v3 -t ping:v0.1 .
```

We can run this image without specifying any command:

```bash
docker container run ping:v0.1
```

That should give a result like the following one.

```
PING localhost (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: seq=0 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: seq=1 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: seq=2 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: seq=3 ttl=64 time=0.046 ms
64 bytes from 127.0.0.1: seq=4 ttl=64 time=0.047 ms
```

You can also override the default CMD indicating another IP address. We will use **8.8.8.8** which is the IP of a Google's DNS.

```bash
docker container run ping:v0.1 8.8.8.8
```

That should return the following.

```
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=38 time=9.235 ms
64 bytes from 8.8.8.8: seq=1 ttl=38 time=8.590 ms
64 bytes from 8.8.8.8: seq=2 ttl=38 time=8.585 ms
```
