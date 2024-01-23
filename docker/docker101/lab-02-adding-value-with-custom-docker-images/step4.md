# Step 4: Push to a Central Registry

Navigate to [Docker Hub](https://hub.docker.com) and create an account if you haven't already. Alternatively, you can also use [https://quay.io](https://quay.io) for instance.

For this lab we will be using the docker hub as our central registry. Docker hub is a free service to store publicly available images, or you can pay to store private images. Go to the [Docker Hub](https://hub.docker.com) website and create a free account.

Most organizations that use docker heavily will set up their own registry internally. To simplify things, we will be using the Docker Hub, but the following concepts apply to any registry.

Login

You can log into the image registry account by typing `docker login` on your terminal, or if using podman, type `podman login`.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME 
Password: 
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Tag your image with your username

The Docker Hub naming convention is to tag your image with [dockerhub username]/[image name]. To do this, we are going to tag our previously created image `python-hello-world` to fit that format.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Push your image to the registry

Once we have a properly tagged image, we can use the `docker push` command to push our image to the Docker Hub registry.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Check out your image on docker hub in your browser

Navigate to [Docker Hub](https://hub.docker.com) and go to your profile to see your newly uploaded image at `https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world`.

Now that your image is on Docker Hub, other developers and operations can use the `docker pull` command to deploy your image to other environments.

**Note:** Docker images contain all the dependencies that it needs to run an application within the image. This is useful because we no longer have deal with environment drift (version differences) when we rely on dependencies that are install on every environment we deploy to. We also don't have to go through additional steps to provision these environments. Just one step: install docker, and you are good to go.
