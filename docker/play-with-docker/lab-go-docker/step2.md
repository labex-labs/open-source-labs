# Using a different version of Go

When you use the `golang` image, Docker expands that to
`golang:latest`, which (as you might guess) will map to
the latest version available on the Docker Hub.

If you want to use a specific version of Go, that's very
easy: specify that version as a _tag_ after the image name.

For instance, to use Go 1.5, change the example above
to replace `golang` with `golang:1.5`:

```bash
docker container run --rm golang:1.5 sh -c \
    "go get github.com/golang/example/hello/... && exec hello"
```

You can see all the versions (and variants) available on the
[Golang image page](https://hub.docker.com/r/library/golang/tags/)
on the Docker Hub.

## Installing on our system

OK, so what if we want to run the compiled program on our
system, instead of in a container?

We could copy the compiled binary out of the container.
Note, however, that this will work only if our container
architecture matches our host architecture; in other words,
if we run Docker on Linux. (I'm leaving out people who
might be running Windows Containers!)

The easiest way to get the binary out of the container
is to map the `$GOPATH/bin` directory to a local directory.
In the `golang` container, `$GOPATH` is `/go`. So we can do
the following:

```bash
docker container run -v /tmp/bin:/go/bin \
  golang go get github.com/golang/example/hello/...
/tmp/bin/hello
```

If you are on Linux, you should see the `Hello, Go examples!` message.
But if you are, for instance, on a Mac, you will probably see:

```bash
/tmp/test/hello: cannot execute binary file
```

What can we do about it?

## Cross-compilation

Go 1.5 comes with [outstanding out-of-the-box cross-compilation abilities](http://dave.cheney.net/2015/08/22/cross-compilation-with-go-1-5), so if your
container operating system and/or architecture doesn't match your system's,
it's no problem at all!

To enable cross-compilation, you need to set `GOOS` and/or `GOARCH`.

For instance, assuming that you are on a 64 bits Mac:

```bash
docker container run -e GOOS=darwin -e GOARCH=amd64 -v /tmp/crosstest:/go/bin \
  golang go get github.com/golang/example/hello/...
```

The output of cross-compilation is not directly in `$GOPATH/bin`,
but in `$GOPATH/bin/$GOOS_$GOARCH`. In other words, to run the
program, you have to execute `/tmp/crosstest/darwin_amd64/hello`.

## Installing straight to the `$PATH`

If you are on Linux, you can even install directly to your system
`bin` directories:

```bash
docker container run -v /usr/local/bin:/go/bin \
  golang go get github.com/golang/example/hello/...
```

However, on a Mac, trying to use `/usr` as a volume will not
mount your Mac's filesystem to the container. It will mount
the `/usr` directory of the Moby VM (the small Linux VM
hidden behind the Docker whale icon in your toolbar).

You can, however, use `/tmp` or something in your home
directory, and then copy it from there.
