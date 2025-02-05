# 在工作区中依赖外部包

注意，工作区在顶层只有一个 _Cargo.lock_ 文件，而不是在每个板条箱的目录中都有一个 _Cargo.lock_。这确保了所有板条箱都使用所有依赖项的相同版本。如果我们将 `rand` 包添加到 _adder/Cargo.toml_ 和 _add_one/Cargo.toml_ 文件中，Cargo 会将这两个文件中的依赖项解析为 `rand` 的同一个版本，并将其记录在一个 _Cargo.lock_ 中。使工作区中的所有板条箱使用相同的依赖项意味着这些板条箱将始终相互兼容。让我们将 `rand` 板条箱添加到 _add_one/Cargo.toml_ 文件的 `[dependencies]` 部分，这样我们就可以在 `add_one` 板条箱中使用 `rand` 板条箱：

文件名：`add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

现在我们可以在 `add_one/src/lib.rs` 文件中添加 `use rand;`，并且通过在 `add` 目录中运行 `cargo build` 来构建整个工作区，这将引入并编译 `rand` 板条箱。我们会得到一个警告，因为我们没有引用引入作用域的 `rand`：

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

顶层的 _Cargo.lock_ 现在包含了 `add_one` 对 `rand` 的依赖信息。然而，即使 `rand` 在工作区的某个地方被使用了，除非我们也将 `rand` 添加到工作区中其他板条箱的 `Cargo.toml` 文件中，否则我们不能在这些板条箱中使用它。例如，如果我们在 `adder` 包的 `adder/src/main.rs` 文件中添加 `use rand;`，我们会得到一个错误：

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

要解决这个问题，编辑 `adder` 包的 `Cargo.toml` 文件，并表明 `rand` 也是它的一个依赖项。构建 `adder` 包会将 `rand` 添加到 _Cargo.lock_ 中 `adder` 的依赖项列表中，但不会下载额外的 `rand` 副本。Cargo 确保了工作区中每个使用 `rand` 包的包中的每个板条箱都将使用相同的版本，这为我们节省了空间，并确保了工作区中的板条箱相互兼容。
