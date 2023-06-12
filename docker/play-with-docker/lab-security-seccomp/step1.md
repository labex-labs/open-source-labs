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
