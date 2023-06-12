# Introduction to capabilities

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
