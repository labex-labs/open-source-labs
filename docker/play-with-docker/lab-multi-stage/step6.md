# More about the lab

This lab was built from a [blog post](http://blog.alexellis.io/mutli-stage-docker-builds/). by [Alex Ellis](https://twitter.com/alexellisuk)

- Blog: [Builder pattern vs. Multi-stage builds in Docker](http://blog.alexellis.io/mutli-stage-docker-builds/).

> Note: We do not recommend moving over to multi-stage builds until they are fully available on the Docker Hub/Cloud and all editions of Docker. The example in `build.sh` provides an interim solution for using separate Dockerfiles to build and ship code.