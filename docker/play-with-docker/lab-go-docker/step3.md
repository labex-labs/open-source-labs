# Building lean images

The Go binaries that we produced with this technique are
_statically linked_. This means that they embed all the code
that they need to run, including all dependencies. This
contrasts with _dynamically linked_ programs, which don't
contain some basic libraries (like the "libc") and use a system-wide
copy which is resolved at run time.

This means that we can drop our Go compiled program in
a container, _without anything else_, and it should work.

Let's try this!

### The `scratch` image

There is a special image in the Docker ecosystem: `scratch`.
This is an empty image. It doesn't need to be created or
downloaded, since by definition, it is empty.

Let's create a new, empty directory for our new Go lean image.

In this new directory, create the following Dockerfile:

```dockerfile
FROM scratch
COPY ./hello /hello
ENTRYPOINT ["/hello"]
```

This means:

- start _from scratch_ (an empty image),
- add the `hello` file to the root of the image,
- define this `hello` program to be the default thing to execute
  when starting this container.

Then, produce our `hello` binary as follows:

```bash
docker container run -v $(pwd):/go/bin --rm \
  golang go get github.com/golang/example/hello/...
```

Note: we don't need to set `GOOS` and `GOARCH` here, because
precisely, we want a binary that will run _in a Docker container_,
not on our host system. So leave those variables alone!

Then, we can build the image:

```bash
docker image build -t hello .
```

And test it:

```bash
docker container run hello
```

(This should display `Hello, Go examples!`.)

Last but not least, check the image's size:

```bash
docker image ls hello
```

If we did everything right, this image should be about 2 MB. Not bad!

### Building something without pushing to GitHub

Of course, if we had to push to GitHub each time we wanted to compile,
we would waste a lot of time.

When you want to work on a piece of code and build it within a container,
you can mount a local directory to `/go` in the `golang` container, so that the
`$GOPATH` is persisted across invocations: `docker run -v $HOME/go:/go golang ...`.

But you can also mount local directories to specific paths, to "override" some
packages (the ones that you have edited locally). Here is a complete example:

```bash
# Adapt the two following environment variables if you are not running on a Mac
export GOOS=darwin GOARCH=amd64
mkdir go-and-docker-is-love
cd go-and-docker-is-love
git clone git://github.com/golang/example
cat example/hello/hello.go
sed -i .bak s/olleH/eyB/ example/hello/hello.go
docker container run --rm \
  -v $(pwd)/example:/go/src/github.com/golang/example \
  -v $(pwd):/go/bin/${GOOS}_${GOARCH} \
  -e GOOS -e GOARCH \
  golang go get github.com/golang/example/hello/...
./hello
# Should display "Bye, Go examples!"
```
