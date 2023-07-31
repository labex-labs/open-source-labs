# View Commits by Author

Your task is to retrieve all commits made by a specific author in the `git-playground` repository. This repository contains a collection of sample projects that you can use to practice your Git skills.

To complete this lab, you will need to use the `git log` command with the `--author` option. This will allow you to filter the commit history to only show commits made by the specified author.

To retrieve all commits made by the author "Hang" in the `git-playground` repository, you can use the following command:
```shell
git log --author="Hang"
```

This will output a list of all commits made by "Hang" in the repository, along with information about the commit message, date, and other details:
```shell
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/
master, origin/feature-branch, origin/HEAD)
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
