# Configure Line Endings

You are working on a project with a team of developers, and you notice that some team members are using different line endings than others. This can cause issues when merging code and can lead to conflicts. You need to configure the line endings for the repository to ensure consistency and avoid conflicts.

## Tasks

To configure the line endings for the `git-playground` repository, follow these steps:

1. Open the command prompt or terminal on your computer.
2. Navigate to the directory where the `git-playground` repository is located.
3. Configure the line endings to use UNIX line endings (`\n`).
4. Verify that the line endings have been configured correctly.

To verify that the line endings have been configured correctly, you can use the following command:

```bash
git config --get core.eol
```

If the line endings have been configured correctly, the command will return `lf`.
