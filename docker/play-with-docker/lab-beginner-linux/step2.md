# Run a single task in an Alpine Linux container

In this step we're going to start a new container and tell it to run the `hostname` command. The container will start, execute the `hostname` command, then exit.

1. Run the following command in your Linux console.

   ```bash
   docker container run alpine hostname
   ```

   The output below shows that the `alpine:latest` image could not be found locally. When this happens, Docker automatically _pulls_ it from Docker Hub.

   After the image is pulled, the container's hostname is displayed (`888e89a3b36b` in the example below).

   ```
   Unable to find image 'alpine:latest' locally
   latest: Pulling from library/alpine
   88286f41530e: Pull complete
   Digest: sha256:f006ecbb824d87947d0b51ab8488634bf69fe4094959d935c0c103f4820a417d
   Status: Downloaded newer image for alpine:latest
   888e89a3b36b
   ```

2. Docker keeps a container running as long as the process it started inside the container is still running. In this case the `hostname` process exits as soon as the output is written. This means the container stops. However, Docker doesn't delete resources by default, so the container still exists in the `Exited` state.

   List all containers.

   ```bash
   docker container ls --all
   ```

   Notice that your Alpine Linux container is in the `Exited` state.

   ```
   CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS            PORTS               NAMES
   888e89a3b36b        alpine              "hostname"          50 seconds ago      Exited (0) 49 seconds ago                       awesome_elion
   ```

   > **Note:** The container ID _is_ the hostname that the container displayed. In the example above it's `888e89a3b36b`.

Containers which do one task and then exit can be very useful. You could build a Docker image that executes a script to configure something. Anyone can execute that task just by running the container - they don't need the actual scripts or configuration information.
