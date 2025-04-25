# HTTP 服务器

你需要编写一个简单的 HTTP 服务器，它能够处理两条路由：`/hello` 和 `/headers`。`/hello` 路由应返回一个简单的“hello”响应，而 `/headers` 路由应返回所有 HTTP 请求头。

## 要求

- 服务器应使用 `net/http` 包。
- `/hello` 路由应返回“hello”响应。
- `/headers` 路由应返回所有 HTTP 请求头。
- 服务器应监听端口 `8090`。

## 示例

```sh
# 在后台运行服务器。
$ go run http-servers.go &

# 访问 `/hello` 路由。
$ curl localhost:8090/hello
hello
```
