# Seccomp and Docker

Docker has used seccomp since version 1.10 of the Docker Engine.

Docker uses seccomp in _filter mode_ and has its own JSON-based DSL that allows you to define _profiles_ that compile down to seccomp filters. When you run a container it gets the default seccomp profile unless you override this by passing the `--security-opt` flag to the `docker run` command.

The following example command starts an interactive container based off the Alpine image and starts a shell process. It also applies the seccomp profile described by `<profile>.json` to it.

```
docker run -it --rm --security-opt seccomp=<profile>.json alpine sh ...
```

The above command sends the JSON file from the client to the daemon where it is compiled into a BPF program using a [thin Go wrapper around libseccomp](https://github.com/seccomp/libseccomp-golang).

Docker seccomp profiles operate using a whitelist approach that specifies allowed syscalls. _Only_ syscalls on the whitelist are permitted.

Docker supports many security related technologies. It is possible for other security related technologies to interfere with your testing of seccomp profiles. For this reason, the best way to test the effect of seccomp profiles is to add all _capabilities_ and disable _apparmor_. This gives you the confidence the behavior you see in the following steps is solely due to seccomp changes.

The following `docker run` flags add all _capabilities_ and disable _apparmor_: `--cap-add ALL --security-opt apparmor=unconfined`.

# Step 1: Clone the labs GitHub repo

In this step you will clone the lab's GitHub repo so that you have the seccomp profiles that you will use for the remainder of this lab.

1. Clone the labs GitHub repo.

   ```bash
   git clone https://github.com/docker/labs
   ```

2. Change into the `labs/security/seccomp` directory.

   ```bash
   cd labs/security/seccomp
   ```

The remaining steps in this lab will assume that you are running commands from this `labs/security/seccomp` directory. This will be important when referencing the seccomp profiles on the various `docker run` commands throughout the lab.

# Step 2: Test a seccomp profile

In this step you will use the `deny.json` seccomp profile included the lab guides repo. This profile has an empty syscall whitelist meaning all syscalls will be blocked. As part of the demo you will add all _capabilities_ and effectively disable _apparmor_ so that you know that only your seccomp profile is preventing the syscalls.

1. Use the `docker run` command to try to start a new container with all capabilities added, apparmor unconfined, and the `seccomp-profiles/deny.json` seccomp profile applied.

   ```bash
   docker run --rm -it --cap-add ALL --security-opt apparmor=unconfined --security-opt seccomp=seccomp-profiles/deny.json alpine sh
   ```

   ```
   docker: Error response from daemon: cannot start a stopped process: unknown.
   ```

In this scenario, Docker doesn't actually have enough syscalls to start the container!

2. Inspect the contents of the `seccomp-profiles/deny.json` profile.

   ```bash
   cat seccomp-profiles/deny.json
   ```

   ```
   {
        "defaultAction": "SCMP_ACT_ERRNO",
        "architectures": [
                "SCMP_ARCH_X86_64",
                "SCMP_ARCH_X86",
                "SCMP_ARCH_X32"
        ],
        "syscalls": [
        ]
   }
   ```

   Notice that there are no **syscalls** in the whitelist. This means that no syscalls will be allowed from containers started with this profile.

In this step you removed _capabilities_ and _apparmor_ from interfering, and started a new container with a seccomp profile that had no syscalls in its whitelist. You saw how this prevented all syscalls from within the container or to let it start in the first place.

# Step 3: Run a container with no seccomp profile

Unless you specify a different profile, Docker will apply the [default seccomp profile](https://github.com/docker/docker/blob/master/profiles/seccomp/default.json) to all new containers. In this step you will see how to force a new container to run without a seccomp profile.

1. Start a new container with the `--security-opt seccomp=unconfined` flag so that no seccomp profile is applied to it.

   ```bash
   docker run --rm -it --security-opt seccomp=unconfined debian:jessie sh
   ```

2. From the terminal of the container run a `whoami` command to confirm that the container works and can make syscalls back to the Docker Host.

   ```bash
   whoami
   ```

   ```
   root
   ```

3. To prove that we are not running with the default seccomp profile, try running a `unshare` command, which runs a shell process in a new namespace:

```bash
unshare --map-root-user --user
whoami
```

```
root
```

4. Exit the new shell and the container.

```bash
exit
exit
```

5. Run the following `strace` command from your Docker Host to see a list of the syscalls used by the `whoami` program.

   Your Docker Host will need the `strace` package installed.

   ```bash
   apk add --update strace
   strace -c -f -S name whoami 2>&1 1>/dev/null | tail -n +3 | head -n -2 | awk '{print $(NF)}'
   ```

   ```
   access
   arch_prctl
   brk
   close
   connect
   execve
   <SNIP>
   socket
   write
   ```

You can also run the following simpler command and get a more verbose output.

```bash
strace whoami
```

```
execve("/usr/bin/whoami", ["whoami", "-qq"], [/* 21 vars */]) = 0
brk(0)                                  = 0x1980000
<SNIP>
```

You can substitute **whoami** for any other program.

In this step you started a new container with no seccomp profile and verified that the `whoami` program could execute. You also used the `strace` program to list the syscalls made by a particular run of the `whoami` program.

# Step 4: Selectively remove syscalls

In this step you will see how applying changes to the `default.json` profile can be a good way to fine-tune which syscalls are available to containers.

The `default-no-chmod.json` profile is a modification of the `default.json` profile with the `chmod()`, `fchmod()`, and `chmodat()` syscalls removed from its whitelist.

1. Start a new container with the `default-no-chmod.json` profile and attempt to run the `chmod 777 / -v` command.

   ```bash
   docker run --rm -it --security-opt seccomp=./seccomp-profiles/default-no-chmod.json alpine sh
   ```

   and then from inside the container:

   ```bash
   chmod 777 / -v
   ```

   ```
   chmod: /: Operation not permitted
   ```

The command fails because the `chmod 777 / -v` command uses some of the `chmod()`, `fchmod()`, and `chmodat()` syscalls that have been removed from the whitelist of the `default-no-chmod.json` profile.

2. Exit the container.

```bash
exit
```

3. Start another new container with the `default.json` profile and run the same `chmod 777 / -v`.

   ```bash
   docker run --rm -it --security-opt seccomp=./seccomp-profiles/default.json alpine sh
   ```

   and then from inside the container:

   ```bash
   chmod 777 / -v
   ```

   ```
   mode of '/' changed to 0777 (rwxrwxrwx)
   ```

The command succeeds this time because the `default.json` profile has the `chmod()`, `fchmod()`, and `chmodat` syscalls included in its whitelist.

4. Exit the container.

```bash
exit
```

5. Check both profiles for the presence of the `chmod()`, `fchmod()`, and `chmodat()` syscalls.

   Be sure to perform these commands from the command line of your Docker Host and not from inside of the container created in the previous step.

   ```bash
   cat ./seccomp-profiles/default.json | grep chmod
   ```

   ```
   "name": "chmod",
   "name": "fchmod",
   "name": "fchmodat",
   ```

   ```bash
   cat ./seccomp-profiles/default-no-chmod.json | grep chmod
   ```

   The output above shows that the `default-no-chmod.json` profile contains no **chmod** related syscalls in the whitelist.

In this step you saw how removing particular syscalls from the `default.json` profile can be a powerful way to start fine tuning the security of your containers.

# Step 5: Write a seccomp profile

It is possible to write Docker seccomp profiles from scratch. You can also edit existing profiles. In this step you will learn about the syntax and behavior of Docker seccomp profiles.

The layout of a Docker seccomp profile looks like the following:

```
{
    "defaultAction": "SCMP_ACT_ERRNO",
    "architectures": [
        "SCMP_ARCH_X86_64",
        "SCMP_ARCH_X86",
        "SCMP_ARCH_X32"
    ],
    "syscalls": [
        {
            "name": "accept",
            "action": "SCMP_ACT_ALLOW",
            "args": []
        },
        {
            "name": "accept4",
            "action": "SCMP_ACT_ALLOW",
            "args": []
        },
        ...
    ]
}
```

The most authoritative source for how to write Docker seccomp profiles is the structs used to deserialize the JSON.

- [https://github.com/docker/engine-api/blob/c15549e10366236b069e50ef26562fb24f5911d4/types/seccomp.go](https://github.com/docker/engine-api/blob/c15549e10366236b069e50ef26562fb24f5911d4/types/seccomp.go)
- [https://github.com/opencontainers/runtime-spec/blob/6be516e2237a6dd377408e455ac8b41faf48bdf6/specs-go/config.go#L502](https://github.com/opencontainers/runtime-spec/blob/6be516e2237a6dd377408e455ac8b41faf48bdf6/specs-go/config.go#L502)

The table below lists the possible _actions_ in order of precedence. Higher actions overrule lower actions.

| Action         | Description                                                     |
|