# `open` 函数

`open` 函数可用于以只读模式打开文件。

一个 `File` 对象拥有一个资源，即文件描述符，并在其被 `drop` 时负责关闭文件。

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // 创建指向所需文件的路径
    let path = Path::new("hello.txt");
    let display = path.display();

    // 以只读模式打开路径，返回 `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("无法打开 {}: {}", display, why),
        Ok(file) => file,
    };

    // 将文件内容读入字符串，返回 `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("无法读取 {}: {}", display, why),
        Ok(_) => print!("{} 包含:\n{}", display, s),
    }

    // `file` 超出作用域，"hello.txt" 文件被关闭
}
```

以下是预期的成功输出：

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt 包含:
Hello World!
```

（鼓励你在不同的失败条件下测试前面的示例：`hello.txt` 不存在，或 `hello.txt` 不可读等。）
