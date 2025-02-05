# 使用 `panic!` 处理不可恢复的错误

有时候，你的代码会出现一些无法处理的糟糕情况。在这些情况下，Rust 提供了 `panic!` 宏。在实际应用中，有两种方式会导致程序出现 `panic!`：一种是执行了某些操作致使代码触发 `panic!`（例如访问超出数组边界的元素），另一种是显式调用 `panic!` 宏。在这两种情况下，程序都会发生 `panic!`。默认情况下，这些 `panic!` 会打印一条失败信息，展开调用栈，清理栈上的数据，然后退出程序。通过设置一个环境变量，你还可以让 Rust 在发生 `panic!` 时显示调用栈，以便更轻松地追踪 `panic!` 的源头。

> **展开调用栈还是立即终止程序以响应 `panic!`**
>
> 默认情况下，当发生 `panic!` 时，程序会开始 _展开调用栈_，这意味着 Rust 会沿着调用栈回溯，并清理它遇到的每个函数中的数据。然而，回溯和清理工作非常耗时。因此，Rust 允许你选择立即 _终止程序_ 的方式，即不进行清理工作就直接结束程序。
>
> 程序使用的内存随后需要由操作系统进行清理。如果在你的项目中，你需要使生成的二进制文件尽可能小，那么你可以通过在 `Cargo.toml` 文件的适当 `[profile]` 部分添加 `panic = 'abort'`，将 `panic!` 时的行为从展开调用栈切换为立即终止程序。例如，如果你想在发布模式下发生 `panic!` 时立即终止程序，可以添加以下内容：
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

让我们在一个简单的程序中尝试调用 `panic!`：

文件名：`src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

当你运行这个程序时，你会看到类似这样的输出：

    thread'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

对 `panic!` 的调用导致了最后两行中的错误信息。第一行显示了我们的 `panic!` 信息以及 `panic!` 在源代码中发生的位置：`src/main.rs:2:5` 表示这是我们 `src/main.rs` 文件的第二行、第五个字符处。

在这种情况下，指示的行是我们代码的一部分，如果我们查看该行，会看到 `panic!` 宏调用。在其他情况下，`panic!` 调用可能在我们的代码所调用的代码中，错误信息报告的文件名和行号将是调用 `panic!` 宏的其他人的代码位置，而不是最终导致 `panic!` 调用的我们的代码行。

我们可以使用 `panic!` 调用所来自的函数的回溯信息来找出导致问题的代码部分。为了理解如何使用 `panic!` 回溯信息，让我们看另一个示例，看看当 `panic!` 调用由于我们代码中的错误而来自库时（而不是直接由我们的代码调用宏）是什么样的。清单 9-1 中的代码尝试访问向量中超出有效索引范围的索引。

文件名：`src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

清单 9-1：尝试访问超出向量末尾的元素，这将导致调用 `panic!`

在这里，我们试图访问向量的第 100 个元素（因为索引从 0 开始，所以是索引 99 处），但向量只有三个元素。在这种情况下，Rust 将发生 `panic!`。使用 `[]` 本应返回一个元素，但如果你传递一个无效索引，Rust 在这里无法返回任何正确的元素。

在 C 语言中，尝试读取超出数据结构末尾的数据是未定义行为。你可能会得到内存中与数据结构中该元素相对应位置上的任何值，即使该内存不属于该结构。这被称为 _缓冲区越界读取_，如果攻击者能够以某种方式操纵索引来读取他们不应该访问的数据结构之后存储的数据，可能会导致安全漏洞。

为了保护你的程序免受此类漏洞的影响，如果你尝试读取不存在的索引处的元素，Rust 将停止执行并拒绝继续。让我们试试看：

    thread'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

这个错误指向我们 `main.rs` 的第 4 行，在那里我们尝试访问 `index`。

`note:` 行告诉我们可以设置 `RUST_BACKTRACE` 环境变量来获取导致错误的确切发生过程的回溯信息。_回溯信息_ 是一个已调用的所有函数的列表。Rust 中的回溯信息与其他语言中的工作方式相同：读取回溯信息的关键是从顶部开始读取，直到看到你编写的文件。那就是问题起源的地方。该位置上方的行是你的代码调用的代码；下方的行是调用你的代码的代码。这些前后的行可能包括核心 Rust 代码、标准库代码或你正在使用的 crate。让我们通过将 `RUST_BACKTRACE` 环境变量设置为除 `0` 以外的任何值来尝试获取回溯信息。清单 9-2 显示了类似你将看到的输出。

```bash
$ RUST_BACKTRACE=1 cargo run
thread'main' panicked at 'index out of bounds: the len is 3 but the index is
99', src/main.rs:4:5
stack backtrace:
0: rust_begin_unwind
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/std
/src/panicking.rs:584:5
1: core::panicking::panic_fmt
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:142:14
2: core::panicking::panic_bounds_check
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:84:5
3: < usize as core::slice::index::SliceIndex < [T] >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:242:10
4: core::slice::index:: core::ops::index::Index [T] < impl < I > for > ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:18:9
5: < alloc::vec::Vec < T,A > as core::ops::index::Index < I >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/alloc
/src/vec/mod.rs:2591:9
6: panic::main
at./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

清单 9-2：当设置环境变量 `RUST_BACKTRACE` 时显示的由 `panic!` 调用生成的回溯信息

这是很多输出！你看到的确切输出可能因操作系统和 Rust 版本而异。为了获得包含此信息的回溯信息，必须启用调试符号。如我们这里所做的，在使用 `cargo build` 或 `cargo run` 且不使用 `--release` 标志时，调试符号默认是启用的。

在清单 9-2 的输出中，回溯信息的第 6 行指向我们项目中导致问题的行：`src/main.rs` 的第 4 行。如果我们不希望程序发生 `panic!`，我们应该从提到我们编写的文件的第一行所指向的位置开始调查。在清单 9-1 中，我们故意编写了会导致 `panic!` 的代码，解决 `panic!` 的方法是不请求超出向量索引范围的元素。当你的代码将来发生 `panic!` 时，你需要弄清楚代码使用了哪些值进行了什么操作从而导致了 `panic!`，以及代码应该做什么来替代。

我们将在“是否使用 `panic!`”中回到 `panic!` 以及何时应该和不应该使用 `panic!` 来处理错误情况。接下来，我们将看看如何使用 `Result` 从错误中恢复。
