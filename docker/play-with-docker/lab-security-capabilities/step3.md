# **libcap-ng**

* `pscap` - list the capabilities of running processes
* `filecap` - list the capabilities of files
* `captest` - test capabilities as well as list capabilities for current process

The remainder of this step will show you some examples of `libcap` and `libcap-ng`.

### Listing all capabilities

The following command will start a new container using Alpine Linux, install the `libcap` package and then list capabilities.

```bash
 docker run --rm -it alpine sh -c 'apk add -U libcap; capsh --print'
````

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

### Experimenting with capabilities

The `capsh` command can be useful for experimenting with capabilities. `capsh --help` shows how to use the command:

```bash
docker run --rm -it alpine sh -c 'apk add -U libcap;capsh --help'
```

```
fetch http://dl-cdn.alpinelinux.org/alpine/v3.5/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.5/community/x86_64/APKINDEX.ta
r.gz
(1/1) Installing libcap (2.25-r1)
Executing busybox-1.25.1-r0.trigger
OK: 4 MiB in 12 packages
usage: capsh [args ...]
  --help         this message (or try 'man capsh')
  --print        display capability relevant state
  --decode=xxx   decode a hex string to a list of caps
  --supports=xxx exit 1 if capability xxx unsupported
  --drop=xxx     remove xxx,.. capabilities from bset
  --caps=xxx     set caps as per cap_from_text()
  --inh=xxx      set xxx,.. inheritiable set
  --secbits=<n>  write a new value for securebits
  --keep=<n>     set keep-capabability bit to <n>
  --uid=<n>      set uid to <n> (hint: id <username>)
  --gid=<n>      set gid to <n> (hint: id <username>)
  --groups=g,... set the supplemental groups
  --user=<name>  set uid,gid and groups to that of user
  --chroot=path  chroot(2) to this path
  --killit=<n>   send signal(n) to child
  --forkfor=<n>  fork and make child sleep for <n> sec
  ==             re-exec(capsh) with args as for --
  --             remaing arguments are for /bin/bash
                 (without -- [capsh] will simply exit(0))
```

> Warning:
> `--drop` sounds like what you want to do, but it only affects the bounding set. This can be very confusing because it doesn't actually take away the capability from the effective or inheritable set. You almost always want to use `--caps`.

### Modifying capabilities

Libcap and libcap-ng can both be used to modify capabilities.

1. Use libcap to modify the capabilities on a file.

   The command below shows how to set the CAP_NET_RAW capability as _effective_ and _permitted_ on the file represented by `$file`. The `setcap` command calls on libcap to do this.

   ```
   setcap cap_net_raw=ep $file
   ```

2. Use libcap-ng to set the capabilities of a file.

   The `filecap` command calls on libcap-ng.

   ```
   filecap /absolute/path net_raw
   ```

   **Note:** `filecap` requires absolute path names. Shortcuts like `./` are not permitted.

### Auditing

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

### Tips

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

### Further reading:

[This article](https://www.kernel.org/doc/ols/2008/ols2008v1-pages-163-172.pdf) explains capabilities in a lot of detail. It will help you understand how capability sets interact with each other, and is very useful if you plan to run privileged docker containers and manage capabilities manually inside of them.

[This is the man page for capabilities](http://man7.org/linux/man-pages/man7/capabilities.7.html). Most of the complex interactions between capability sets don't affect Docker containers as long as there are no files with capability bits set.