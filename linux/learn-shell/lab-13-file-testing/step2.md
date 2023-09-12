# Test if a directory exists

To test if a directory exists, you can use the `-d` command. This command checks if a directory exists. If the directory exists, it will return true; otherwise, it will return false.

```shell
#!/bin/bash
directory_name="test_directory"
if [ -d "$directory_name" ]; then
    echo "$directory_name exists as a directory"
fi
```
