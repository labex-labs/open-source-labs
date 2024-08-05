# Shallow Clone with Depth

Sometimes, you might only need the most recent version of a repository without its full history. In such cases, you can perform a shallow clone using the `--depth` option.

Let's clone the repository again, but this time only fetch the most recent commit:

```bash
cd ~/project
git clone --depth 1 https://github.com/labex-labs/git-playground.git shallow-repo
```

This command creates a shallow clone with a history truncated to only the last commit. The `--depth 1` option tells Git to only fetch the most recent commit.

Shallow clones can be significantly faster and take up less disk space, which is particularly useful for large repositories when you don't need the full history.

To verify the shallow clone, navigate into the new directory and check the git log:

```bash
cd shallow-repo
git log --oneline
```

You should only see one commit in the log.

If you later decide you need more history, you can fetch it using:

```bash
git fetch --unshallow
```

This will retrieve the full history of the repository.
