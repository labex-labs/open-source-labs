# Write a seccomp profile

It is possible to write Docker seccomp profiles from scratch. You can also edit existing profiles. In this step you will learn about the syntax and behavior of Docker seccomp profiles.

The layout of a Docker seccomp profile looks like the following:

```json
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
| -------------- | --------------------------------------------------------------- |
| SCMP_ACT_KILL  | Kill with a exit status of `0x80 + 31 (SIGSYS) = 159`           |
| SCMP_ACT_TRAP  | Send a `SIGSYS` signal without executing the system call        |
| SCMP_ACT_ERRNO | Set `errno` without executing the system call                   |
| SCMP_ACT_TRACE | Invoke a ptracer to make a decision or set `errno` to `-ENOSYS` |
| SCMP_ACT_ALLOW | Allow                                                           |

The most important actions for Docker users are `SCMP_ACT_ERRNO` and `SCMP_ACT_ALLOW`.

Profiles can contain more granular filters based on the value of the arguments to the system call.

```json
{
    ...
    "syscalls": [
        {
            "name": "accept",
            "action": "SCMP_ACT_ALLOW",
            "args": [
                {
                    "index": 0,
                    "op": "SCMP_CMP_MASKED_EQ",
                    "value": 2080505856,
                    "valueTwo": 0
                }
            ]
        }
    ]
}
```

- `index` is the index of the system call argument
- `op` is the operation to perform on the argument. It can be one of:
  - SCMP_CMP_NE - not equal
  - SCMP_CMP_LT - less than
  - SCMP_CMP_LE - less than or equal to
  - SCMP_CMP_EQ - equal to
  - SCMP_CMP_GE - greater or equal to
  - SCMP_CMP_GT - greater than
  - SCMP_CMP_MASKED_EQ - masked equal: true if `(value & arg == valueTwo)`
- `value` is a parameter for the operation
- `valueTwo` is used only for SCMP_CMP_MASKED_EQ

The rule only matches if **all** args match. Add multiple rules to achieve the effect of an OR.

`strace` can be used to get a list of all system calls made by a program.
It's a very good starting point for writing seccomp policies.
Here's an example of how we can list all system calls made by `ls`:

```.term1
strace -c -f -S name ls 2>&1 1>/dev/null | tail -n +3 | head -n -2 | awk '{print $(NF)}'
```

```
access
arch_prctl
brk
close
execve
<SNIP>
statfs
write
```

The output above shows the syscalls that will need to be enabled for a container running the `ls` program to work, in addition to the syscalls required to start a container.

In this step you learned the format and syntax of Docker seccomp profiles. You also learned the order of preference for actions, as well as how to determine the syscalls needed by an individual program.
