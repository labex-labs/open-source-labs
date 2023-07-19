# Step 2: Link Extractor Module with Full URI and Anchor Text

Checkout the `step2` branch and list files in it.

```bash
git checkout step2
tree
```

```
.
├── Dockerfile
├── README.md
└── linkextractor.py

0 directories, 3 files
```

In this step the `linkextractor.py` script is updated with the following functional changes:

- Paths are normalized to full URLs
- Reporting both links and anchor texts
- Usable as a module in other scripts

Let's have a look at the updated script:

```bash
cat linkextractor.py
```

```py
#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    base = url
    # TODO: Update base if a <base> element is present with the href attribute
    links = []
    for link in soup.find_all("a"):
        links.append({
            "text": " ".join(link.text.split()) or "[IMG]",
            "href": urljoin(base, link.get("href"))
        })
    return links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(sys.argv[-1]):
        print("[{}]({})".format(link["text"], link["href"]))
```

The link extraction logic is abstracted into a function `extract_links` that accepts a URL as a parameter and returns a list of objects containing anchor texts and normalized hyperlinks.
This functionality can now be imported into other scripts as a module (which we will utilize in the next step).

Now, let's build a new image and see these changes in effect:

```bash
docker image build -t linkextractor:step2 .
```

We have used a new tag `linkextractor:step2` for this image so that we don't overwrite the image from the `step1` to illustrate that they can co-exist and containers can be run using either of these images.

```bash
docker image ls
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
linkextractor       step2               be2939eada96        3 seconds ago        931MB
linkextractor       step1               673d045a822f        About a minute ago   931MB
python              3                   a9d071760c82        2 weeks ago          923MB
```

Running a one-off container using the `linkextractor:step2` image should now yield an improved output:

```bash
docker container run -it --rm linkextractor:step2 https://training.play-with-docker.com/
```

```
[Play with Docker classroom](https://training.play-with-docker.com/)
[About](https://training.play-with-docker.com/about/)
[IT Pros and System Administrators](https://training.play-with-docker.com/#ops)
[Developers](https://training.play-with-docker.com/#dev)
[Stage 1: The Basics](https://training.play-with-docker.com/ops-stage1)
[Stage 2: Digging Deeper](https://training.play-with-docker.com/ops-stage2)
[Stage 3: Moving to Production](https://training.play-with-docker.com/ops-stage3)
[Stage 1: The Basics](https://training.play-with-docker.com/dev-stage1)
[Stage 2: Digging Deeper](https://training.play-with-docker.com/dev-stage2)
[Stage 3: Moving to Staging](https://training.play-with-docker.com/dev-stage3)
[Full list of individual labs](https://training.play-with-docker.com/alacart)
[[IMG]](https://twitter.com/intent/tweet?text=Play with Docker Classroom&url=https://training.play-with-docker.com/&via=docker&related=docker)
[[IMG]](https://facebook.com/sharer.php?u=https://training.play-with-docker.com/)
[[IMG]](https://plus.google.com/share?url=https://training.play-with-docker.com/)
[[IMG]](http://www.linkedin.com/shareArticle?mini=true&url=https://training.play-with-docker.com/&title=Play%20with%20Docker%20Classroom&source=https://training.play-with-docker.com)
[[IMG]](https://2018.dockercon.com/)
[DockerCon 2018 in San Francisco](https://2018.dockercon.com/)
[training.docker.com](https://success.docker.com/training/)
[Register here](https://community.docker.com/registrations/groups/4316)
[Docker, Inc.](https://docker.com)
[[IMG]](https://www.docker.com)
[[IMG]](https://www.facebook.com/docker.run)
[[IMG]](https://twitter.com/docker)
[[IMG]](https://www.github.com/play-with-docker/play-with-docker.github.io)
```

Running a container using the previous image `linkextractor:step1` should still result in the old output:

```bash
docker container run -it --rm linkextractor:step1 https://training.play-with-docker.com/
```

So far, we have learned how to containerize a script with its necessary dependencies to make it more portable.
We have also learned how to make changes in the application and build different variants of Docker images that can co-exist.
In the next step we will build a web service that will utilize this script and will make the service run inside a Docker container.
