# Creating Your First Script

Let's start by creating a simple shell script to demonstrate the use of special variables.

1. Open your terminal in the WebIDE. You should see a command prompt waiting for your input.

2. Navigate to the project directory:

```bash
cd ~/project
```

This command changes your current directory to `~/project`, which is your default working directory for this lab.

3. Create a new file named `special_vars.sh` using the following command:

```bash
touch special_vars.sh
```

The `touch` command creates an empty file if it doesn't exist, or updates its timestamp if it does.

4. Open the file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of your screen.

5. Add the following content to the file:

```bash
#!/bin/bash

echo "Script Name: $0"
echo "First Argument: $1"
echo "Second Argument: $2"
echo "All Arguments: $@"
echo "Number of Arguments: $#"
echo "Process ID: $$"
```

Let's break down what each line does:

- `#!/bin/bash`: This is called a shebang. It tells the system to use bash to interpret this script.
- `$0`: This special variable holds the name of the script.
- `$1` and `$2`: These represent the first and second command-line arguments respectively.
- `$@`: This represents all the command-line arguments passed to the script.
- `$#`: This gives the count of command-line arguments.
- `$$`: This provides the process ID of the current shell.

6. Save the file after adding the content.

7. Make the script executable by running the following command in your terminal:

```bash
chmod +x special_vars.sh
```

The `chmod` command changes the permissions of a file. The `+x` option adds execute permission, allowing you to run the script.
