# 读取请求

让我们实现从浏览器读取请求的功能！为了将首先获取连接的关注点与随后对该连接采取某些操作的关注点分开，我们将启动一个新函数来处理连接。在这个新的`handle_connection`函数中，我们将从TCP流中读取数据并打印出来，这样我们就能看到从浏览器发送的数据。将代码修改为如清单20-2所示。

文件名：`src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5.lines()
      6.map(|result| result.unwrap())
      7.take_while(|line|!line.is_empty())
       .collect();

  8 println!("Request: {:#?}", http_request);
}
```

清单20-2：从`TcpStream`读取并打印数据

我们引入`std::io::prelude`和`std::io::BufReader`到作用域中，以获取让我们能够对流进行读写的 trait 和类型\[1\]。在`main`函数的`for`循环中，我们现在不再打印表示建立了连接的消息，而是调用新的`handle_connection`函数并将`stream`传递给它\[2\]。

在`handle_connection`函数中，我们创建一个新的`BufReader`实例，它包装了对`stream`的可变引用\[3\]。`BufReader`通过为我们管理对`std::io::Read` trait 方法的调用来添加缓冲。

我们创建一个名为`http_request`的变量来收集浏览器发送到我们服务器的请求行。通过添加`Vec<_>`类型注释，我们表明希望将这些行收集到一个向量中\[4\]。

`BufReader`实现了`std::io::BufRead` trait，该 trait 提供了`lines`方法\[5\]。`lines`方法通过在每次看到换行符时分割数据流来返回一个`Result<String, std::io::Error>`的迭代器。为了获取每个`String`，我们对每个`Result`进行映射并调用`unwrap`\[6\]。如果数据不是有效的UTF-8编码或者从流中读取时有问题，`Result`可能是一个错误。同样，一个生产程序应该更优雅地处理这些错误，但为了简单起见，我们选择在出错时停止程序。

浏览器通过连续发送两个换行符来表示HTTP请求的结束，所以为了从流中获取一个请求，我们读取行直到得到一个空字符串的行\[7\]。一旦我们将行收集到向量中，我们就使用漂亮的调试格式将它们打印出来\[8\]，这样我们就可以查看Web浏览器发送到我们服务器的指令。

让我们试试这段代码！启动程序并再次在Web浏览器中发出请求。请注意，我们在浏览器中仍然会得到一个错误页面，但我们程序在终端中的输出现在将类似于这样：

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User:?1",
    "Cache-Control: max-age=0",
]
```

根据你的浏览器，你可能会得到略有不同的输出。现在我们打印了请求数据，通过查看请求第一行中`GET`之后的路径，我们可以明白为什么从一个浏览器请求会得到多个连接。如果重复的连接都在请求`/_`，我们就知道浏览器因为没有从我们的程序得到响应而在反复尝试获取`/_`。

让我们剖析一下这个请求数据，以了解浏览器对我们的程序有什么要求。
