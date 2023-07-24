# Working with Docker and capabilities

In this step you'll learn the basic approach to managing capabilities with Docker. You'll also learn the Docker commands used to manage capabilities for a container's root account.

As of Docker 1.12 you have 3 high level options for using capabilities:

1. Run containers as root with a large set of capabilities and try to manage capabilities within your container manually.
2. Run containers as root with limited capabilities and never change them within a container.
3. Run containers as an unprivileged user with no capabilities.

Option 2 as the most realistic as of Docker 1.12. Option 3 would be ideal but not realistic. Option 1 should be avoided wherever possible.

> **Note:** Another option may be added in future versions of Docker that will allow you to run containers as a non-root user with added capabilities. The correct way of doing this requires _ambient capabilities_ which was added to the Linux kernel in version 4.3. Whether it is possible for Docker to approximate this behavior in older kernels requires more research.

In the following commands, `$CAP` will be used to indicate one or more individual capabilities. We'll test these out in the next section.

1. To drop capabilities from the `root` account of a container.

   ```
   docker run --rm -it --cap-drop $CAP alpine sh
   ```

2. To add capabilities to the `root` account of a container.

   ```
   docker run --rm -it --cap-add $CAP alpine sh
   ```

3. To drop all capabilities and then explicitly add individual capabilities to the `root` account of a container.

   ```
   docker run --rm -it --cap-drop ALL --cap-add $CAP alpine sh
   ```

The Linux kernel prefixes all capability constants with "CAP*". For example, CAP_CHOWN, CAP_NET_ADMIN, CAP_SETUID, CAP_SYSADMIN etc. Docker capability constants are not prefixed with "CAP*" but otherwise match the kernel's constants.

For more information on capabilities, including a full list, see the [capabilities man page](http://man7.org/linux/man-pages/man7/capabilities.7.html)
