# 嵌入指令

你的任务是修改给定代码，将文件和文件夹嵌入到 Go 二进制文件中，并打印它们的内容。

## 要求

- 你必须使用 `embed` 包来嵌入文件和文件夹。
- 你必须使用 `string` 和 `[]byte` 类型来存储嵌入文件的内容。
- 你必须使用 `embed.FS` 类型来通过通配符嵌入多个文件或文件夹。
- 你必须打印嵌入文件的内容。

## 示例

```sh
# 使用这些命令运行示例。
# （注意：由于 Go 在线运行环境的限制，
# 此示例只能在你的本地机器上运行。）
$ mkdir -p folder
$ echo "hello go" > folder/single_file.txt
$ echo "123" > folder/file1.hash
$ echo "456" > folder/file2.hash

$ go run embed-directive.go
hello go
hello go
123
456
```
