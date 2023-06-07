# Task 2: Package and run a custom app using Docker

In this step you'll learn how to package your own apps as Docker images using a [Dockerfile](https://docs.docker.com/engine/reference/builder/).

The Dockerfile syntax is straightforward. In this task, we're going to create a simple NGINX website from a Dockerfile.

### Build a simple website image

Let's have a look at the Dockerfile we'll be using, which builds a simple website that allows you to send a tweet.

1. Make sure you're in the `linux_tweet_app` directory.

   ```bash
   cd ~/linux_tweet_app
   ```

2. Display the contents of the Dockerfile.

   ```bash
   cat Dockerfile
   ```

   ```
   FROM nginx:latest

   COPY index.html /usr/share/nginx/html
   COPY linux.png /usr/share/nginx/html

   EXPOSE 80 443

   CMD ["nginx", "-g", "daemon off;"]
   ```

   Let's see what each of these lines in the Dockerfile do.

   - [FROM](https://docs.docker.com/engine/reference/builder/#from) specifies the base image to use as the starting point for this new image you're creating. For this example we're starting from `nginx:latest`.
   - [COPY](https://docs.docker.com/engine/reference/builder/#copy) copies files from the Docker host into the image, at a known location. In this example, `COPY` is used to copy two files into the image: `index.html`. and a graphic that will be used on our webpage.
   - [EXPOSE](https://docs.docker.com/engine/reference/builder/#expose) documents which ports the application uses.
   - [CMD](https://docs.docker.com/engine/reference/builder/#cmd) specifies what command to run when a container is started from the image. Notice that we can specify the command, as well as run-time arguments.

3. In order to make the following commands more copy/paste friendly, export an environment variable containing your DockerID (if you don't have a DockerID you can get one for free via [Docker Hub](https://hub.docker.com)).

   You will have to manually type this command as it requires your unique DockerID.

   `export DOCKERID=<your docker id>`

4. Echo the value of the variable back to the terminal to ensure it was stored correctly.

   ```bash
   echo $DOCKERID
   ```

5. Use the `docker image build` command to create a new Docker image using the instructions in the Dockerfile.

   - `--tag` allows us to give the image a custom name. In this case it's comprised of our DockerID, the application name, and a version. Having the Docker ID attached to the name will allow us to store it on Docker Hub in a later step
   - `.` tells Docker to use the current directory as the build context

   Be sure to include period (`.`) at the end of the command.

   ```bash
   docker image build --tag $DOCKERID/linux_tweet_app:1.0 .
   ```

   The output below shows the Docker daemon executing each line in the Dockerfile

   ```
   Sending build context to Docker daemon  32.77kB
   Step 1/5 : FROM nginx:latest
   latest: Pulling from library/nginx
   afeb2bfd31c0: Pull complete
   7ff5d10493db: Pull complete
   d2562f1ae1d0: Pull complete
   Digest: sha256:af32e714a9cc3157157374e68c818b05ebe9e0737aac06b55a09da374209a8f9
   Status: Downloaded newer image for nginx:latest
   ```