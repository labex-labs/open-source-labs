# Configure Line Endings

You are working on a project with a team of developers, and you notice that some team members are using different line endings than others. This can cause issues when merging code and can lead to conflicts. You need to configure the line endings for the repository to ensure consistency and avoid conflicts.

To configure the line endings for the `git-playground` repository, follow these steps:

1. Open the command prompt or terminal on your computer.
2. Navigate to the directory where the `git-playground` repository is located.
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
