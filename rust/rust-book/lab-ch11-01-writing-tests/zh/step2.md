# 测试函数剖析

在 Rust 中，最简单的测试就是一个使用 `test` 属性进行注解的函数。属性是关于 Rust 代码片段的元数据；比如我们在第五章用于结构体的 `derive` 属性。要将一个函数变成测试函数，在 `fn` 之前的那一行添加 `#[test]`。当你使用 `cargo test` 命令运行测试时，Rust 会构建一个测试运行器二进制文件，它会运行这些带注解的函数，并报告每个测试函数是通过还是失败。

每当我们使用 Cargo 创建一个新的库项目时，会自动为我们生成一个包含测试函数的测试模块。这个模块为你提供了一个编写测试的模板，这样你每次开始一个新项目时就不必去查找确切的结构和语法了。你可以根据需要添加任意数量的额外测试函数和测试模块！

在实际测试任何代码之前，我们先通过对模板测试进行实验来探索测试的一些工作原理。然后我们将编写一些实际的测试，调用我们编写的一些代码，并断言其行为是正确的。

让我们创建一个名为 `adder` 的新库项目，用于将两个数字相加：

```bash
$ cargo new adder --lib
Created library $(adder) project
$ cd adder
```

你的 `adder` 库中 `src/lib.rs` 文件的内容应该如下所示（清单 11 - 1）。

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

清单 11 - 1：由 `cargo new` 自动生成的测试模块和函数

目前，让我们先忽略前两行，专注于这个函数。注意 `#[test]` 注解 \[1\]：这个属性表明这是一个测试函数，这样测试运行器就知道将这个函数视为测试。在 `tests` 模块中我们可能也有非测试函数，用于帮助设置常见场景或执行常见操作，所以我们总是需要指明哪些函数是测试。

示例函数体使用 `assert_eq!` 宏 \[2\] 来断言 `result`（它包含 2 加 2 的结果）等于 4。这个断言是典型测试格式的一个示例。让我们运行它看看这个测试是否通过。

`cargo test` 命令会运行我们项目中的所有测试，如清单 11 - 2 所示。

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.57s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

1 running 1 test
2 test tests::it_works... ok

3 test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s

  4 Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

清单 11 - 2：运行自动生成的测试的输出

Cargo 编译并运行了测试。我们看到 `running 1 test` 这一行 \[1\]。下一行显示了生成的测试函数的名称，即 `it_works`，并且运行该测试的结果是 `ok` \[2\]。整体总结 `test result: ok.` \[3\] 表示所有测试都通过了，而 `1 passed; 0 failed` 这部分汇总了通过或失败的测试数量。

可以将一个测试标记为被忽略，这样它在特定实例中就不会运行；我们将在“除非特别请求，否则忽略某些测试”中介绍这一点。因为我们这里没有这样做，所以总结中显示 `0 ignored`。我们也可以向 `cargo test` 命令传递一个参数，只运行名称与某个字符串匹配的测试；这称为 _过滤_，我们将在“按名称运行测试子集”中介绍。这里我们没有过滤正在运行的测试，所以总结的最后显示 `0 filtered out`。

`0 measured` 统计信息是关于测量性能的基准测试的。截至本文撰写时，基准测试仅在 Rust 的夜间版本中可用。有关基准测试的更多信息，请参阅 *https://doc.rust-lang.org/unstable-book/library-features/test.html* 上的文档。

测试输出从 `Doc-tests adder` 开始的下一部分 \[4\] 是关于任何文档测试的结果。我们目前还没有任何文档测试，但是 Rust 可以编译我们 API 文档中出现的任何代码示例。这个功能有助于使你的文档和代码保持同步！我们将在“作为测试的文档注释”中讨论如何编写文档测试。目前，我们将忽略 `Doc-tests` 输出。

让我们开始根据自己的需要定制测试。首先，将 `it_works` 函数的名称更改为其他名称，比如 `exploration`，如下所示：

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

然后再次运行 `cargo test`。现在输出显示的是 `exploration` 而不是 `it_works`：

    running 1 test
    test tests::exploration... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

现在我们再添加一个测试，但这次我们要让这个测试失败！当测试函数中的某些内容导致程序恐慌时，测试就会失败。每个测试都在一个新线程中运行，当主线程看到一个测试线程终止时，该测试就会被标记为失败。在第九章中，我们讨论过导致程序恐慌的最简单方法是调用 `panic!` 宏。输入一个名为 `another` 的新测试函数，这样你的 `src/lib.rs` 文件就如下所示（清单 11 - 3）。

文件名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
```

清单 11 - 3：添加第二个会因为调用 `panic!` 宏而失败的测试

再次使用 `cargo test` 运行测试。输出应该如下所示（清单 11 - 4），它显示我们的 `exploration` 测试通过了，而 `another` 测试失败了。

    running 2 tests
    test tests::exploration... ok
    1 test tests::another... FAILED

    2 failures:

    ---- tests::another stdout ----
    thread'main' panicked at 'Make this test fail', src/lib.rs:10:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    3 failures:
        tests::another

    4 test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

    error: test failed, to rerun pass '--lib'

清单 11 - 4：一个测试通过而一个测试失败时的测试结果

`test tests::another` 这一行显示的不是 `ok`，而是 `FAILED` \[1\]。在单个测试结果和总结之间出现了两个新部分：第一个 \[2\] 显示了每个测试失败的详细原因。在这种情况下，我们得到的详细信息是 `another` 失败了，因为它在 `src/lib.rs` 文件的第 10 行 `panicked at 'Make this test fail'`。下一个部分 \[3\] 只列出了所有失败测试的名称，当有很多测试和大量详细的失败测试输出时，这很有用。我们可以使用失败测试的名称来只运行那个测试，以便更轻松地调试它；我们将在“控制测试的运行方式”中更多地讨论运行测试的方法。

总结行在最后显示 \[4\]：总体而言，我们的测试结果是 `FAILED`。我们有一个测试通过，一个测试失败。

既然你已经看到了不同场景下的测试结果是什么样的，让我们来看看除了 `panic!` 之外，在测试中还有用的其他一些宏。
