# A few gotchas

The remainder of this lab will walk you through a few things that are easy to miss when using seccomp with Docker.

## Timing of a seccomp profile application

In versions of Docker prior to 1.12, seccomp polices tended to be applied very early in the container creation process. This resulted in you needing to add syscalls to your profile that were required for the container creation process but not required by your container. This was not ideal. See:

- [https://github.com/docker/docker/issues/22252](https://github.com/docker/docker/issues/22252)
- [https://github.com/opencontainers/runc/pull/789](https://github.com/opencontainers/runc/pull/789)

A good way to avoid this issue in Docker 1.12+ can be to use the `--security-opt no-new-privileges` flag when starting your container. However, this will also prevent you from gaining privileges through `setuid` binaries.

## Truncation

When writing a seccomp filter, there may be unused or randomly set bits on 32-bit arguments when using a 64-bit operating system after the filter has run.

> When checking values from args against a blacklist, keep in mind that
> arguments are often silently truncated before being processed, but
> after the seccomp check. For example, this happens if the i386 ABI
> is used on an x86-64 kernel: although the kernel will normally not
> look beyond the 32 lowest bits of the arguments, the values of the
> full 64-bit registers will be present in the seccomp data. A less
> surprising example is that if the x86-64 ABI is used to perform a
> system call that takes an argument of type int, the more-significant
> half of the argument register is ignored by the system call, but
> visible in the seccomp data.

[https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt)

## seccomp escapes

Syscall numbers are architecture dependent. This limits the portability of BPF filters. Fortunately Docker profiles abstract this issue away, so you don't need to worry about it if using Docker seccomp profiles.

`ptrace` is disabled by default and you should avoid enabling it. This is because it allows bypassing of seccomp. You can use [this script](https://gist.github.com/thejh/8346f47e359adecd1d53) to test for seccomp escapes through `ptrace`.

## Differences between Docker versions

- Seccomp is supported as of Docker 1.10.

- Using the `--privileged` flag when creating a container with `docker run` disables seccomp in all versions of docker - even if you explicitly specify a seccomp profile. In general you should avoid using the `--privileged` flag as it does too many things. You can achieve the same goal with `--cap-add ALL --security-opt apparmor=unconfined --security-opt seccomp=unconfined`. If you need access to devices use `-ice`.

- In docker 1.10-1.12 `docker exec --privileged` does not bypass seccomp. This may change in future versions (see [https://github.com/docker/docker/issues/21984](https://github.com/docker/docker/issues/21984)).

- In docker 1.12 and later, adding a capability may enable some appropriate system calls in the default seccomp profile. However, it does not disable apparmor.

## Using multiple filters

The only way to use multiple seccomp filters, as of Docker 1.12, is to load additional filters within your program at runtime. The kernel supports layering filters.

When using multiple layered filters, all filters are always executed starting with the most recently added. The highest precedence action returned is taken. See the man page for all the details: [http://man7.org/linux/man-pages/man2/seccomp.2.html](http://man7.org/linux/man-pages/man2/seccomp.2.html).

## Misc

There is no easy way to use seccomp in a mode that reports errors without crashing the program. However, there are several round-about ways to accomplish this. One such way is to use SCMP_ACT_TRAP and write your code to handle SIGSYS and report the errors in a useful way. Here is some information on [how Firefox handles seccomp violations](https://wiki.mozilla.org/Security/Sandbox/Seccomp).

## Further reading:

- Very comprehensive presentation about seccomp that goes into more detail than this document.
  - Article: [https://lwn.net/Articles/656307/](https://lwn.net/Articles/656307/)
  - Slides: [http://man7.org/conf/lpc2015/limiting_kernel_attack_surface_with_seccomp-LPC_2015-Kerrisk.pdf](http://man7.org/conf/lpc2015/limiting_kernel_attack_surface_with_seccomp-LPC_2015-Kerrisk.pdf)
- Chrome's DSL for generating seccomp BPF programs:
  [https://cs.chromium.org/chromium/src/sandbox/linux/bpf_dsl/bpf_dsl.h?sq=package:chromium&dr=CSs](https://cs.chromium.org/chromium/src/sandbox/linux/bpf_dsl/bpf_dsl.h?sq=package:chromium&dr=CSs)
