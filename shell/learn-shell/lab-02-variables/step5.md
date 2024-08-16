# Using Environment Variables

Environment variables are a type of variable that is available to all processes running in the current shell session. Let's explore some common environment variables and how to create our own.

1. Create a new file named `environment.sh` in the `/home/labex/project` directory:

   ```bash
   touch /home/labex/project/environment.sh
   ```

2. Open the `environment.sh` file in the WebIDE and add the following content:

   ```bash
   #!/bin/bash
   
   # Displaying some common environment variables
   echo "Home directory: $HOME"
   echo "Current user: $LOGNAME"
   echo "Shell being used: $SHELL"
   echo "Current PATH: $PATH"
   
   # Creating a new environment variable
   export MY_VARIABLE="Hello from my variable"
   
   # Displaying the new variable
   echo "My new variable: $MY_VARIABLE"
   
   # Creating a child process to demonstrate variable scope
   bash -c 'echo "MY_VARIABLE in child process: $MY_VARIABLE"'
   
   # Removing the environment variable
   unset MY_VARIABLE
   
   # Verifying the variable is unset
   echo "MY_VARIABLE after unsetting: $MY_VARIABLE"
   ```

3. Save the file.

4. Make the script executable:

   ```bash
   chmod +x /home/labex/project/environment.sh
   ```

5. Run the script:

   ```bash
   ./environment.sh
   ```

   You should see output similar to this (the actual values will depend on your system):

   ```
   Home directory: /home/labex
   Current user: labex
   Shell being used: /bin/zsh
   Current PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
   My new variable: Hello from my variable
   MY_VARIABLE in child process: Hello from my variable
   MY_VARIABLE after unsetting:
   ```

   This script demonstrates how to access existing environment variables, create new ones, and remove them.
