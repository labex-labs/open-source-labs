# Seccomp and Docker

Docker has used seccomp since version 1.10 of the Docker Engine.

Docker uses seccomp in _filter mode_ and has its own JSON-based DSL that allows you to define _profiles_ that compile down to seccomp filters. When you run a container it gets the default seccomp profile unless you override this by passing the `--security-opt` flag to the `docker run` command.

The following example command starts an interactive container based off the Alpine image and starts a shell process. It also applies the seccomp profile described by `<profile>.json` to it.

```bash
docker run -it --rm --security-opt seccomp= alpine sh ... < profile > .json
```

The above command sends the JSON file from the client to the daemon where it is compiled into a BPF program using a [thin Go wrapper around libseccomp](https://github.com/seccomp/libseccomp-golang).

Docker seccomp profiles operate using a whitelist approach that specifies allowed syscalls. _Only_ syscalls on the whitelist are permitted.

Docker supports many security related technologies. It is possible for other security related technologies to interfere with your testing of seccomp profiles. For this reason, the best way to test the effect of seccomp profiles is to add all _capabilities_ and disable _apparmor_. This gives you the confidence the behavior you see in the following steps is solely due to seccomp changes.

The following `docker run` flags add all _capabilities_ and disable _apparmor_: `--cap-add ALL --security-opt apparmor=unconfined`.
