# Implement a Basic Trap Command

Now, let's implement a basic `trap` command in our script to catch specific signals and exit gracefully.

1. Add the following content to the `trap_example.sh` file:

   ```bash
   #!/bin/bash
   
   cleanup_and_exit() {
     echo -e "\nSignal received! Cleaning up and exiting..."
     exit 0
   }
   
   trap cleanup_and_exit SIGINT SIGTERM
   
   echo "This script will run until you press Ctrl+C."
   echo "Press Ctrl+C to see the trap in action and exit gracefully."
   
   count=1
   while true; do
     echo "Script is running... (iteration $count)"
     sleep 1
     ((count++))
   done
   ```

   Let's break down this script:

   - The first line `#!/bin/bash` is called a shebang. It tells the system that this script should be executed by the Bash shell.
   - We define a `cleanup_and_exit` function that prints a message and exits the script.
   - The `trap` command is set up to call `cleanup_and_exit` when it catches either SIGINT (interrupt) or SIGTERM (termination) signals. SIGINT is typically sent when you press Ctrl+C, while SIGTERM is often used when a process is asked to terminate gracefully.
   - The `echo` commands print instructions for the user.
   - The `while` loop runs indefinitely, printing a message and incrementing a counter every second.

2. Save the file after adding the content.
