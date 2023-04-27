# Configure the git text editor

## Problem

You want to configure the text editor used by Git to your preferred editor.

## Example

1. Clone the `git-playground` repository:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navigate to the cloned repository:

```shell
cd git-playground
```

3. Configure Git to use your preferred text editor (in this example, we will use VS Code):

```shell
git config --global core.editor "code --wait"
```

4. Make a change to a file and stage it for commit:

```shell
echo "Hello, Git!" > hello.txt
git add hello.txt
```

5. Commit the change:

```shell
git commit
```

6. Your preferred text editor (in this example, VS Code) should open with the commit message. Write your commit message and save the file.

7. Close the text editor. The commit will be made with the message you wrote.
