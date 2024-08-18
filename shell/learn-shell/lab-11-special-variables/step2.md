# Running the Script with Arguments

Now that we have created our script, let's run it with different arguments to see how the special variables behave.

1. Run the script without any arguments:

```bash
./special_vars.sh
```

The `./` before the script name tells the shell to look for the script in the current directory.

You should see output similar to this:

```
Script Name: ./special_vars.sh
First Argument:
Second Argument:
All Arguments:
Number of Arguments: 0
Process ID: 1234
```

Notice that the first and second arguments are empty, and the number of arguments is 0 since we didn't provide any.

2. Now, run the script with some arguments:

```bash
./special_vars.sh hello world
```

The output should look like this:

```
Script Name: ./special_vars.sh
First Argument: hello
Second Argument: world
All Arguments: hello world
Number of Arguments: 2
Process ID: 1235
```

Here's what changed:

- `$1` now contains "hello"
- `$2` now contains "world"
- `$@` shows all arguments: "hello world"
- `$#` shows 2, because we provided two arguments

The Process ID (`$$`) might be different each time you run the script, as it's assigned by the operating system.
