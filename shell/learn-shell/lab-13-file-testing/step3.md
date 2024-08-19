# Testing Directory Existence

Similar to testing file existence, we can also check if a directory exists. This is useful when your script needs to work with directories that may or may not be present.

1. Create a new script file named `dir_exists.sh`:

   ```bash
   touch dir_exists.sh
   ```

2. Add the following content to the file:

   ```bash
   #!/bin/bash
   
   dirname="test_directory"
   if [ -d "$dirname" ]; then
     echo "$dirname exists"
   else
     echo "$dirname does not exist"
   fi
   ```

   This script is very similar to our file existence script, but it uses `-d` instead of `-e`. The `-d` test checks specifically for directory existence.

3. Save the file and exit the editor.

4. Make the script executable:

   ```bash
   chmod +x dir_exists.sh
   ```

5. Run the script:

   ```bash
   ./dir_exists.sh
   ```

   You should see the output: "test_directory does not exist"

6. Now, let's create the directory and run the script again:

   ```bash
   mkdir test_directory
   ./dir_exists.sh
   ```

   You should now see the output: "test_directory exists"

   `mkdir` is the command to create a new directory.

This script demonstrates how to check for directory existence. This can be particularly useful in scripts that need to create, modify, or delete directories.
