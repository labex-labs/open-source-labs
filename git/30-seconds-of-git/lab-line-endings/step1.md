# Configure Line Endings

You are working on a project with a team of developers, and you notice that some team members are using different line endings than others. This can cause issues when merging code and can lead to conflicts. You need to configure the line endings for the repository to ensure consistency and avoid conflicts.

On Unix or Unix-like systems, every line of text ends with the line terminator `LF` (Line Feed). When you use the cat command to view a file, line terminators are not normally displayed on the screen because they are considered to be the end of the line, not part of the line.

When viewing a file with the `cat -vet` command, the `-v` option displays non-printing characters as visible character sequences, such as the `$` symbol. Therefore, if you see the `$` symbol in a file, it means that every line in the file ends with the line terminator `LF`. `LF` and `\n` are the same concept, indicating a line terminator.

To configure the line endings for the `git-playground` repository, follow these steps:

1. Open the command prompt or terminal on your computer.
2. Navigate to the directory where the `git-playground` repository is located in the `~/project` directory.
3. Run the following command to configure the line endings to use UNIX line endings:

   ```shell
   git config core.eol lf
   ```

   This will configure the line endings to use the UNIX line ending (`\n`).

4. Run the following command to verify that the line endings have been configured correctly:

   ```shell
   git config core.eol
   ```

   This will display the current line ending configuration.

This is the result of running `cat -vet file2.txt`:

```shell
This is file2.$
```
