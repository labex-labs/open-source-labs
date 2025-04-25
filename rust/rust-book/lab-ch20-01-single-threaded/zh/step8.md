# 一点重构

目前，`if`和`else`块中有很多重复代码：它们都在读取文件并将文件内容写入流中。唯一的区别是状态行和文件名。让我们通过将这些差异提取到单独的`if`和`else`行中，将状态行和文件名的值赋给变量，从而使代码更简洁；然后我们可以在代码中无条件地使用这些变量来读取文件并写入响应。清单 20-9 展示了替换大的`if`和`else`块后的最终代码。

文件名：`src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

清单 20-9：重构`if`和`else`块，使其仅包含两种情况之间不同的代码

现在，`if`和`else`块只返回元组中状态行和文件名的适当值；然后我们使用解构，通过`let`语句中的模式将这两个值赋给`status_line`和`filename`，如第 18 章所述。

之前重复的代码现在在`if`和`else`块之外，并使用`status_line`和`filename`变量。这使得更容易看出两种情况之间的区别，并且这意味着如果我们想更改文件读取和响应写入的工作方式，我们只需要在一个地方更新代码。清单 20-9 中的代码行为与清单 20-8 中的相同。

太棒了！我们现在用大约 40 行 Rust 代码就有了一个简单的 Web 服务器，它对一个请求用一页内容进行响应，对所有其他请求用 404 响应进行响应。

目前，我们的服务器在单个线程中运行，这意味着它一次只能处理一个请求。让我们通过模拟一些慢速请求来研究这可能会带来什么问题。然后我们将修复它，以便我们的服务器能够一次处理多个请求。
