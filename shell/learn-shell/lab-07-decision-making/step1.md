# Creating Your First If Statement

Let's start by creating a simple if statement that checks if a variable called `NAME` is equal to "John".

First, open a terminal in the WebIDE. You should be in the `/home/labex/project` directory by default. If you're not sure, you can always check your current directory with the `pwd` command.

Create a new file called `if.sh` using the following command:

```bash
touch if.sh
```

This command creates an empty file named `if.sh` in your current directory.

Now, open the `if.sh` file in the WebIDE. You can do this by clicking on the file in the file explorer on the left side of the WebIDE.

Add the following content to the file:

```bash
#!/bin/bash

NAME="John"
if [ "$NAME" = "John" ]; then
  echo "The name is John"
fi
```

Let's break down this script:

1. `#!/bin/bash`: This is called a "shebang" line. It tells the system which interpreter to use to run the script. In this case, we're using Bash.
2. `NAME="John"`: This line creates a variable called `NAME` and assigns it the value "John".
3. `if [ "$NAME" = "John" ]; then`: This is the start of our if statement. It checks if the value of `NAME` is equal to "John".
   - The square brackets `[ ]` are actually a command in Bash, equivalent to the `test` command.
   - We put `"$NAME"` in quotes to handle cases where `NAME` might be empty or contain spaces.
   - The semicolon and `then` are part of the if statement syntax in Bash.
4. `echo "The name is John"`: This line will be executed if the condition is true.
5. `fi`: This marks the end of the if statement. It's "if" spelled backwards!

Save the file after adding this content.

Now, we need to make the script executable. In Unix-like systems, files aren't executable by default for security reasons. We can change this using the `chmod` command:

```bash
chmod +x if.sh
```

This command adds the execute permission to the file. The `+x` means "add execute permission".

Now, run the script:

```bash
./if.sh
```

The `./` tells the shell to look for the script in the current directory.

You should see the output: `The name is John`

If you don't see this output, double-check that you've saved the file with the correct content and that you've made it executable.
