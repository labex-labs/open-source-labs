# Solution

Here is the Bash script that appends new content to the 'book.txt' file:

```bash
#!/bin/bash

echo "Before appending the file"
cat book.txt

echo "Learning Laravel 5" >> book.txt
echo "After appending the file"
cat book.txt
```

To run the script, use the following command:

```bash
bash append_file.sh
```
