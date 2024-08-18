# Modify the Trap to Use a Function

Instead of using an inline command, let's modify our script to use a function with the `trap` command. This allows us to perform more complex actions when a signal is received.

1. Open the `trap_example.sh` file in the WebIDE editor.

2. Replace the content of the file with the following:

   ```bash
   #!/bin/bash
   
   handle_signal() {
     echo "Signal received! Cleaning up..."
     echo "Exiting script."
     exit 0
   }
   
   trap handle_signal SIGINT SIGTERM
   
   echo "This script will run until you press Ctrl+C."
   echo "Press Ctrl+C to see the trap function in action."
   
   while true; do
     sleep 1
   done
   ```

   Let's examine the changes:

   - We've defined a function called `handle_signal`. In Bash, you define a function by writing its name followed by parentheses `()`.

   - Inside the function, we echo two messages and then use `exit 0` to end the script. The `0` means the script ended successfully.

   - We've updated the `trap` command to call our `handle_signal` function instead of just echoing a message.

3. Save the file after making these changes.

4. Run the script again and test it by pressing Ctrl+C:

   ```bash
   ~/project/trap_example.sh
   ```

   You should see the new messages from the `handle_signal` function when you interrupt the script.
