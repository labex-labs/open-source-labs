---
title: Clone a repository
---

Clones an existing repository, creating a local copy of it.

- Use `git clone <url>` to clone an existing repository from `<url>` to a local directory. The directory's name will be based on the name of the cloned repository.
- Alternatively, use `git clone <url> [<directory>]` to clone the repository into the specified local `<directory>`.

```shell
git clone < url > [ < directory > ]
```

```shell
git clone https://github.com/labex-labs/git-playground.git
# Clones the repository in a new directory named 'git-playground'
cd git-playground

git clone https://github.com/labex-labs/git-playground.git my-project
# Clones the repository in a new directory named 'my-project'
cd my-project
```
