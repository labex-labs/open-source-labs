# Experimenting with capabilities

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
