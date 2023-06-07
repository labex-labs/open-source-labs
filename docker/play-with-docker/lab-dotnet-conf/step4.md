# Task 3: Run a .NET Core container!

A Docker image is a complete packaged app. You can share it on [Docker Hub](https://hub.docker.com), which is how thousands of open-source and commercial projects now distribute their software.

Your image contains the .NET Core 3.0 runtime, together with the assemblies and configuration for the demo app.

You run the app by running a container from the image:

```bash
docker container run dotnetconf:19
```

> Scroll up to read the message from .NET Bot - that's your .NET Conf code!

If you want to learn more about what's happened here and how you can use Docker to build cross-platform apps that run on Windows, Linux, Itenal and Arm - check out this blog post:

- [Docker + Arm Virtual Meetup Recap: Building Multi-arch Apps with Buildx](https://blog.docker.com/2019/09/docker-arm-virtual-meetup-multi-arch-with-buildx/).
