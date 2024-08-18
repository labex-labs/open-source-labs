# Creating a Test File

Now that we know where we are, let's create a test file that we'll use throughout this lab.

1. Create a new file named `test_file.txt`:

   ```bash
   touch test_file.txt
   ```

   The `touch` command is used to create an empty file. If the file already exists, it updates the file's timestamp without changing its content.

2. Add some content to the file:

   ```bash
   echo "This is a test file for our lab." > test_file.txt
   ```

   This command uses `echo` to output the text, and `>` to redirect that output into the file. Be careful with `>`, as it will overwrite any existing content in the file.

3. Verify the file contents:

   ```bash
   cat test_file.txt
   ```

   `cat` is short for "concatenate", but it's often used to display the contents of a file. You should see the message "This is a test file for our lab."

If you make a mistake or want to start over, you can always remove the file with `rm test_file.txt` and start again from step 1.
