# Lab: Seccomp

> **Difficulty**: Advanced

> **Time**: Approximately 20 minutes

seccomp is a sandboxing facility in the Linux kernel that acts like a firewall for system calls (syscalls). It uses Berkeley Packet Filter (BPF) rules to filter syscalls and control how they are handled. These filters can significantly limit a containers access to the Docker Host's Linux kernel - especially for simple containers/applications.

You will complete the following steps as part of this lab.

- [Step 1 - Clone the labs GitHub repo](#clone)
- [Step 2 - Test a seccomp profile](#test)
- [Step 3 - Run a container with no seccomp profile](#no-default)
- [Step 4 - Selectively remove syscalls](#chmod)
- [Step 5 - Write a seccomp profile](#write)
- [Step 6 - A few Gotchas](#gotchas)

# Prerequisites

With this lab in Play With Docker you have all you need to complete the lab. If you are running this on another environment, you will need:

- A Linux-based Docker Host with seccomp enabled
- Docker 1.10 or higher (preferably 1.12 or higher)

The following commands show you how to check if seccomp is enabled in your system's kernel:

Check from Docker 1.12 or higher

```
$ docker info | grep seccomp
Security Options: apparmor seccomp
```

If the above output does not return a line with `seccomp` then your system does not have seccomp enabled in its kernel.

Check from the Linux command line

```
$ grep SECCOMP /boot/config-$(uname -r)
CONFIG_HAVE_ARCH_SECCOMP_FILTER=y
CONFIG_SECCOMP_FILTER=y
CONFIG_SECCOMP=y
```
