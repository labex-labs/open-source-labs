# Using Relative Dates and Formatting Options

Git also supports relative dates, which can be very convenient for quickly viewing recent activity.

Let's view all commits from the last 12 weeks:

```bash
git log --since='12 weeks ago'
```

Depending on when you're running this command, you might see all commits or just some of them if they fall within that time frame.

Other useful relative date formats include:

- `"X days ago"`
- `"X months ago"`
- `"yesterday"`
- `"last week"`

Let's try viewing commits from the last year:

```bash
git log --since='1 year ago'
```

This command will show all commits made within the past year.

## Additional Formatting Options

Git log provides various formatting options to customize the output. Here are a few useful ones:

1. To display a more concise log with each commit on a single line:

```bash
git log --oneline --since='Apr 25 2023' --until='Apr 27 2023'
```

The output will look like:

```
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

2. To see the files that were changed in each commit:

```bash
git log --name-status --since='Apr 25 2023' --until='Apr 27 2023'
```

This command shows the status of files that were modified in each commit, which can be helpful for understanding what was changed.

These formatting options can be combined with date filters to create powerful queries that help you understand the history of a project more effectively.
