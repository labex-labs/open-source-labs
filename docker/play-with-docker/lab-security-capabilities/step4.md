# Extra for experts

The remainder of this lab will show you additional tools for working with capabilities form the Linux shell.

There are two main sets of tools for managing capabilities:

- **libcap** focuses on manipulating capabilities.
- **libcap-ng** has some useful tools for auditing.

Below are some useful commands from both.

> You may need to manually install the packages required for some of these commands.

```

```

## **libcap**

- `capsh` - lets you perform capability testing and limited debugging
- `setcap` - set capability bits on a file
- `getcap` - get the capability bits from a file

## **libcap-ng**

- `pscap` - list the capabilities of running processes
- `filecap` - list the capabilities of files
- `captest` - test capabilities as well as list capabilities for current process

### Listing all capabilities

The following command will start a new container using Alpine Linux, install the `libcap` package and then list capabilities.

```bash
docker run --rm -it alpine sh -c 'apk add -U libcap; capsh --print'
```

```
(1/1) Installing libcap (2.25-r0)
Executing busybox-1.24.2-r9.trigger
OK: 5 MiB in 12 packages
Current: = cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap+eip
Bounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
uid=0(root)
gid=0(root)
groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```

**Current** is multiple sets separated by spaces. Multiple capabilities within the same set are separated by commas `,`. The letters following the `+` at the end of each set are as follows:

- `e` is effective
- `i` is inheritable
- `p` is permitted

For information on what these mean, see the [capabilities manpage](http://man7.org/linux/man-pages/man7/capabilities.7.html).
