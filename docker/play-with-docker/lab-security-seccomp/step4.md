# Test a seccomp profile

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
