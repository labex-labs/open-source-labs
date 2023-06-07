# The special case of SSL certificates

There is one more thing that you have to worry about if
your code has to validate SSL certificates; for instance
if it will connect to external APIs over HTTPS. In that
case, you need to put the root certificates in your
container too, because Go won't bundle those into your
binary.

### Installing the SSL certificates

Three again, there are multiple options available, but
the easiest one is to use a package from an existing
distribution.

Alpine is a good candidate here because it's so tiny.
The following `Dockerfile` will give you a base image
that is small, but has an up-to-date bundle of root
certificates:

```dockerfile
FROM alpine:3.4
RUN apk add --no-cache ca-certificates apache2-utils
```

Check it out; the resulting image is only 6 MB!

Note: the `--no-cache` option tells `apk` (the Alpine
package manager) to get the list of available packages
from Alpine's distribution mirrors, without saving it
to disk. You might have seen Dockerfiles doing something
like `apt-get update && apt-get install ... && rm -rf /var/cache/apt/*`;
this achieves something equivalent (i.e. not leave package
caches in the final image) with a single flag.

_As an added bonus,_ putting your application in a container
based on the Alpine image gives you access to a ton of really
useful tools: now you can drop a shell into your container
and poke around while it's running, if you need to!
