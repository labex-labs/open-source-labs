# Make the Script Executable

Before we can run our script, we need to make it executable. In Unix-like systems, files have permissions that control who can read, write, or execute them. By default, new files are not executable.

To make our script executable, we use the `chmod` command (which stands for "change mode"). Type the following command in the terminal and press Enter:

```bash
chmod +x hello.sh
```

Here's what this command does:

- `chmod` is the command to change file permissions
- `+x` means "add execute permission"
- `hello.sh` is the name of our file

You won't see any output from this command if it's successful.
