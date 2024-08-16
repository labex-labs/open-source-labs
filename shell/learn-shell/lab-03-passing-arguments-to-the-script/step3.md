# Make the script executable

Before we can run our script, we need to make it executable. This is done using the `chmod` command. In the terminal, navigate to the project directory and run the following command:

```bash
cd /home/labex/project
chmod +x arguments.sh
```

The `chmod +x` command adds execute permissions to the file, allowing it to be run as a script.

For beginners:

- `chmod` stands for "change mode". It's used to change the permissions of a file or directory.
- The `+x` option adds the execute permission. This is necessary for bash to be able to run the file as a script.
- If you forget this step, you'll get a "permission denied" error when trying to run your script.
