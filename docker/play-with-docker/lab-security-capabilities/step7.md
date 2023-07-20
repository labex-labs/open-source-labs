# Auditing

There are multiple ways to read out the capabilities from a file.

1. Using libcap:

   ```
   getcap $file

   $file = cap_net_raw+ep
   ```

2. Using libcap-ng:

   ```
   $ filecap /absolue/path/to/file
   ```

   ```
   file                     capabilities
   /absolute/path/to/file        net_raw
   ```

3. Using extended attributes (attr package):

   ```
   getfattr -n security.capability $file
   ```

   ```
   # file: $file
   security.capability=0sAQAAAgAgAAAAAAAAAAAAAAAAAAA=
   ```

## Tips

Docker images cannot have files with capability bits set. This reduces the risk of Docker containers using capabilities to escalate privileges. However, it is possible to mount volumes that contain files with capability bits set into containers. Therefore you should use caution if doing this.

1. You can audit directories for capability bits with the following commands:

```
# with libcap
getcap -r /

# with libcap-ng
filecap -a
```

2. To remove capability bits you can use.

```
# with libcap
setcap -r $file

# with libcap-ng
filecap /path/to/file none
```

## Further reading:

[This article](https://www.kernel.org/doc/ols/2008/ols2008v1-pages-163-172.pdf) explains capabilities in a lot of detail. It will help you understand how capability sets interact with each other, and is very useful if you plan to run privileged docker containers and manage capabilities manually inside of them.

[This is the man page for capabilities](http://man7.org/linux/man-pages/man7/capabilities.7.html). Most of the complex interactions between capability sets don't affect Docker containers as long as there are no files with capability bits set.
