# Command Substitution

Command substitution allows you to use the output of a command as the value of a variable. This is done by enclosing the command with `$()` or backticks (``).

1. Open the `variables.sh` file in the WebIDE.

2. Add the following content to the end of the file:

   ```bash
   # Command substitution
   CURRENT_DATE=$(date +"%Y-%m-%d")
   echo "Today's date is: $CURRENT_DATE"
   
   FILES_IN_DIR=$(ls)
   echo "Files in the current directory:"
   echo "$FILES_IN_DIR"
   
   UPTIME=$(uptime -p)
   echo "System uptime: $UPTIME"
   ```

3. Save the file.

4. Run the script:

   ```bash
   ./variables.sh
   ```

   You should see output similar to this (the actual values will depend on your system):

   ```
   Today's date is: 2023-08-16
   Files in the current directory:
   variables.sh
   System uptime: up 2 hours, 15 minutes
   ```

   In this example:

   - `$(date +"%Y-%m-%d")` runs the `date` command and captures its output.
   - `$(ls)` runs the `ls` command and captures its output.
   - `$(uptime -p)` runs the `uptime` command with the `-p` option and captures its output.
