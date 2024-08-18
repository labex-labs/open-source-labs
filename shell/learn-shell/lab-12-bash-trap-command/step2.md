# Implement a Basic Trap Command

Now, let's implement a basic `trap` command in our script to catch specific signals.

1. Add the following content to the `trap_example.sh` file:

   ```bash
   #!/bin/bash
   
   trap "echo Signal received!" SIGINT SIGTERM
   
   echo "This script will run until you press Ctrl+C."
   echo "Press Ctrl+C to see the trap in action."
   
   while true; do
     sleep 1
   done
   ```

   Let's break down this script:

   - The first line `#!/bin/bash` is called a shebang. It tells the system that this script should be executed by the Bash shell.

   - The `trap` command is set up to echo "Signal received!" when it catches either SIGINT (interrupt) or SIGTERM (termination) signals. SIGINT is typically sent when you press Ctrl+C, while SIGTERM is often used when a process is asked to terminate gracefully.

   - The `echo` commands print instructions for the user.

   - The `while true; do` creates an infinite loop. This keeps our script running so we can test the trap.

   - `sleep 1` pauses the script for 1 second in each iteration of the loop. This prevents the script from consuming too much CPU time.

2. Save the file after adding the content. In most text editors, you can do this by pressing Ctrl+S or by clicking on a "Save" button.
