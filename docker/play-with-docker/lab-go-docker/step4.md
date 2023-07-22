# The special case of the `net` package and CGo

Before diving into real-world Go code, we have to confess something:
we lied a little bit about the static binaries. If you are using CGo,
or if you are using the `net` package, the Go linker will generate
a dynamic binary. In the case of the `net` package (which a _lot_
of useful Go programs out there are using indeed!), the main culprit
is the DNS resolver. Most systems out there have a fancy, modular name
resolution system (like the _Name Service Switch_) which relies on
plugins which are, technically, dynamic libraries. By default,
Go will try to use that; and to do so, it will produce dynamic
libraries.

How do we work around that?

## Re-using another distro's libc

One solution is to use a base image that _has_ the essential
libraries needed by those Go programs to function. Almost any
"regular" Linux distro based on the GNU libc will do the trick.
So instead of `FROM scratch`, you would use `FROM debian` or
`FROM fedora`, for instance. The resulting image will be much
bigger now; but at least, the bigger bits will be shared with
other images on your system.

Note: you _cannot_ use Alpine
in that case, since Alpine is using the musl library instead
of the GNU libc.

## Bring your own libc

Another solution is to surgically extract the files needed,
and place them in your container with `COPY`. The resulting
container will be small. However, this extraction process
leaves the author with the uneasy impression of a really
dirty job, and they would rather not go into more details.

If you want to see for yourself, look around `ldd` and the
Name Service Switch plugins mentioned earlier.

## Producing static binaries with `netgo`

We can also instruct Go to _not_ use the system's libc, and
substitute Go's `netgo` library, which comes with a native
DNS resolver.

To use it, just add `-tags netgo -installsuffix netgo` to
the `go get` options.

- `-tags netgo` instructs the toolchain to use netgo.

* `-installsuffix netgo` will make sure that the resulting
  libraries (if any) are placed in a different, non-default
  directory. This will avoid conflicts between code built
  with and without netgo, if you do multiple `go get`
  (or `go build`) invocations. If you build in containers
  like we have shown so far, this is not strictly necessary,
  since there will be no other Go code compiled in this
  container, ever; but it's a good idea to get used to it,
  or at least know that this flag exists.
