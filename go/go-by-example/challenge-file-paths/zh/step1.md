# 文件路径

在这个挑战中，你需要使用 `filepath` 包对文件路径执行各种操作，例如以可移植的方式构建路径、将路径拆分为目录和文件组件、检查路径是否为绝对路径、查找文件的扩展名以及查找两条路径之间的相对路径。

## 要求

- 使用 `Join` 以可移植的方式构建路径。
- 使用 `Dir` 和 `Base` 将路径拆分为目录和文件组件。
- 使用 `IsAbs` 检查路径是否为绝对路径。
- 使用 `Ext` 查找文件的扩展名。
- 使用 `TrimSuffix` 从文件名中移除扩展名。
- 使用 `Rel` 查找两条路径之间的相对路径。

## 示例

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```
