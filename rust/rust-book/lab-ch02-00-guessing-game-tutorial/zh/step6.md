# 使用 Result 处理潜在失败

我们仍在处理这行代码。现在我们要讨论第三行文本，但请注意它仍然是单个逻辑行代码的一部分。接下来的部分是这个方法：

```rust
.expect("Failed to read line");
```

我们本可以将这段代码写成：

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

然而，一长行代码很难阅读，所以最好将其拆分。当你使用 `.method_name()` 语法调用方法时，引入换行符和其他空白字符来帮助拆分长行通常是明智的。现在让我们来讨论这一行代码的作用。

如前所述，`read_line` 会将用户输入的任何内容放入我们传递给它的字符串中，但它也会返回一个 `Result` 值。`Result` 是一种 _枚举类型_，通常称为 _枚举_，它是一种可以处于多种可能状态之一的类型。我们将每个可能的状态称为一个 _变体_。

第 6 章将更详细地介绍枚举。这些 `Result` 类型的目的是对错误处理信息进行编码。

`Result` 的变体是 `Ok` 和 `Err`。`Ok` 变体表示操作成功，`Ok` 内部是成功生成的值。`Err` 变体表示操作失败，`Err` 包含有关操作如何或为何失败的信息。

`Result` 类型的值，就像任何类型的值一样，都定义了一些方法。`Result` 的一个实例有一个 `expect` 方法，你可以调用它。如果这个 `Result` 实例是一个 `Err` 值，`expect` 会导致程序崩溃并显示你作为参数传递给 `expect` 的消息。如果 `read_line` 方法返回一个 `Err`，这很可能是底层操作系统出现错误的结果。如果这个 `Result` 实例是一个 `Ok` 值，`expect` 会获取 `Ok` 所包含的返回值并将其返回给你，以便你使用。在这种情况下，那个值是用户输入中的字节数。

如果你不调用 `expect`，程序将编译通过，但你会收到一个警告：

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust 会警告你没有使用 `read_line` 返回的 `Result` 值，这表明程序没有处理可能出现的错误。

抑制警告的正确方法是实际编写错误处理代码，但在我们的例子中，我们只是希望在出现问题时使程序崩溃，所以我们可以使用 `expect`。你将在第 9 章学习如何从错误中恢复。
