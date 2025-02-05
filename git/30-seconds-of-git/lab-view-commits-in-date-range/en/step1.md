# View Commits in a Specific Date Range

Your task is to view all commits in a specific date range using Git. You will need to use the `git log` command with the `--since` and `--until` options to specify the date range. You can use either a specific date or a relative date (e.g. "12 weeks ago").

To complete this challenge, you will need to use the `https://github.com/labex-labs/git-playground` repository. Follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/labex-labs/git-playground`.
2. Navigate to the repository directory using the command `cd git-playground`.
3. Use the command `git log --since='Apr 25 2023' --until='Apr 27 2023'` to view all commits between April 25, 2023 and April 27, 2023.
4. Use the command `git log --since='12 weeks ago'` to view all commits made in the last twelve weeks.

This is the final result:

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
