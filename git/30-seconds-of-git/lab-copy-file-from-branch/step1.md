# Copy a File from Another Branch

You are working on a project in a Git repository named `https://github.com/your-username/git-playground`. You have two branches named `feature-1` and `feature-2`. You need to copy the file `hello.txt` from `feature-1` branch to `feature-2` branch.

1. Clone the repository:
```shell
git clone https://github.com/your-username/git-playground.git
```
2. Navigate to the directory and configure the identity:
```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```
3. Create and switch to `feature-1` branch and create a text file named `hello.txt` and write the string "hello,world" to it and commit the file with the message "add hello.txt":
```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```
4. Create and switch to `feature-2` branch after switching to `master` branch:
```shell
git checkout master
git checkout -b feature-2
```
5. Copy the `hello.txt` file from the `feature-1` branch to the `feature-2` branch and commit it with the commit message "copy hello.txt":
```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```
6. Verify that the `hello.txt` file has been copied to `feature-2` branch:
```shell
ll
```

You should see the `hello.txt` file in the list of files in the `feature-2` branch:
```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
