# Some Generative Art

Create the following program and put it in a file called `art.py`:

```python
# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in rows:
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
```

Make sure you can run this program from the command line or a terminal.

```bash
python3 art.py 10 20
```

If you run the above command, you'll get a crash and traceback message.
Go fix the problem and run the program again. You should get output like
this:

```bash
python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|

```

## Important Note

It is absolutely essential that you are able to edit, run, and debug
ordinary Python programs for the rest of this course. The choice
of editor, IDE, or operating system doesn't matter as long as you
are able to experiment interactively and create normal Python source
files that can execute from the command line.
