# Introduction

In this lab, you will run your first Docker container.

Containers are just a process (or a group of processes) running in isolation. Isolation is achieved via linux namespaces, control groups (cgroups), seccomp and SELinux. Note that linux namespaces and control groups are built into the linux kernel! Other than the linux kernel itself, there is nothing special about containers.

What makes containers useful is the tooling that surrounds it. For these labs, we will be using Docker, which has been a widely adopted tool for using containers to build applications. Docker provides developers and operators with a friendly interface to build, ship and run containers on any environment with a Docker engine. Because Docker client requires a Docker engine, an alternative is to use [Podman](https://podman.io/), which is a deamonless container engine to develop, manage and run [OCI](https://opencontainers.org/) containers and is able to run containers as root or in rootless mode. For those reasons, we recommend Podman but because of adoption, this lab still uses Docker.

The first part of this lab, we will run our first container, and learn how to inspect it. We will be able to witness the namespace isolation that we acquire from the linux kernel.

After we run our first container, we will dive into other uses of containers. You can find many examples of these on the Docker Store, and we will run several different types of containers on the same host. This will allow us to see the benefit of isolation- where we can run multiple containers on the same host without conflicts.

We will be using a few Docker commands in this lab. For full documentation on available commands check out the [official documentation](https://docs.docker.com/).

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a <span class="text-green-600 dark:text-green-400">beginner</span> level lab with a <span class="text-green-600 dark:text-green-400">89%</span> completion rate. It has received a <span class="text-primary-600 dark:text-primary-400">92%</span> positive review rate from learners.
</div>
