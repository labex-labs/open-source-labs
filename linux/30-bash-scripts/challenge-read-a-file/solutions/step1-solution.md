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
