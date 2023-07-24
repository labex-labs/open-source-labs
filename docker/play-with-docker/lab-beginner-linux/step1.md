# Prerequisites

You will need all of the following to complete this lab:

- A clone of the lab's GitHub repo.
- A DockerID.

## Clone the Lab's GitHub Repo

Use the following command to clone the lab's repo from GitHub (you can click the command or manually type it). This will make a copy of the lab's repo in a new sub-directory called `linux_tweet_app`.

```bash
git clone https://github.com/dockersamples/linux_tweet_app
```

## Make sure you have a DockerID

If you do not have a DockerID (a free login used to access Docker Hub), please visit [Docker Hub](https://hub.docker.com) and register for one. You will need this for later steps.

## Run some simple Docker containers

There are different ways to use containers. These include:

1. **To run a single task:** This could be a shell script or a custom app.
2. **Interactively:** This connects you to the container similar to the way you SSH into a remote server.
3. **In the background:** For long-running services like websites and databases.

In this lab, you'll try each of those options and see how Docker manages the workload.
