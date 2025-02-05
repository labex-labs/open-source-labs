# 验证请求并选择性地做出响应

目前，我们的Web服务器无论客户端请求什么，都会返回文件中的HTML。让我们添加功能来检查浏览器在返回HTML文件之前是否请求的是`/_`，如果浏览器请求的是其他内容，则返回一个错误。为此，我们需要修改`handle_connection`，如清单20-6所示。这段新代码会将接收到的请求内容与我们所知道的对`/_`的请求进行对比，并添加`if`和`else`块来区别对待不同的请求。

文件名：`src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
     .lines()
     .next()
     .unwrap()
     .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // 其他请求
    }
}
```

清单20-6：对请求`/_`和其他请求进行不同处理

我们只关注HTTP请求的第一行，所以不是将整个请求读入一个向量，而是调用`next`从迭代器中获取第一个元素\[1\]。第一个`unwrap`处理`Option`，如果迭代器没有元素则停止程序。第二个`unwrap`处理`Result`，其效果与清单20-2中添加的`map`里的`unwrap`相同。

接下来，我们检查`request_line`是否等于对`/_`路径的GET请求的请求行\[2\]。如果是，`if`块返回我们HTML文件的内容。

如果`request_line`不等于对`/_`路径的GET请求，这意味着我们收到了其他请求。我们稍后会在`else`块中添加代码\[3\]来响应所有其他请求。

现在运行这段代码并请求`127.0.0.1:7878`；你应该会得到`hello.html`中的HTML。如果你进行任何其他请求，比如`127.0.0.1:7878/something-else`，你会得到一个连接错误，就像你在运行清单20-1和清单20-2中的代码时看到的那样。

现在让我们将清单20-7中的代码添加到`else`块中，以返回状态码为404的响应，这表示请求的内容未找到。我们还将返回一些HTML，用于在浏览器中渲染一个页面，向最终用户指示响应情况。

文件名：`src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

清单20-7：如果请求的不是`/_`，则返回状态码404和错误页面

在这里，我们的响应状态行包含状态码404和原因短语`NOT FOUND`\[1\]。响应的主体将是`404.html`文件中的HTML\[1\]。你需要在`hello.html`旁边创建一个`404.html`文件作为错误页面；同样，你可以随意使用任何你想要的HTML，或者使用清单20-8中的示例HTML。

文件名：`404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>哎呀！</h1>
    <p>对不起，我不知道你在请求什么。</p>
  </body>
</html>
```

清单20-8：用于在任何404响应中返回的页面的示例内容

有了这些更改后，再次运行你的服务器。请求`127.0.0.1:7878`应该返回`hello.html`的内容，而任何其他请求，比如`127.0.0.1:7878/foo`，应该返回`404.html`中的错误HTML。
