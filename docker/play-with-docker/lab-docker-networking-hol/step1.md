# Networking Basics

## Step 1: The Docker Network Command

The `docker network` command is the main command for configuring and managing container networks. Run the `docker network` command from the first terminal.

```bash
docker network
```

```

Usage:	docker network COMMAND

Manage networks

Options:
      --help   Print usage

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
```

The command output shows how to use the command as well as all of the `docker network` sub-commands. As you can see from the output, the `docker network` command allows you to create new networks, list existing networks, inspect networks, and remove networks. It also allows you to connect and disconnect containers from networks.

## Step 2: List networks

Run a `docker network ls` command to view existing container networks on the current Docker host.

```bash
docker network ls
```

```
NETWORK ID          NAME                DRIVER              SCOPE
3430ad6f20bf        bridge              bridge              local
a7449465c379        host                host                local
06c349b9cc77        none                null                local
```

The output above shows the container networks that are created as part of a standard installation of Docker.

New networks that you create will also show up in the output of the `docker network ls` command.

You can see that each network gets a unique `ID` and `NAME`. Each network is also associated with a single driver. Notice that the "bridge" network and the "host" network have the same name as their respective drivers.
