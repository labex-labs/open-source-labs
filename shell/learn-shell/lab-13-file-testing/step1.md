# Understanding the Working Environment

Before we begin with file operations, it's important to understand our working environment. In Linux, you're always working within a specific directory, and it's crucial to know where you are in the file system.

1. Open a terminal in the WebIDE. This is where you'll type your commands.

2. Check your current working directory:

   ```bash
   pwd
   ```

   You should see `/home/labex/project` as the output. This command, `pwd`, stands for "print working directory" and shows you where you are in the file system.

3. List the contents of the current directory:

   ```bash
   ls -la
   ```

   This command will show all files and directories, including hidden ones, in your current location. The `-l` option gives a long format listing, and `-a` shows all files, including hidden ones (those starting with a dot).

   Don't worry if you see only a few items or even nothing at all. That's normal in a fresh project directory.
