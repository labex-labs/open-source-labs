# Lab: Capabilities

> **Difficulty**: Advanced

> **Time**: Approximately 30 minutes

In this lab you'll learn the basics of capabilities in the Linux kernel. You'll learn how they work with Docker, some basic commands to view and manage them, as well as how to add and remove capabilities in new containers.

You will complete the following steps as part of this lab.

- [Step 1 - Introduction to capabilities](#cap_intro)
- [Step 2 - Working with Docker and capabilities](#docker_cap)
- [Step 3 - Testing Docker capabilities](#test_docker)
- [Step 4 - Extra for experts](#extra)

# Step 1: Introduction to capabilities

In this step you'll learn the basics of capabilities.

The Linux kernel is able to break down the privileges of the `root` user into distinct units referred to as **capabilities**. For example, the CAP_CHOWN capability is what allows the root user to make arbitrary changes to file UIDs and GIDs. The CAP_DAC_OVERRIDE capability allows the root user to bypass kernel permission checks on file read, write and execute operations. Almost all of the special powers associated with the Linux root user are broken down into individual capabilities.

This breaking down of root privileges into granular capabilities allows you to:

1. Remove individual capabilities from the `root` user account, making it less powerful/dangerous.
2. Add privileges to non-root users at a very granular level.

Capabilities apply to both files and threads. File capabilities allow users to execute programs with higher privileges. This is similar to the way the `setuid` bit works. Thread capabilities keep track of the current state of capabilities in running programs.

The Linux kernel lets you set capability _bounding sets_ that impose limits on the capabilities that a file/thread can gain.

Docker imposes certain limitations that make working with capabilities much simpler. For example, file capabilities are stored within a file's extended attributes, and extended attributes are stripped out when Docker images are built. This means you will not normally have to concern yourself too much with file capabilities in containers.

> It is of course possible to get file capabilities into containers at runtime, however this is not recommended.

In an environment without file based capabilities, it's not possible for applications to escalate their privileges beyond the _bounding set_ (a set beyond which capabilities cannot grow). Docker sets the _bounding set_ before starting a container. You can use Docker commands to add or remove capabilities to or from the _bounding set_.

By default, Docker drops all capabilities except [those needed](https://github.com/moby/moby/blob/5f17312653c3e4dc5474f86692b09f06262a1ebd/oci/defaults.go#L14-L31), using a whitelist approach.

# Step 2: Working with Docker and capabilities

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

# Step 3: Testing Docker capabilities

In this step you will start various new containers. Each time you will use the commands learned in the previous step to tweak the capabilities associated with the account used to run the container.

1. Start a new container and prove that the container's root account can change the ownership of files.

   ```bash
    docker run --rm -it alpine chown nobody /
   ```

   The command gives no return code indicating that the operation succeeded. The command works because the default behavior is for new containers to be started with a root user. This root user has the CAP_CHOWN capability by default.

2. Start another new container and drop all capabilities for the containers root account other than the CAP_CHOWN capability. Remember that Docker does not use the "CAP\_" prefix when addressing capability constants.

   ```bash
    docker run --rm -it --cap-drop ALL --cap-add CHOWN alpine chown nobody /
   ```

   This command also gives no return code, indicating a successful run. The operation succeeds because although you dropped all capabilities for the container's `root` account, you added the `chown` capability back. The `chown` capability is all that is needed to change the ownership of a file.

3. Start another new container and drop only the `CHOWN` capability form its root account.

   ```bash
    docker run --rm -it --cap-drop CHOWN alpine chown nobody /
   ```

   ```
    chown: /: Operation not permitted
   ```

   This time the command returns an error code indicating it failed. This is because the container's root account does not have the `CHOWN` capability and therefore cannot change the ownership of a file or directory.

4. Create another new container and try adding the `CHOWN` capability to the non-root user called `nobody`. As part of the same command try and change the ownership of a file or folder.

   ```bash
    docker run --rm -it --cap-add chown -u nobody alpine chown nobody /
   ```

```

```

chown: /: Operation not permitted

```

The above command fails because Docker does not yet support adding capabilities to non-root users.

In this step you have added and removed capabilities to a range of new containers. You have seen that capabilities can be added and removed from the root user of a container at a very granular level. You also learned that Docker does not currently support adding capabilities to non-root users.

# Step 4: Extra for experts

The remainder of this lab will show you additional tools for working with capabilities form the Linux shell.

There are two main sets of tools for managing capabilities:
- **libcap** focuses on manipulating capabilities.
- **libcap-ng** has some useful tools for auditing.

Below are some useful commands from both.

> You may need to manually install the packages required for some of these commands.
```
