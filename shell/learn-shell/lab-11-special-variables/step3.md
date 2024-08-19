# Understanding $? and $

Two other important special variables are `$?` and `$!`. Let's create a new script to demonstrate their use.

1. Create a new file named `exit_status.sh`:

```bash
touch ~/project/exit_status.sh
```

2. Open the file in the WebIDE editor and add the following content:

```bash
#!/bin/bash

echo "Running a successful command:"
ls /home
echo "Exit status: $?"

echo "Running a command that will fail:"
ls /nonexistent_directory
echo "Exit status: $?"

echo "Running a background process:"
sleep 2 &
echo "Process ID of last background command: $!"
```

Let's break down this script:

- `$?` gives the exit status of the last executed command. 0 typically means success, while non-zero values indicate various error conditions.
- `$!` gives the process ID of the last background command.
- The `&` at the end of a command runs it in the background.

3. Save the file and make it executable:

```bash
chmod +x ~/project/exit_status.sh
```

4. Run the script:

```bash
./exit_status.sh
```

You should see output similar to this:

```
Running a successful command:
labex
Exit status: 0
Running a command that will fail:
ls: cannot access '/nonexistent_directory': No such file or directory
Exit status: 2
Running a background process:
Process ID of last background command: 1236
```

Notice:

- The first `ls` command succeeds, so `$?` is 0.
- The second `ls` command fails (because the directory doesn't exist), so `$?` is 2 (a non-zero value indicating an error).
- The `sleep` command runs in the background, and `$!` gives its process ID.
