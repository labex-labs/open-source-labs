# URL 解析

此挑战要求解析一个示例 URL，该 URL 包含协议、认证信息、主机、端口、路径、查询参数和查询片段。解析后的 URL 应用于提取 URL 的各个组件。

## 要求

- 应导入 `url` 和 `net` 包。
- 应解析示例 URL 并检查错误。
- 应从解析后的 URL 中提取协议、认证信息、主机、端口、路径、查询参数和查询片段。
- 应使用 `SplitHostPort` 函数从 `Host` 字段中提取主机名和端口。
- 应使用 `ParseQuery` 函数将查询参数解析为映射。

## 示例

```sh
# 运行我们的 URL 解析程序会显示我们提取的所有不同部分。
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```
