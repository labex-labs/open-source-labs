# Creating a Script File

Let's start by creating a script file where we'll write our string operations.

1. Open your terminal in the WebIDE. The terminal is where you'll type commands to interact with the Linux system.

2. Navigate to the project directory:

   ```bash
   cd ~/project
   ```

   This command changes your current directory to `~/project`. The `~` symbol represents your home directory, so `~/project` is a folder named "project" in your home directory.

3. Create a new file named `string_operations.sh`:

   ```bash
   touch string_operations.sh
   ```

   The `touch` command creates a new, empty file. If the file already exists, it updates the file's timestamp.

4. Open the file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of your WebIDE.

5. Add the following shebang line at the top of the file to specify the interpreter:

   ```bash
   #!/bin/bash
   ```

   This line, called a "shebang", tells the system to use the Bash shell to interpret this script. It's always the first line of a shell script.
