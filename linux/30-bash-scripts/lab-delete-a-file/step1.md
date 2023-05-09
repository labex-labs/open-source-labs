# Delete a File

## Problem

You need to delete a file using Bash. The file name will be provided by the user, and the script should prompt for confirmation before deleting the file.

## Requirements

To complete this challenge, you need to have a basic understanding of Bash scripting and file management. You should also have access to a Linux or Unix-based operating system.

To delete a file using Bash, you can use the `rm` command followed by the file name. To prompt for confirmation before deleting the file, you can use the `-i` option with the `rm` command.

## Solution

Create a file named `delete_file.sh` with the following code:

```bash
#!/bin/bash
echo "Enter filename to remove"
read fn
rm -i $fn
```

Save the file and run it using the following commands:

```bash
ls
bash delete_file.sh
ls
```

The script will prompt you to enter the filename you want to delete. Once you enter the filename, it will ask for confirmation before deleting the file.
