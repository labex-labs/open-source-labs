# Read a File

## Problem

You have a file named 'book.txt' that contains some text. Your task is to read the contents of this file line by line and display them on the terminal.

## Requirements

- Create a Bash script named 'read_file.sh'.
- Use a loop to read the file line by line.
- Display each line on the terminal.
- The file name should be stored in a variable.
- The script should be executable.
- The original content of the file should be checked using the 'cat' command.

## Solution

To solve this problem, we can create a Bash script named 'read_file.sh' and use a loop to read the file line by line. The file name should be stored in a variable for easy modification. Here's the code:

```bash
#!/bin/bash  
file='book.txt'  
while read line; do  
echo $line  
done < $file
```

To run the script, use the following command:

```bash
bash read_file.sh
```

To check the original content of the file, use the 'cat' command:

```bash
cat book.txt
```

