# 作为测试的文档注释

在文档注释中添加示例代码块有助于演示如何使用你的库，这样做还有一个额外的好处：运行 `cargo test` 时会将文档中的代码示例作为测试运行！没有什么比带有示例的文档更好的了。但也没有什么比因为自编写文档以来代码发生了变化而导致示例无法正常工作更糟糕的了。如果我们使用清单14-1中 `add_one` 函数的文档来运行 `cargo test`，我们会在测试结果中看到一个类似这样的部分：

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5)... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

现在，如果我们更改函数或示例，使示例中的 `assert_eq!` 导致恐慌，然后再次运行 `cargo test`，我们会看到文档测试会捕捉到示例和代码彼此不同步的情况！
