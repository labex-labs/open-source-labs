# Use Signal Numbers in the Trap Command

Instead of using signal names, we can use their corresponding numbers in the `trap` command. This is sometimes preferred for portability, as signal numbers are standardized across POSIX systems.

1. In the terminal, run the following command to see a list of signal numbers:

   ```bash
   kill -l
   ```

   This command lists all available signals with their corresponding numbers. Look for SIGINT and SIGTERM in this list.

2. Modify the `trap_example.sh` file to use signal numbers. Replace the content with:

   ```bash
   #!/bin/bash
   
   handle_signal() {
     echo "Signal received! Cleaning up..."
     echo "Exiting script."
     exit 0
   }
   
   trap handle_signal 2 15
   
   echo "This script will run until you press Ctrl+C."
   echo "Press Ctrl+C to see the trap function in action."
   
   while true; do
     sleep 1
   done
   ```

   Here's what changed:

   - We replaced `SIGINT` with `2` and `SIGTERM` with `15`.
   - These numbers correspond to the SIGINT and SIGTERM signals, respectively. You can verify this in the output of the `kill -l` command.

3. Save the file after making these changes.

4. Run the script again and test it by pressing Ctrl+C:

   ```bash
   ~/project/trap_example.sh
   ```

   The behavior should be the same as before, but now we're using signal numbers instead of names.
