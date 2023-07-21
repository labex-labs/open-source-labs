# Multi-staged builds

A common pipe-line for building applications in Docker involves adding SDKs and runtimes, followed by adding code and building it. The most efficient way to get a small image tends to be to use 2-3 Dockerfiles with different filenames where each one takes the output of the last. This is referred to as the _Builder pattern_ in the Docker community.

This lab explores a new bleeding-edge feature called Multi-stage builds. It is not yet released into a Docker version, but when it is available on the Docker Hub/Cloud and for all the Docker editions it will mean we can use a single Dockerfile with multiple stages instead of the _Builder pattern_.

Let's build a simple Golang application which counts internal/external facing anchor tags to help us come up with an SEO rating.

Let's try out the href-counter Docker image from the hub, then look at how to re-build from the Github repository:

```bash
docker run -e url=https://news.ycombinator.com alexellis2/href-counter
```

```
{"internal":197,"external":32}
```

You get a JSON object returned giving the total amount of internal vs external links.

Let's clone the source:

```bash
git clone https://github.com/alexellis/href-counter
cd href-counter
```

```
Cloning into 'href-counter'...
remote: Counting objects: 24, done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 24 (delta 7), reused 12 (delta 1), pack-reused 0
Unpacking objects: 100% (24/24), done.
```
