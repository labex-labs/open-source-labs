# Execute the script with arguments

Now that our script is executable, let's run it with some arguments. In the terminal, execute the following command:

```bash
./arguments.sh hello world example
```

You should see output similar to this:

```
Script name: ./arguments.sh
First argument: hello
Second argument: world
Third argument: example
```

This output shows that our script successfully accessed and displayed the command-line arguments.

For beginners:

- The `./` before the script name tells bash to look for the script in the current directory.
- Each word after the script name becomes a separate argument. In this case, "hello" is the first argument, "world" is the second, and "example" is the third.
- If you want to pass an argument with spaces, you need to use quotes, like this: `./arguments.sh "hello world" example`
