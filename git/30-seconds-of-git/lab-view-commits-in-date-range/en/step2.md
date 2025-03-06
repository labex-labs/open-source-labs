# Exploring Basic Git Log Command

Now that we have our repository cloned, let's learn how to view the commit history using the `git log` command.

The `git log` command displays a list of all commits in the repository, starting with the most recent one. Each commit entry includes:

- A unique commit hash (identifier)
- Author information
- Date and time of the commit
- Commit message

Let's view the basic commit history:

```bash
git log
```

You should see output similar to the following:

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

If the output is long, you can navigate through it using:

- Press `Space` to move forward
- Press `b` to move backward
- Press `q` to quit the log view

Note that each commit has a unique identifier (the long hexadecimal string), the author's information, the date and time of the commit, and a message describing what changes were made.
