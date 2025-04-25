# 返回真实的 HTML

让我们实现返回不仅仅是一个空白页面的功能。在项目目录的根目录下创建新文件*hello.html*，而不是在`src`目录中。你可以输入任何你想要的 HTML；清单 20-4 展示了一种可能性。

文件名：`hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>Hi from Rust</p>
  </body>
</html>
```

清单 20-4：一个用于在响应中返回的示例 HTML 文件

这是一个包含标题和一些文本的最小 HTML5 文档。为了在接收到请求时从服务器返回这个文件，我们将按照清单 20-5 修改`handle_connection`，以读取 HTML 文件，将其作为主体添加到响应中并发送。

文件名：`src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
       .lines()
       .map(|result| result.unwrap())
       .take_while(|line|!line.is_empty())
       .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

清单 20-5：将*hello.html*的内容作为响应主体发送

我们在`use`语句中添加了`fs`，以将标准库的文件系统模块引入作用域\[1\]。将文件内容读取为字符串的代码应该看起来很熟悉；我们在清单 12-4 中为 I/O 项目读取文件内容时使用过它。

接下来，我们使用`format!`将文件内容作为成功响应的主体添加进去\[2\]。为了确保有效的 HTTP 响应，我们添加了`Content-Length`头部，其值设置为响应主体的大小，在这种情况下是`hello.html`的大小。

使用`cargo run`运行此代码，并在浏览器中加载`127.0.0.1:7878`；你应该会看到渲染后的 HTML！

目前，我们忽略了`http_request`中的请求数据，只是无条件地返回 HTML 文件的内容。这意味着如果你在浏览器中尝试请求`127.0.0.1:7878/something-else`，你仍然会得到相同的 HTML 响应。目前，我们的服务器非常有限，并不具备大多数 Web 服务器的功能。我们希望根据请求定制响应，并且只在对`/_`的格式良好的请求时才返回 HTML 文件。
