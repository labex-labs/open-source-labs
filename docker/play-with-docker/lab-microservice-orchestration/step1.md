# In this tutorial we will learn about basic application containerization using Docker and running various components of an application as microservices.
We will utilize [Docker Compose](https://docs.docker.com/compose/) for orchestration during the development.
This tutorial is targeted for beginners who have the basic familiarity with Docker.
If you are new to Docker, we recommend you check out [Docker for Beginners](/beginner-linux) tutorial first.

We will start from a basic Python script that scrapes links from a given web page and gradually evolve it into a multi-service application stack.
The demo code is available in the [Link Extractor](https://github.com/ibnesayeed/linkextractor) repo.
The code is organized in steps that incrementally introduce changes and new concepts.
After completion, the application stack will contain the following microservices:

- A web application written in PHP and served using Apache that takes a URL as the input and summarizes extracted links from it
- The web application talks to an API server written in Python (and Ruby) that takes care of the link extraction and returns a JSON response
- A Redis cache that is used by the API server to avoid repeated fetch and link extraction for pages that are already scraped

The API server will only load the page of the input link from the web if it is not in the cache.
The stack will eventually look like the figure below:

![A Microservice Architecture of the Link Extractor Application](/images/linkextractor-microservice-diagram.png)

This tutorial was initially developed for a colloquium in the [Computer Science Department](https://odu.edu/compsci) of the [Old Dominion University](https://www.odu.edu/), Norfolk, Virginia. A [video recording](https://www.youtube.com/watch?v=Y_X0F2FgYm8), [presentation slides](https://www.slideshare.net/ibnesayeed/introducing-docker-application-containerization-service-orchestration), and a brief description of the talk can be found in [a blog post](https://ws-dl.blogspot.com/2017/12/2017-12-03-introducing-docker.html).

> **Steps:**
>
> - Table of contents
>   {:toc}
