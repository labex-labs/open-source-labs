# Test if a file is readable

To test if a file has read permission for the user running the script, you can use the `-r` command. This command checks if a file is readable. If the file is readable, it will return true; otherwise, it will return false. If the file doesn't exist, you can create it using the `touch` command.

```shell
#!/bin/bash
filename="sample.md"
if [ ! -f "$filename" ]; then
    touch "$filename" # Create the file if it doesn't exist
fi
if [ -r "$filename" ]; then
    echo "You are allowed to read $filename"
else
    echo "You are not allowed to read $filename"
fi
```
