# Delete a File

## Problem

You need to delete a file using Bash. The file name will be provided by the user, and the script should prompt for confirmation before deleting the file.

## Requirements

To complete this challenge, you need to have a basic understanding of Bash scripting and file management. You should also have access to a Linux or Unix-based operating system.

To delete a file using Bash, you can use the `rm` command followed by the file name. To prompt for confirmation before deleting the file, you can use the `-i` option with the `rm` command.

## Example

To run the script, use the following command:

```bash
bash delete_file.sh
```

Output:

```bash
Enter filename to remove
example.txt
rm: remove regular file 'example.txt'? y
```
