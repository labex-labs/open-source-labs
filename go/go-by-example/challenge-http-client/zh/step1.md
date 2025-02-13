# HTTP 客户端

你需要编写一个程序，向服务器发送 HTTP GET 请求，并打印 HTTP 响应状态以及响应体的前 5 行。

## 要求

- 程序应使用 `net/http` 包发出 HTTP GET 请求。
- 程序应打印 HTTP 响应状态。
- 程序应打印响应体的前 5 行。
- 程序应妥善处理错误。

## 示例

```sh
$ go run http-clients.go
响应状态：200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
