# Creating a Test File

Before we begin with file operations, it's important to understand our working environment. In Linux, you're always working within a specific directory, and it's crucial to know where you are in the file system.

1. Open a terminal in the WebIDE. This is where you'll type your commands.

2. Create a new file named `test_file.txt`:

   ```bash
   touch test_file.txt
   ```

   The `touch` command is used to create an empty file. If the file already exists, it updates the file's timestamp without changing its content.

3. Add some content to the file:

   ```bash
   echo "This is a test file for our lab." > test_file.txt
   ```

   This command uses `echo` to output the text, and `>` to redirect that output into the file. Be careful with `>`, as it will overwrite any existing content in the file.

4. Verify the file contents:

   ```bash
   cat test_file.txt
   ```

   `cat` is short for "concatenate", but it's often used to display the contents of a file. You should see the message "This is a test file for our lab."

If you make a mistake or want to start over, you can always remove the file with `rm test_file.txt` and start again from step 1.
