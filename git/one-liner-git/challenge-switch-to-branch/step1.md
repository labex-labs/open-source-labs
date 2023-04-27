# Switch to a Branch

## Problem

You have been working on a project in a Git repository named `https://github.com/labex-labs/git-playground`. Your team has created a new branch named `feature-1` to work on a new feature. You need to switch to the `feature-1` branch to continue working on the feature.

## Example

1. Clone the Git repository:

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the repository directory:

```
cd git-playground
```

3. List all the branches in the repository:

```
git branch
```

Output:

```
* main
  patch-1
```

4. Switch to the `feature-1` branch:

```
git checkout feature-1
```

Output:

```
Switched to branch 'feature-1'
```

5. Verify that you are now on the `feature-1` branch:

```
git branch
```

Output:

```
  main
  patch-1
* feature-1
```
