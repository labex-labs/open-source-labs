# Testing File Existence

Now that we have created a file, let's learn how to check if a file exists. This is a common task in shell scripts, especially when you need to perform operations on files.

1. Create a new script file named `file_exists.sh`:

   ```bash
   touch file_exists.sh
   ```

2. Add the following content to the file:

   ```bash
   #!/bin/bash
   
   filename="test_file.txt"
   if [ -e "$filename" ]; then
     echo "$filename exists"
   else
     echo "$filename does not exist"
   fi
   ```

   Let's break this down:

   - `#!/bin/bash` is called a shebang. It tells the system this is a bash script.
   - We set a variable `filename` to "test_file.txt".
   - The `if` statement checks if the file exists. `-e` is a test that returns true if the file exists.
   - We use `echo` to print a message based on whether the file exists or not.

3. Save the file and exit the editor.

4. Make the script executable:

   ```bash
   chmod +x file_exists.sh
   ```

   `chmod` changes the permissions of a file. `+x` adds executable permissions.

5. Run the script:

   ```bash
   ./file_exists.sh
   ```

   You should see the output: "test_file.txt exists"

6. Now, let's test with a non-existent file. Modify the script to check for a file named "non_existent.txt":

   Change the `filename` variable to "non_existent.txt".

7. Run the script again:

   ```bash
   ./file_exists.sh
   ```

   You should see the output: "non_existent.txt does not exist"

This script demonstrates how to check for file existence, which is crucial when your script needs to work with files that may or may not be present.
