# Go without `go`

_... And by that, we mean "Go without installing `go`"._

If you write Go code, or if you have even the slightest interest
into the Go language, you certainly have the Go compiler and toolchain installed,
so you might be wondering "what's the point?"; but there are
a few scenarios where you want to compile Go without installing Go.

- You still have this old Go 1.2 on your machine (that you can't
  or won't upgrade), and you have to work on this codebase that
  requires a newer version of the toolchain.
- You want to play with cross compilation features of Go 1.5
  (for instance, to make sure that you can create OS X binaries
  from a Linux system).
- You want to have multiple versions of Go side-by-side, but don't
  want to completely litter your system.
- You want to be 100% sure that your project and all its dependencies
  download, build, and run fine on a clean system.

If any of this is relevant to you, then let's call Docker to the rescue!

## Compiling a program in a container

When you have installed Go, you can do `go get -v github.com/user/repo`
to download, build, and install a library. (The `-v` flag is just
here for verbosity, you can remove it if you prefer your
toolchain to be swift and silent!)

You can also do `go get github.com/user/repo/...` (yes, that's
three dots) to download, build, and install all the things in
that repo (including libraries and binaries).

We can do that in a container!

Try this:

```bash
docker container run golang go get -v github.com/golang/example/hello/...
```

This will pull the `golang` image (unless you have it already;
then it will start right away), and create a container based on
that image. In that container, `go` will download a little
"hello world" example, build it, and install it. But it will
install it in the container ... So how do we run that program now?

## Running our program in a container

One solution is to _commit_ the container that we just built,
i.e. "freeze" it into a new image:

```bash
docker container commit $(docker container ls -lq) awesomeness
```

Note: `docker container ls -lq` outputs the ID (and only the ID!) of
the last container that was executed. If you are the only
user on your machine, and if you haven't created another
container since the previous command, that container
should be the one in which we just built the "hello world"
example.

Now, we can run our program in a container based on
the image that we just built:

```bash
docker container run awesomeness hello
```

The output should be `Hello, Go examples!`.

### Bonus points

When creating the image with `docker container commit`, you can
use the `--change` flag to specify arbitrary [Dockerfile](https://docs.docker.com/engine/reference/builder/) commands.
For instance, you could use a `CMD` or `ENTRYPOINT` command
so that `docker run awesomeness` automatically executes
`hello`.

## Running in a throwaway container

What if we don't want to create an extra image just to
run this Go program?

We got you covered:

```bash
docker container run --rm golang sh -c \
    "go get github.com/golang/example/hello/... && exec hello"
```

Wait a minute, what are all those bells and whistles?

- `--rm` tells to the Docker CLI to automatically issue a
  `docker container rm` command once the container exits. That way,
  we don't leave anything behind ourselves.
- We chain together the build step (`go get`) and the
  execution step (`exec hello`) using the shell logical
  operator `&&`. If you're not a shell aficionado, `&&`
  means "and". It will run the first part `go get...`,
  and if (and only if!) that part is successful, it will run
  the second part (`exec hello`). If you wonder why this
  is like that: it works like a lazy `and` evaluator,
  which needs to evaluate the right hand side
  only if the left hand side evaluates to `true`.
- We pass our commands to `sh -c`, because if we were to
  simply do `docker container run golang "go get ... && hello"`,
  Docker would try to execute the program named `go SPACE get
SPACE etc.` and that wouldn't work. So instead, we start
  a shell and instruct the shell to execute the command
  sequence.
- We use `exec hello` instead of `hello`: this will replace
  the current process (the shell that we started) with the
  `hello` program. This ensures that `hello` will be PID 1
  in the container, instead of having the shell as PID 1
  and `hello` as a child process. This is totally useless
  for this tiny example, but when we will run more useful
  programs, this will allow them to receive external signals
  properly, since external signals are delivered to PID 1 of
  the container. What kind of signal, you might be wondering?
  A good example is `docker container stop`, which sends `SIGTERM` to
  PID 1 in the container.
