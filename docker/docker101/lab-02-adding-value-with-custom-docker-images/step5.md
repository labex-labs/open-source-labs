# Deploying a Change

The "hello world!" application is overrated, let's update the app so that it says "Hello Beautiful World!" instead.

## Update `app.py`

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

## Rebuild and Push Your Image

Now that your app is updated, you need repeat the steps above to rebuild your app and push it to the Docker Hub registry.

First rebuild, this time use your Docker Hub username in the build command:

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world .
```

Notice the "Using cache" for steps 1-3. These layers of the Docker Image have already been built and `docker image build` will use these layers from the cache instead of rebuilding them.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

There is a caching mechanism in place for pushing layers too. Docker Hub already has all but one of the layers from an earlier push, so it only pushes the one layer that has changed.

When you change a layer, every layer built on top of that will have to be rebuilt. Each line in a Dockerfile builds a new layer that is built on the layer created from the lines before it. This is why the order of the lines in our Dockerfile is important. We optimized our Dockerfile so that the layer that is most likely to change (`COPY app.py /app.py`) is the last line of the Dockerfile. Generally for an application, your code changes at the most frequent rate. This optimization is particularly important for CI/CD processes, where you want your automation to run as fast as possible.
