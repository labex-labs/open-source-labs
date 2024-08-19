# Testing File Permissions

In Linux, every file and directory has associated permissions that determine who can read, write, or execute them. In this step, we'll learn how to check file permissions, specifically if a file is readable.

1. Create a new script file named `file_readable.sh`:
2. Add the following content to the file:

   ```bash
   #!/bin/bash
   
   filename="test_file.txt"
   if [ -r "$filename" ]; then
     echo "You have read permission for $filename"
   else
     echo "You do not have read permission for $filename"
   fi
   ```

   This script uses the `-r` test, which checks if the file is readable by the current user.

3. Save the file and exit the editor.

4. Make the script executable:

   ```bash
   chmod +x file_readable.sh
   ```

5. Run the script:

   ```bash
   ./file_readable.sh
   ```

   You should see the output: "You have read permission for test_file.txt"

6. Now, let's remove the read permission and run the script again:

   ```bash
   chmod -r test_file.txt
   ./file_readable.sh
   ```

   You should now see the output: "You do not have read permission for test_file.txt"

   `chmod -r` removes read permissions from the file.

7. Restore the read permission:

   ```bash
   chmod +r test_file.txt
   ```

   It's important to restore the permissions so we don't accidentally leave our file unreadable.

This script demonstrates how to check file permissions. Understanding and managing file permissions is crucial for system security and proper functioning of scripts.
