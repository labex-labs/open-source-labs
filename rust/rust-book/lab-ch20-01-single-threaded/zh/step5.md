# 编写响应

我们将实现发送数据以响应客户端请求。响应具有以下格式：

    HTTP版本 状态码 原因短语 CRLF
    头部信息 CRLF
    消息体

第一行是**状态行**，包含响应中使用的HTTP版本、总结请求结果的数字状态码以及提供状态码文本描述的原因短语。在CRLF序列之后是任何头部信息、另一个CRLF序列以及响应的主体。

这是一个使用HTTP版本1.1、状态码为200、原因短语为OK、没有头部信息且没有主体的响应示例：

```rust
HTTP/1.1 200 OK\r\n\r\n
```

状态码200是标准的成功响应。这段文本是一个简短的成功HTTP响应。让我们将其写入流中作为对成功请求的响应！在`handle_connection`函数中，删除打印请求数据的`println!`，并用清单20-3中的代码替换它。

文件名：`src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
     .lines()
     .map(|result| result.unwrap())
     .take_while(|line|!line.is_empty())
     .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

清单20-3：向流中写入一个简短的成功HTTP响应

新的第一行定义了保存成功消息数据的`response`变量\[1\]。然后我们对`response`调用`as_bytes`将字符串数据转换为字节\[3\]。`stream`上的`write_all`方法接受一个`&[u8]`并将这些字节直接通过连接发送出去\[2\]。因为`write_all`操作可能失败，所以我们像之前一样对任何错误结果使用`unwrap`。同样，在实际应用中你应该在这里添加错误处理。

有了这些更改后，让我们运行代码并发出请求。我们不再向终端打印任何数据，所以除了Cargo的输出外我们不会看到任何其他输出。当你在Web浏览器中加载`127.0.0.1:7878`时，你应该会得到一个空白页面而不是错误页面。你刚刚手动编写了接收HTTP请求并发送响应的代码！
