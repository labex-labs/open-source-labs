# Introduction

seccomp is a sandboxing facility in the Linux kernel that acts like a firewall for system calls (syscalls). It uses Berkeley Packet Filter (BPF) rules to filter syscalls and control how they are handled. These filters can significantly limit a containers access to the Docker Host's Linux kernel - especially for simple containers/applications.
