# Modify the Trap to Use a Function

Instead of using a simple function, let's modify our script to use a more complex function with the `trap` command. This allows us to perform more detailed actions when a signal is received.

1. Open the `trap_example.sh` file in the WebIDE editor.

2. Replace the content of the file with the following:

   ```bash
   #!/bin/bash
   
   cleanup_and_exit() {
     echo -e "\nSignal received! Cleaning up..."
     echo "Performing cleanup tasks..."
     # Add any necessary cleanup code here
     echo "Cleanup completed."
     echo "Exiting script gracefully."
     exit 0
   }
   
   trap cleanup_and_exit SIGINT SIGTERM
   
   echo "This script will run until you press Ctrl+C."
   echo "Press Ctrl+C to see the trap function in action and exit gracefully."
   
   count=1
   while true; do
     echo "Script is running... (iteration $count)"
     sleep 1
     ((count++))
   done
   ```

   Let's examine the changes:

   - We've expanded the `cleanup_and_exit` function to include more detailed messages and a placeholder for cleanup tasks.
   - The function now simulates a more realistic cleanup process, which could include tasks like closing file handles, removing temporary files, or releasing other resources.
   - We've updated the main loop to show an iteration count, making it clearer that the script is actively running.

3. Save the file after making these changes.

4. Run the script again and test it by pressing Ctrl+C:

   ```bash
   ~/project/trap_example.sh
   ```

   You should see the new messages from the `cleanup_and_exit` function when you interrupt the script, demonstrating a graceful exit.
