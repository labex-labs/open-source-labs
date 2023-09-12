# Declare the Trap Command

Inside the `trap_example.sh` file, declare the `trap` command to catch specific signals and define the actions to be taken when those signals are received.

```bash
#!/bin/bash
# trap_example.sh

trap "echo Booh!" SIGINT SIGTERM
echo "The script will run until you hit Ctrl+Z."
echo "Hit Ctrl+C to display a message!"

while true
do
    sleep 60
done
```

In this example, we are catching the `SIGINT` (interrupt) and `SIGTERM` (termination) signals. When either of these signals is received, the script will execute the specified action, which, in this case, is to display the message `"Booh!"`.
