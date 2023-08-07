# Configure the git text editor

For this lab, let's use the repository from `https://github.com/labex-labs/git-playground`. You want to configure the text editor used by Git to your preferred editor.

1. Clone the `git-playground` repository:

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Navigate to the cloned repository and configure the identity:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Configure Git to use your preferred text editor (in this example, we will use vim):

```shell
git config --global core.editor "vim"
```

4. Make a change to a file and stage it for commit:

```shell
echo "Hello, Git" > hello.txt
git add hello.txt
```

5. Commit the change:

```shell
git commit
```

6. Your preferred text editor (in this example, vim) should open with the commit message. Write down your commit message "Update hello.txt" and save the file.
7. Close the text editor. The commit will be made with the message you wrote.

This is the finished result:

```shell
commit 1f19499s5387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Update hello.txt
```
