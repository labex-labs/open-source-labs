# Optimize the Local Repository

Over time, your Git repository can become cluttered with old versions of files and other unnecessary data. This can slow down Git and make it harder to work with your repository. To optimize your local repository, you need to remove this unnecessary data. This can be done using the `git gc` command.

The `git gc` command stands for "Git garbage collector". It is used to clean up unnecessary data in your repository. When you run `git gc`, Git will remove any loose objects (objects that are not referenced by any branch or tag) and pack the remaining objects into a new set of pack files. This can significantly reduce the size of your repository and improve Git's performance.

To optimize the local repository, you can use the `git gc` command with the `--prune=now` and `--aggressive` options. For example, let's say you have a Git repository named `git-playground` located in your home directory. To optimize this repository, you would run the following command:

```shell
cd git-playground
git gc --prune=now --aggressive
```

This is the result of optimising the `git-playground` repository by removing all loose objects and packing the remaining objects into a new set of pack files:

![<result>](assets/challenge-optimize-repository-step1-1.png)
