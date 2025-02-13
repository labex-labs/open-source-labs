# Configure Line Endings

You are working on a project with a team of developers, and you notice that some team members are using different line endings than others. This can cause issues when merging code and can lead to conflicts. You need to configure the line endings for the repository to ensure consistency and avoid conflicts.

## Tasks

To configure the line endings for the `git-playground` repository, follow these steps:

1. Navigate to the directory where the `git-playground` repository is located (`~/project/git-playground`).
2. Configure the line endings to use UNIX line endings (`\n`).
3. Verify that the line endings have been configured correctly.

## Example

To verify that the line endings have been configured correctly, you can use the following command:

```bash
git config --get core.eol
```

If the line endings have been configured correctly, the command will return `lf`.

![Git line endings configuration](./assets/20240702-15-01-34-S4a8vHzh@2x.png)
