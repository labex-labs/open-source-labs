# Image Inspection

As we have already seen with containers, and as we will see with other Docker's components (volume, network, ...), the **inspect** command is available for the image API and it returns all the information of the image provided.

The alpine image should already be present locally, if it's not, run the following command to pull it.

```bash
docker image pull alpine
```

Once we are sure it is there let's inspect it.

```bash
docker image inspect alpine
```

There is a lot of information in there:

- the layers the image is composed of
- the driver used to store the layers
- the architecture / os it has been created for
- metadata of the image
- ...

We will not go into all the details now but it's interesing to see an example of the Go template notation that enables to extract the part of information we need in just a simple command.

Let's get the list of layers (only one for alpine)

```bash
docker image inspect --format "{{ "{{ json .RootFS.Layers "}}}}" alpine | python -m json.tool
```

```
[
    "sha256:60ab55d3379d47c1ba6b6225d59d10e1f52096ee9d5c816e42c635ccc57a5a2b"
]
```

Let's try another example to query only the Architecture information

```bash
docker image inspect --format "{{ "{{ .Architecture "}}}}" alpine
```

This should return **amd64**.

Feel free to play with the Go template format and get familiar with it as it's really handy.
