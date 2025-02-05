# `create`

`create` 函数以只写模式打开一个文件。如果文件已经存在，旧内容将被删除。否则，将创建一个新文件。

```rust
static LOREM_IPSUM: &str =
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
";

use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("lorem_ipsum.txt");
    let display = path.display();

    // 以只写模式打开一个文件，返回 `io::Result<File>`
    let mut file = match File::create(&path) {
        Err(why) => panic!("无法创建 {}: {}", display, why),
        Ok(file) => file,
    };

    // 将 `LOREM_IPSUM` 字符串写入 `file`，返回 `io::Result<()>`
    match file.write_all(LOREM_IPSUM.as_bytes()) {
        Err(why) => panic!("无法写入 {}: {}", display, why),
        Ok(_) => println!("成功写入 {}", display),
    }
}
```

以下是预期的成功输出：

```shell
$ rustc create.rs && ./create
成功写入 lorem_ipsum.txt
$ cat lorem_ipsum.txt
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

（与上一个示例一样，鼓励你在失败条件下测试此示例。）

\[`OpenOptions`\] 结构体可用于配置文件的打开方式。
