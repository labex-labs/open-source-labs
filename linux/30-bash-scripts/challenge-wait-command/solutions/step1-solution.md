## Solution

Here is an example script that demonstrates the use of the **wait** command:

```bash
#!/bin/bash
echo "Wait command" &
process_id=$!
wait $process_id
echo "Exited with status $?"
```

To run the script, save it as **wait_example.sh** and execute the following command in the terminal:

```bash
bash wait_example.sh
```

The script will print "Wait command" to the console, run a process in the background, wait for the process to complete, and print the exit status of the process.
