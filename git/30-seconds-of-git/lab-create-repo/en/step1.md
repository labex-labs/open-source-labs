# Create a New Repository

We have learned how to clone an existing Git repository. Now, let's create a new Git repository from scratch.

Open your terminal or command prompt and follow the steps below to create a new Git repository:

```bash
cd ~/project
git init my_repo
```

This will create a new directory named `my_repo` in your current working directory and initialize a new Git repository inside it.

Let's see what inside the `my_repo` directory:

```bash
ls -a my_repo
```

You should see the following files and directories:

```plaintext
.  ..  .git
```

The `.` and `..` directories are special directories that represent the current directory and the parent directory, respectively.

The `.git` directory is where Git stores all the configuration files and version history for the repository.

Try running the following command to see the files and directories inside the `.git` directory:

```bash
ls -a my_repo/.git
```

You should see the following files and directories:

```plaintext
.  ..  branches  config  description  HEAD  hooks  info  objects  ref
```

- The `branches` directory contains references to the branches in the repository.
- The `config` file contains the repository-specific configuration settings.
- The `description` file contains a short description of the repository.
- The `HEAD` file contains a reference to the currently checked out branch.
- The `hooks` directory contains scripts that can be triggered by Git events.
- The `info` directory contains global information files.
- The `objects` directory contains all the objects in the repository.
- The `ref` directory contains references to the commits in the repository.

We don't need to worry about the contents of the `.git` directory for now. Just remember that it's where Git stores all the information about the repository.
