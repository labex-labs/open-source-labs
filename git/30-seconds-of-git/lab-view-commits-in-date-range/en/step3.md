# Viewing Commits in a Specific Date Range

Now we will learn how to filter commits based on specific dates. Git provides two useful options for this purpose:

- `--since` or `--after`: Shows commits more recent than a specific date
- `--until` or `--before`: Shows commits older than a specific date

When we combine these options, we can view commits within a specific date range.

Let's view all commits that occurred between April 25, 2023, and April 27, 2023:

```bash
git log --since='Apr 25 2023' --until='Apr 27 2023'
```

This command will display all commits that were made between April 25 and April 27, 2023. The output should look like this:

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

Git accepts many date formats, including:

- `"YYYY-MM-DD"` (e.g., `2023-04-25`)
- `"Month DD YYYY"` (e.g., `Apr 25 2023`)
- `"DD Month YYYY"` (e.g., `25 Apr 2023`)

Try another date format to see if there are any commits within a different range:

```bash
git log --since='2023-04-20' --until='2023-04-24'
```

This command might not return any results if there were no commits during that period, which is perfectly normal.
