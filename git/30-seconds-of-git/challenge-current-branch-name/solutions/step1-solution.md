# Solutions

Here are a few ways to get the current branch name:

**Method 1: Using `git rev-parse`**

```shell
git rev-parse --abbrev-ref HEAD
```

**Method 2: Using `git symbolic-ref`**

```shell
git symbolic-ref --short HEAD
```

**Method 3: Using `git branch`**

```shell
git branch --show-current
```

**Method 4: Using `git status`**

```shell
git status | head -n 1 | awk '{print $3}'
```
