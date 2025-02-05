# `read_lines`

## 简单方法

对于初学者首次实现从文件读取行来说，这可能是一种合理的初次尝试。

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

由于 `lines()` 方法返回文件中行的迭代器，我们也可以内联执行映射并收集结果，从而得到更简洁流畅的表达式。

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // 对可能的文件读取错误进行 panic
     .lines()  // 将字符串拆分为字符串切片的迭代器
     .map(String::from)  // 将每个切片转换为字符串
     .collect()  // 将它们收集到一个向量中
}
```

请注意，在上述两个示例中，我们必须分别使用 `.to_string()` 和 `String::from` 将 `lines()` 返回的 `&str` 引用转换为拥有的类型 `String`。

## 更高效的方法

在这里，我们将打开的 `File` 的所有权传递给 `BufReader` 结构体。`BufReader` 使用内部缓冲区来减少中间分配。

我们还更新了 `read_lines`，使其返回一个迭代器，而不是为每行在内存中分配新的 `String` 对象。

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // hosts.txt 文件必须存在于当前路径中
    if let Ok(lines) = read_lines("./hosts.txt") {
        // 消耗迭代器，返回一个（可选的）字符串
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// 输出包装在 Result 中以允许对错误进行匹配
// 返回文件行读取器的迭代器。
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

运行此程序只会逐行打印内容。

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

（请注意，由于 `File::open` 期望一个通用的 `AsRef<Path>` 作为参数，我们使用 `where` 关键字为我们的通用 `read_lines()` 方法定义相同的通用约束。）

此过程比在内存中使用文件的所有内容创建一个 `String` 更高效。在处理较大文件时，这尤其可能导致性能问题。
