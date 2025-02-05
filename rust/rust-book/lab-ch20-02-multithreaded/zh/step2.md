# 模拟一个耗时请求

我们将看看一个处理缓慢的请求如何影响对当前服务器实现发出的其他请求。清单20-10实现了对`/sleep`的请求处理，它带有一个模拟的缓慢响应，这会导致服务器在响应之前休眠五秒钟。

文件名：`src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

清单20-10：通过休眠五秒钟来模拟一个耗时请求

既然我们有三种情况，我们就从`if`切换到了`match`\[1\]。我们需要显式地匹配`request_line`的切片，以便与字符串字面量值进行模式匹配；`match`不像相等方法那样进行自动引用和解引用。

第一个分支\[2\]与清单20-9中的`if`块相同。第二个分支\[3\]匹配对`/sleep`的请求。当接收到该请求时，服务器将休眠五秒钟，然后再渲染成功的HTML页面。第三个分支\[4\]与清单20-9中的`else`块相同。

你可以看到我们的服务器是多么原始：真正的库会以一种简洁得多的方式处理多个请求的识别！

使用`cargo run`启动服务器。然后打开两个浏览器窗口：一个用于访问*http://127.0.0.1:7878*，另一个用于访问*http://127.0.0.1:7878/sleep*。如果你像之前一样多次输入`/_` URI，你会看到它响应得很快。但是如果你输入`/sleep`，然后再加载`/_`，你会看到`/_`会一直等到`sleep`休眠满五秒钟后才加载。

我们可以使用多种技术来避免请求在一个耗时请求之后排队等待；我们将实现的是一个线程池。
