# Make the Script Executable and Run It

Before we can run our script, we need to make it executable. This tells the system that this file is allowed to be run as a program.

1. In the terminal, make the script executable:

   ```bash
   chmod +x ~/project/trap_example.sh
   ```

   The `chmod` command changes the permissions of a file. The `+x` option adds execute permission.

2. Run the script:

   ```bash
   ~/project/trap_example.sh
   ```

   This command tells Bash to execute our script.

3. The script will start running. You'll see the instructions printed on the screen. Let it run for a few seconds.

4. Now, press Ctrl+C to interrupt it. You should see the message "Signal received!" before the script exits. This is our trap in action!

5. If the script doesn't exit after the first Ctrl+C (which can happen depending on how the terminal handles signals), press Ctrl+C again to stop the script completely.
