# Find the Commit that Introduced a Bug

Your task is to use Git's `bisect` command to find the commit that introduced a bug in the `https://github.com/labex-labs/git-playground` repository. The bug causes the `npm test` command to fail.

1. Run `git clone https://github.com/username/git-playground.git` to clone the `https://github.com/labex-labs/git-playground` repository.
2. Run `npm install` to install the project dependencies.
3. Run `npm test` to see the failing test.
4. Use `git bisect start` to start the `bisect` process.
5. Use the git log --full-history command to see the full history of commits.
6. Use `git bisect good d22f46ba8c2d4e07d773c5126e9c803933eb5898` to mark a `<commit>` as "good", indicating it is known to be bug-free.
7. Use `git bisect bad b00b9374a7c549d1af111aa777fdcc868d8a2a01` to mark a different `<commit>` as "bad" indicating it has the bug.
8. Use `git bisect run npm test` to run the `npm test` command on each subsequent commit to find which commit introduce the bug.
9. Once the bad commit is found, use `git bisect reset` to reset to the original branch.