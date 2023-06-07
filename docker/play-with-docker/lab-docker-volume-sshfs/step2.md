# Setting up

First we install openssh and configure test user with password `testpassword` in the second node

```.term2
apk add --no-cache openssh
adduser -D test
echo "test:testpassword" | chpasswd
ssh-keygen -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
/usr/sbin/sshd
```

You can safely ignore any `Could not load host key` error messages.

Now, let's install the plugin and create a docker volume with it

```bash
mkdir /var/lib/docker/plugins # Shouldn't have to do this if graph folder is somewhere else
docker plugin install --grant-all-permissions vieux/sshfs
docker volume create -d vieux/sshfs -o sshcmd=test@node2:/home/test -o password=testpassword sshvolume
```

We can now use the plugin volume in a container as usual

```bash
docker run -it -v sshvolume:/test alpine sh -c 'echo "Hello world" > /test/somefile'
```

Now we check that the file has been created in the second node

```.term2
cat /home/test/somefile
```