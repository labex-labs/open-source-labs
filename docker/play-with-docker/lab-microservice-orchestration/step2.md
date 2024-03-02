# Basic Link Extractor Script

Checkout the `step0` branch and list files in it.

```bash
git checkout step0
tree
```

```
.
├── README.md
└── linkextractor.py

0 directories, 2 files
```

The `linkextractor.py` file is the interesting one here, so let's look at its contents:

```bash
cat linkextractor.py
```

```python
#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

res = requests.get(sys.argv[-1])
soup = BeautifulSoup(res.text, "html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))
```

This is a simple Python script that imports three packages: `sys` from the standard library and two popular third-party packages `requests` and `bs4`.
User-supplied command line argument (which is expected to be a URL to an HTML page) is used to fetch the page using the `requests` package, then parsed using the `BeautifulSoup`.
The parsed object is then iterated over to find all the anchor elements (i.e., `<a>` tags) and print the value of their `href` attribute that contains the hyperlink.

However, this seemingly simple script might not be the easiest one to run on a machine that does not meet its requirements.
The `README.md` file suggests how to run it, so let's give it a try:

```bash
./linkextractor.py http://example.com/
```

```
bash: ./linkextractor.py: Permission denied
```

When we tried to execute it as a script, we got the `Permission denied` error.
Let's check the current permissions on this file:

```bash
ls -l linkextractor.py
```

```
-rw-r--r--    1 root     root           220 Sep 23 16:26 linkextractor.py
```

This current permission `-rw-r--r--` indicates that the script is not set to be executable.
We can either change it by running `chmod a+x linkextractor.py` or run it as a Python program instead of a self-executing script as illustrated below:

```bash
python3 linkextractor.py
```

```python
Traceback (most recent call last):
  File "linkextractor.py", line 5, in <module>
    from bs4 import BeautifulSoup
ImportError: No module named bs4
```

Here we got the first `ImportError` message because we are missing the third-party package needed by the script.
We can install that Python package (and potentially other missing packages) using one of the many techniques to make it work, but it is too much work for such a simple script, which might not be obvious for those who are not familiar with Python's ecosystem.

Depending on which machine and operating system you are trying to run this script on, what software is already installed, and how much access you have, you might face some of these potential difficulties:

- Is the script executable?
- Is Python installed on the machine?
- Can you install software on the machine?
- Is `pip` installed?
- Are `requests` and `beautifulsoup4` Python libraries installed?

This is where application containerization tools like Docker come in handy.
In the next step we will try to containerize this script and make it easier to execute.
