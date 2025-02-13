# 目录

创建一个 Go 程序，该程序在当前工作目录中创建一个新的子目录，创建一个包含父目录的目录层次结构，列出目录内容，更改当前工作目录，并递归访问一个目录。

## 要求

- 在当前工作目录中创建一个新的子目录。
- 创建临时目录时，最好使用 `defer` 来删除它们。`os.RemoveAll` 将删除整个目录树（类似于 `rm -rf`）。
- 使用 `MkdirAll` 创建一个包含父目录的目录层次结构。这类似于命令行中的 `mkdir -p`。
- `ReadDir` 列出目录内容，返回一个 `os.DirEntry` 对象的切片。
- `Chdir` 允许我们更改当前工作目录，类似于 `cd`。
- 递归访问一个目录，包括其所有子目录。`Walk` 接受一个回调函数来处理访问的每个文件或目录。

## 示例

```sh
$ go run directories.go
列出 subdir/parent
child true
file2 false
file3 false
列出 subdir/parent/child
file4 false
访问 subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
