# Step 3: Run the Docker image

Now that you have built the image, you can run it to see that it works.

1. Run the Docker image

   ```bash
   $ docker run -p 5001:5000 -d python-hello-world
   0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26
   ```

   The `-p` flag maps a port running inside the container to your host. In this case, we are mapping the python app running on port 5000 inside the container, to port 5001 on your host. Note that if port 5001 is already in use by another application on your host, you may have to replace 5001 with another value, such as 5002.

1. Navigate to [localhost:5001](http://localhost:5001) in a browser to see the results.

   In a terminal run `curl localhost:5001`, which returns `hello world!`.

   If you are using katacoda, click on the link in the left-hand pane that says: `View port at https://....environments.katacoda.com` then type in 5001 and click `Display Port`.

   In play-with-docker, click the link `5001` that should appear near the top of your session.

   You should see "hello world!" on your browser.

1. Check the log output of the container.

   If you want to see logs from your application you can use the `docker container logs` command. By default, `docker container logs` prints out what is sent to standard out by your application. Use `docker container ls` to find the id for your running container.

   ```bash
   $ docker container ls
   CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES
   7b04d5320cb4    python-hello-world   "python app.py"     About a minute ago   Up About a minute   0.0.0.0:5001->5000/tcp   elastic_ganguly
   $ docker container logs [container id]
   * Serving Flask app "app" (lazy loading)
   * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
   * Debug mode: off
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   172.17.0.1 - - [23/Sep/2020 22:00:33] "GET / HTTP/1.1" 200 -
   ```

   The Dockerfile is how you create reproducible builds for your application. A common workflow is to have your CI/CD automation run `docker image build` as part of its build process. Once images are built, they will be sent to a central registry, where it can be accessed by all environments (such as a test environment) that need to run instances of that application. In the next step, we will push our custom image to the public docker registry: the docker hub, where it can be consumed by other developers and operators.
