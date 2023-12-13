# Append to File

## Problem

Suppose we have a file named 'book.txt' and we want to add new content to it without deleting the existing content. We can achieve this by using the '>>' operator in Bash. The problem is to create a Bash script that appends new content to the end of the 'book.txt' file.

## Requirements

- Create a Bash script named 'append_file.sh'.
- The script should display the existing content of the 'book.txt' file before appending new content.
- The script should append the text 'Learning Laravel 5' to the end of the 'book.txt' file.
- The script should display the updated content of the 'book.txt' file after appending new content.

## Example

To run the script, use the following command:

```bash
bash append_file.sh
```

Output:

```bash
Before appending the file
This is the existing content of the 'book.txt' file.

After appending the file
This is the existing content of the 'book.txt' file.
Learning Laravel 5
```
