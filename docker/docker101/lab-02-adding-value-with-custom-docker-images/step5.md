# Step 5: Deploying a Change

The "hello world!" application is overrated, let's update the app so that it says "Hello Beautiful World!" instead.

1. Update `app.py`

   Replace the string "Hello World" with "Hello Beautiful World!" in `app.py`. You can update the file with the following command. (copy-paste the entire code block)

   ```bash
   echo 'from flask import Flask

   app = Flask(__name__)

   @app.route("/")
   def hello():
       return "hello beautiful world!"

   if __name__ == "__main__":
       app.run(host="0.0.0.0")' > app.py
   ```

1. Rebuild and push your image

   Now that your app is updated, you need repeat the steps above to rebuild your app and push it to the Docker Hub registry.

   First rebuild, this time use your Docker Hub username in the build command:

   ```bash
   $  docker image build -t $DOCKERHUB_USERNAME/python-hello-world .
   Sending build context to Docker daemon  3.072kB
   Step 1/4 : FROM python:3.6.1-alpine
   ---> c86415c03c37
   Step 2/4 : RUN pip install flask
   ---> Using cache
   ---> ce41f2517c16
   Step 3/4 : CMD python app.py
   ---> Using cache
   ---> 0ab91286958b
   Step 4/4 : COPY app.py /app.py
   ---> 3e08b2eeace1
   Removing intermediate container 23a955e881fc
   Successfully built 3e08b2eeace1
   Successfully tagged <dockerhub-username>/python-hello-world:latest
   ```

   Notice the "Using cache" for steps 1-3. These layers of the Docker Image have already been built and `docker image build` will use these layers from the cache instead of rebuilding them.

   ```bash
   $ docker push $DOCKERHUB_USERNAME/python-hello-world
   The push refers to a repository [docker.io/<dockerhub-username>/python-hello-world]
   94525867566e: Pushed
   64d445ecbe93: Layer already exists
   18b27eac38a1: Layer already exists
   3f6f25cd8b1e: Layer already exists
   b7af9d602a0f: Layer already exists
   ed06208397d5: Layer already exists
   5accac14015f: Layer already exists
   latest: digest: sha256:91874e88c14f217b4cab1dd5510da307bf7d9364bd39860c9cc8688573ab1a3a size: 1786
   ```

   There is a caching mechanism in place for pushing layers too. Docker Hub already has all but one of the layers from an earlier push, so it only pushes the one layer that has changed.

   When you change a layer, every layer built on top of that will have to be rebuilt. Each line in a Dockerfile builds a new layer that is built on the layer created from the lines before it. This is why the order of the lines in our Dockerfile is important. We optimized our Dockerfile so that the layer that is most likely to change (`COPY app.py /app.py`) is the last line of the Dockerfile. Generally for an application, your code changes at the most frequent rate. This optimization is particularly important for CI/CD processes, where you want your automation to run as fast as possible.
