# 测试

如我们所知，测试对于任何软件来说都是不可或缺的！Rust 对单元测试和集成测试提供了一流的支持（请参阅《Rust 程序设计语言》（TRPL）中的[这一章](https://doc.rust-lang.org/book/ch11-00-testing.html)）。

从上面链接的测试章节中，我们了解了如何编写单元测试和集成测试。在组织方面，我们可以将单元测试放在它们所测试的模块中，而将集成测试放在它们自己的 `tests/` 目录中：

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

`tests` 目录中的每个文件都是一个单独的[集成测试](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)，即一个旨在测试你的库的测试，就好像它是从一个依赖的 crate 中被调用一样。

测试章节详细阐述了三种不同的测试风格：单元测试、文档测试和集成测试。

`cargo` 自然提供了一种简单的方法来运行你所有的测试！

```shell
$ cargo test
```

你应该会看到如下输出：

```shell
[object Object]
```

你也可以运行名称匹配某个模式的测试：

```shell
$ cargo test test_foo
```

```shell
[object Object]
```

需要注意的一点是：Cargo 可能会并发运行多个测试，所以要确保它们不会相互竞争。

这种并发导致问题的一个例子是，如果两个测试都输出到一个文件，如下所示：

```rust
#[cfg(test)]
mod tests {
    // 导入必要的模块
    use std::fs::OpenOptions;
    use std::io::Write;

    // 这个测试写入一个文件
    #[test]
    fn test_file() {
        // 打开文件 ferris.txt，如果不存在则创建一个。
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // 打印 "Ferris" 5 次。
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }

    // 这个测试尝试写入同一个文件
    #[test]
    fn test_file_also() {
        // 打开文件 ferris.txt，如果不存在则创建一个。
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // 打印 "Corro" 5 次。
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }
}
```

尽管预期的结果是这样：

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

但实际写入 `ferris.txt` 的内容却是这样：

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
