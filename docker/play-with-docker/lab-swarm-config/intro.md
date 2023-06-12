# Introduction

This lab showcases the [config](https://github.com/moby/moby/pull/32336) swarm feature that allow config objects to be attached to services. Config files can be mounted inside services' containers, avoiding the need to bake configuration into images.

Configuration files are similar to secrets, and in fact the CLI and API show few differences between the two. The principal differences so far are:

- Secrets are always redacted at the API level, so the payload cannot be obtained through an API call after they are created.

- Secrets are restricted to the /run/secrets directory inside the container, as a design choice. Config files can be mounted anywhere.
  Start securing your swarm services using the latest compose reference that allows to specify secrets in your application stack
