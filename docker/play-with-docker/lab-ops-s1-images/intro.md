# Introduction

In the previous exercise you pulled down images from [Docker Store](https://store.docker.com) to run in your containers. Then you ran multiple instances and noted how each instance was isolated from the others. We hinted that this is used in many production IT environments every day but obviously we need a few more tools in our belt to get to the point where Docker can become a true time & money saver.

First thing you may want to do is figure out how to create our own images. While there are over 700K images on [Docker Store](https://store.docker.com) it is almost certain that none of them are exactly what you run in your data center today. Even something as common as a Windows OS image would get its own tweaks before you actually run it in production. In the lab `ops-s1-hello`, we created a file called "hello.txt" in one of our container instances. If that instance of our Alpine container was something we wanted to re-use in future containers and share with others, we would need to create a custom image that everyone could use.

We will start with the simplest form of image creation, in which we simply `commit` one of our container instances as an image. Then we will explore a much more powerful and useful method for creating images: the Dockerfile.

We will then see how to get the details of an image through the inspection and explore the filesystem to have a better understanding of what happens under the hood.
