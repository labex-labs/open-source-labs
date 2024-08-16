# Create a new script file

Let's start by creating a new script file. We'll use the WebIDE (VS Code) for this lab.

1. Open the WebIDE if it's not already open.
2. In the file explorer on the left, navigate to the `/home/labex/project` directory.
3. Right-click in the file explorer and select "New File".
4. Name the new file `arguments.sh`.

Now that we have created the file, let's add the basic structure of our script:

```bash
#!/bin/bash

# Your code will go here
```

The first line is called the "shebang" or "hashbang". It tells the system which interpreter to use to execute the script. In this case, we're using bash. The `#!` at the beginning is special and tells the system that this is the interpreter line.

For beginners: The shebang line is important because it allows you to run the script directly (like `./arguments.sh`) instead of having to type `bash arguments.sh` every time. It's a small detail, but it makes your scripts more convenient to use.
