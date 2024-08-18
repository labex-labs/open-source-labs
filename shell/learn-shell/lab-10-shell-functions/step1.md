# Creating Your First Shell Function

Let's start by creating a simple shell function. Shell functions are like mini-scripts within a larger script, allowing you to group commands that perform a specific task.

First, we need to create a new file. Open your terminal and type:

```bash
cd ~/project
nano functions.sh
```

This command changes to the `project` directory and opens a new file named `functions.sh` in the nano text editor.

Now, let's add our first function. Type the following into the nano editor:

```bash
#!/bin/bash

# This is a simple function
greet() {
  echo "Hello, World!"
}

# This line calls (runs) the function
greet
```

Let's break this down:

- The first line `#!/bin/bash` is called a shebang. It tells the system to use bash to interpret this script.
- We define our function with `greet() { }`. Everything between the curly braces is part of the function.
- Inside the function, we have a simple `echo` command that prints "Hello, World!".
- The last line `greet` calls (runs) our function.

To save the file, press `Ctrl+X`, then `Y`, then `Enter`.

Now, let's make our script executable and run it:

```bash
chmod +x functions.sh
./functions.sh
```

You should see:

```
Hello, World!
```

If you don't see this output, double-check that you've typed everything correctly in the `functions.sh` file.
