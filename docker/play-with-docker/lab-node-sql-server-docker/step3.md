# Add a SQL Server database container for storage

Storing data in client memory is only good for proof-of-concept applications. In this step you'll build and deploy version 2 of the app, which uses a SQL Server database to store the events.

First switch to the v2 code branch:

```bash
git checkout v2
```

Now clear up all the containers from the previous part:

```bash
docker container rm --force $(docker container ls --quiet)
```

You'll use Docker Compose to build and run the application. The compose file specifies the database and application containers to run, and how to configure them.

The compose file also contains the path to the [application Dockerfile](https://github.com/dockersamples/node-bulletin-board/blob/v2/bulletin-board-app/Dockerfile) and to the [database Dockerfile](https://github.com/dockersamples/node-bulletin-board/blob/v2/bulletin-board-db/Dockerfile), so you can build the database and application images with one command:

```bash
docker-compose build
```

When that completes, you'll have two Docker images:

- `<your-docker-id>/bulletin-board-db:v2` - which is based on Microsoft's SQL Server image and packages the database schema for the bulletin board

- `<your-docker-id>/bulletin-board-app:v2` - which is the new version of the Node.js application, using SQL Server to store events

You can start the whole app with Docker Compose:

```bash
docker-compose up -d
```

You'll see compose starts the database first, because it's specified as a dependency for the application container. Then it starts the app container.

> If you list all containers, you'll see there are two instances of the app container. One container started before the database was ready, so it failed - and then Docker Compose started a replacement container, which did connect to the database.

```bash
docker container ls --all
```

[Click here for v2 of the app](/){:data-term=".term1"}{:data-port="8080"}

You'll see it's the same user interface, but now you can add and delete events and when you refresh the page they're still there. The data is persisted in SQL Server.

The SQL Server database is not publicly available. In the [docker-compose.yml](https://github.com/dockersamples/node-bulletin-board/blob/v2/docker-compose.yml) file, the web container, the port `8080` is published so you can send traffic in, but no ports are published for the database. It's only available to other containers and to Docker.
