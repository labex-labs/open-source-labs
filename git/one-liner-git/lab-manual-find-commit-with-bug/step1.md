# Manually Find the Commit that Introduced a Bug

Your task is to manually find the commit that introduced a bug in the `git-playground` repository. The repository can be found at `https://github.com/labex-labs/git-playground`. The bug is a syntax error in the `main.py` file that causes the program to crash when run.

To complete this challenge, you will need to use the `git bisect` command to perform a binary search through the commit history of the repository. You will need to mark commits as either "good" (bug-free) or "bad" (buggy) until you have narrowed down the commit that introduced the bug.

1. Clone the `git-playground` repository:

```
git clone https://github.com/labex-labs/git-playground
```

2. Change into the repository directory:

```
cd git-playground
```

3. Start the `git bisect` process:

```
git bisect start
```

4. Mark the current commit as "bad":

```
git bisect bad HEAD
```

5. Mark an earlier commit as "good":

```
git bisect good 3050fc0de
```

6. Git will automatically checkout a new commit for you to test. Run the program to see if it is buggy:

```
python main.py
```

7. If the program runs without error, mark the current commit as "good":

```
git bisect good
```

8. If the program crashes, mark the current commit as "bad":

```
git bisect bad
```

9. Repeat steps 6-8 until you have narrowed down the commit that introduced the bug.
10. Once you have found the buggy commit, reset the `git bisect` process:

```
git bisect reset
```

11. You can now examine the code changes in the buggy commit to find the source of the bug.
