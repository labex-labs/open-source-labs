# 使用包来获取更多功能

请记住，包是 Rust 源代码文件的集合。我们一直在构建的项目是一个 _二进制包_，它是一个可执行文件。`rand` 包是一个 _库包_，它包含的代码旨在供其他程序使用，不能单独执行。

Cargo 对外部包的协调是它真正发挥作用的地方。在我们编写使用 `rand` 的代码之前，需要修改 `Cargo.toml` 文件，将 `rand` 包作为依赖项包含进来。现在打开该文件，在 Cargo 为你创建的 `[dependencies]` 部分标题下方的底部添加以下行。请确保按照我们这里的写法准确指定 `rand` 及其版本号，否则本教程中的代码示例可能无法正常工作：

文件名：`Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

在 `Cargo.toml` 文件中，跟在标题后面的所有内容都是该部分的一部分，一直延续到另一个部分开始。在 `[dependencies]` 中，你要告诉 Cargo 你的项目依赖哪些外部包以及你需要这些包的哪些版本。在这种情况下，我们使用语义化版本规范 `0.8.5` 指定了 `rand` 包。Cargo 理解语义化版本控制（有时称为 _SemVer_），这是一种编写版本号的标准。规范 `0.8.5` 实际上是 `^0.8.5` 的简写，意思是任何至少为 0.8.5 但低于 0.9.0 的版本。

Cargo 认为这些版本具有与 0.8.5 版本兼容的公共 API，并且这个规范确保你将获得最新的补丁版本，该版本仍然可以与本章中的代码编译。任何 0.9.0 或更高版本不能保证具有与以下示例中使用的相同 API。

现在，在不更改任何代码的情况下，让我们像清单 2-2 中那样构建项目。

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  Downloaded libc v0.2.127
  Downloaded getrandom v0.2.7
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.16
  Downloaded rand_chacha v0.3.1
  Downloaded rand_core v0.6.3
   Compiling rand_core v0.6.3
   Compiling libc v0.2.127
   Compiling getrandom v0.2.7
   Compiling cfg-if v1.0.0
   Compiling ppv-lite86 v0.2.16
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
```

清单 2-2：添加 `rand` 包作为依赖项后运行 `cargo build` 的输出

你可能会看到不同的版本号（但由于 SemVer，它们都将与代码兼容！）和不同的行（取决于操作系统），并且这些行的顺序可能也不同。

当我们包含一个外部依赖项时，Cargo 会从 _注册表_ 中获取该依赖项所需的所有内容的最新版本，注册表是来自 *https://crates.io* 的 Crates.io 数据的副本。Crates.io 是 Rust 生态系统中的人们发布他们的开源 Rust 项目以供其他人使用的地方。

更新注册表后，Cargo 会检查 `[dependencies]` 部分并下载任何尚未下载的列出的包。在这种情况下，虽然我们只将 `rand` 列为依赖项，但 Cargo 也会获取 `rand` 运行所需的其他依赖包。下载完这些包后，Rust 会对它们进行编译，然后使用可用的依赖项编译项目。

如果你在不做任何更改的情况下立即再次运行 `cargo build`，除了 `Finished` 行之外你不会得到任何输出。Cargo 知道它已经下载并编译了依赖项，并且你在 `Cargo.toml` 文件中没有对它们进行任何更改。Cargo 也知道你没有对你的代码进行任何更改，所以它也不会重新编译代码。由于无事可做，它就直接退出了。

如果你打开 `src/main.rs` 文件，进行一个小的更改，然后保存并再次构建，你只会看到两行输出：

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53 secs
```

这些行表明 Cargo 仅根据你对 `src/main.rs` 文件所做的微小更改来更新构建。你的依赖项没有更改，所以 Cargo 知道它可以重用已经为这些依赖项下载和编译的内容。
