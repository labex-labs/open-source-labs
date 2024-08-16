# Create a new Bash script

Let's start by creating a new Bash script file.

1. Open your terminal in the WebIDE. You should see a command prompt, which might look something like this: `labex@ubuntu:~/project$`.

2. We'll create our script in the `project` directory. You're already in this directory by default, but let's make sure by using the `cd` command:

   ```bash
   cd ~/project
   ```

   This command changes the current directory to `/home/labex/project`.

3. Now, let's create a new file named `fruit_basket.sh`. We'll use the `touch` command, which creates an empty file:

   ```bash
   touch fruit_basket.sh
   ```

4. Open the `fruit_basket.sh` file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of the WebIDE.

5. Every Bash script should start with a "shebang" line. This line tells the system which interpreter to use to run the script. Add the following line at the beginning of the file:

   ```bash
   #!/bin/bash
   ```

   This line specifies that the script should be run with the Bash interpreter.
