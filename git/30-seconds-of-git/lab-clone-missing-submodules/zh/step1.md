# 克隆缺失的子模块

你正在处理一个包含子模块的项目。当你克隆该项目时，子模块不会自动被克隆。这在尝试构建或运行项目时会导致问题。你需要克隆缺失的子模块并检出正确的提交。

对于本实验，我们将使用名为 `https://github.com/git/git` 的 Git 仓库。该仓库包含一些在克隆仓库时不会自动被克隆的子模块。

要克隆缺失的子模块并检出正确的提交，请按照以下步骤操作：

1. 进入仓库目录：
   ```
   cd git
   ```
2. 初始化子模块：
   ```
   git submodule update --init --recursive
   ```
3. 检出子模块的正确提交，即 `master` 分支：
   ```
   git submodule foreach git checkout master
   ```
   以下是最终结果：

```shell
Submodule 'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
