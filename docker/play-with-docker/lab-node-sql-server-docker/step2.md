# Run v1 of the app in a container

The first version of the application uses a single container, running the Node.js application, and the data is only stored on the client's browser.

Switch to the `v1` source code branch:

```bash
git checkout v1
```

Now build the Docker image, which uses this [Dockerfile](https://github.com/dockersamples/node-bulletin-board/blob/v1/bulletin-board-app/Dockerfile) to package the source code on top of the official Node.js image:

```bash
docker image build --tag $dockerId/bb-app:v1 --file bulletin-board-app/Dockerfile ./bulletin-board-app
```

When that completes you will have version 1 of the app in an image stored locally. Run a container from that image to start the app:

```bash
docker container run --detach --publish 8080:8080 $dockerId/bb-app:v1
```

Docker will start a container from the application image, which runs `npm start` to start the app. You can browse to the application on port 8080:

[Click here for v1 of the app](/){:data-term=".term1"}{:data-port="8080"}

You'll see the bulletin board application, and you can add and remove events:

![Bulletin Board sample app](../images/node-sql-server-docker-bulletin-board.jpg)

If you make some changes and refresh the browser, you'll see your changes get lost. That's because the events are only stored in memory on the client.

In the next step you'll fix that.
