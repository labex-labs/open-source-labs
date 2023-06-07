# Task 2: Build the application image

The `Dockerfile` has `dotnet` commands to restore NuGet packages and publish the app:

```bash
cat Dockerfile
```

> Even if you're not familiar with the [Dockerfile syntax](https://docs.docker.com/engine/reference/builder/), you can kind of work out that this is a script to compile the app and package it up to run

You run the script with the `docker image build` command, which produces a container package called a _Docker image_:

```bash
docker image build --tag dotnetconf:19 .
```

You'll see lots of download progress bars, and some familiar output from MSBuild.

The final message `Successfully tagged dotnetconf:19` tells you the image has been built and given the tag `dotnetconf:19` - which is just the image name.
