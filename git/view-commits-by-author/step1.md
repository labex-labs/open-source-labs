# Git Challenge: View Commits by Author

## Problem

Your task is to retrieve all commits made by a specific author in the `git-playground` repository. This repository contains a collection of sample projects that you can use to practice your Git skills.

To complete this challenge, you will need to use the `git log` command with the `--author` option. This will allow you to filter the commit history to only show commits made by the specified author.

## Example

To retrieve all commits made by the author "John Doe" in the `git-playground` repository, you can use the following command:

```shell
git log --author="John Doe"
```

This will output a list of all commits made by "John Doe" in the repository, along with information about the commit message, date, and other details.

```shell
commit 6a3c9a9f6c9e8c8b7e8d6c4f6a7c8d2d7a8c9a9f
Author: John Doe <johndoe@example.com>
Date:   Mon Apr 5 14:22:45 2021 -0400

    Updated README.md file

commit 4d6c9a9f6c9e8c8b7e8d6c4f6a7c8d2d7a8c9a9f
Author: John Doe <johndoe@example.com>
Date:   Fri Apr 2 09:15:23 2021 -0400

    Added new feature to project

commit 2a3c9a9f6c9e8c8b7e8d6c4f6a7c8d2d7a8c9a9f
Author: John Doe <johndoe@example.com>
Date:   Wed Mar 31 16:38:12 2021 -0400

    Initial commit of project
```
