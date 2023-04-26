# Create a New Branch

## Problem

You are working on a project in a Git repository named `https://github.com/labex-labs/git-playground`. You need to create a new branch named `feature-1` to work on a new feature.

## Example

1. Clone the repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```shell
cd git-playground
```

3. Check the current branch:

```shell
git branch
```

4. Create a new branch named `feature-1`:

```shell
git checkout -b feature-1
```

5. Verify that you are now on the `feature-1` branch:

```shell
git branch
```

6. Make changes to the code and commit them:

```shell
git add .
git commit -m "Added new feature"
```

7. Push the changes to the remote repository:

```shell
git push -u origin feature-1
```
