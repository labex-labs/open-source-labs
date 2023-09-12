# Use the $# variable

The $# variable holds the number of arguments passed to the script. You can use it to check the number of arguments and perform different actions based on that.

```shell
#!/bin/bash
if [ $# -eq 0 ]; then
    echo "No arguments passed."
elif [ $# -eq 1 ]; then
    echo "Only one argument passed."
else
    echo "Multiple arguments passed."
fi
```
