# Prerequisites

You will need:

- a copy of the application source code
- a Docker ID

## Clone the source code from GitHub

Use the following command to clone the application source code from GitHub (you can click the command or manually type it). This will make a copy of the lab's repo in a new sub-directory called `node-bulletin-board`.

```bash
git clone https://github.com/dockersamples/node-bulletin-board.git
```

And browse to the source code folder:

```bash
cd node-bulletin-board
```

## Save your Docker ID

You need a Docker ID to push your images to Docker Hub. If you don't have one, [create a free Docker ID at Docker Hub](https://hub.docker.com).

Now save your Docker ID in an environment variable - **you need to type this command manually with your own Docker ID**:

```
export dockerId='your-docker-id'
```

> Be sure to use your own Docker ID. Mine is `sixeyed`, so the command I run is `export dockerId='sixeyed'`.

Check your Docker ID gets displayed when you read the variable:

```bash
echo $dockerId
```
