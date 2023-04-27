# Copy a File from Another Branch

You are working on a project in a Git repository named `https://github.com/labex-labs/git-playground`. You have two branches named `feature-1` and `feature-2`. You need to copy the file `index.html` from `feature-1` branch to `feature-2` branch.

1. Clone the repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Change to the repository directory:

```shell
cd git-playground
```

3. Switch to `feature-2` branch:

```shell
git checkout feature-2
```

4. Copy the `index.html` file from `feature-1` branch to `feature-2` branch:

```shell
git checkout feature-1 index.html
```

5. Verify that the `index.html` file has been copied to `feature-2` branch:

```shell
ls
```

You should see `index.html` file in the list of files.
