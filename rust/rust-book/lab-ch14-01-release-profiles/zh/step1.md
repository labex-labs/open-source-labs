# 使用发布配置文件自定义构建

在 Rust 中，**发布配置文件** 是预定义且可定制的配置文件，具有不同的配置，使程序员能够更好地控制编译代码的各种选项。每个配置文件都是独立配置的。

Cargo 有两个主要的配置文件：当你运行 `cargo build` 时 Cargo 使用的 `dev` 配置文件，以及当你运行 `cargo build --release` 时 Cargo 使用的 `release` 配置文件。`dev` 配置文件为开发定义了良好的默认值，而 `release` 配置文件为发布构建定义了良好的默认值。

你可能从构建输出中熟悉这些配置文件名：

```bash
$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s
```

`dev` 和 `release` 就是编译器使用的这些不同的配置文件。

当你没有在项目的 `Cargo.toml` 文件中显式添加任何 `[profile.*]` 部分时，Cargo 会为每个配置文件设置默认值。通过为你想要自定义的任何配置文件添加 `[profile.*]` 部分，你可以覆盖默认设置的任何子集。例如，以下是 `dev` 和 `release` 配置文件的 `opt-level` 设置的默认值：

文件名：`Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 0

[profile.release]
opt-level = 3
```

`opt-level` 设置控制 Rust 应用于你的代码的优化数量，范围是 0 到 3。应用更多优化会延长编译时间，所以如果你处于开发阶段且经常编译代码，你会希望进行较少的优化以更快地编译，即使生成的代码运行速度较慢。因此，`dev` 的默认 `opt-level` 是 `0`。当你准备发布代码时，最好花更多时间编译。你只会在发布模式下编译一次，但会多次运行编译后的程序，所以发布模式以更长的编译时间换取运行速度更快的代码。这就是为什么 `release` 配置文件的默认 `opt-level` 是 `3`。

你可以通过在 `Cargo.toml` 中为其添加不同的值来覆盖默认设置。例如，如果我们想在开发配置文件中使用优化级别 1，我们可以在项目的 `Cargo.toml` 文件中添加以下两行：

文件名：`Cargo.toml`

```tomltoml
[profile.dev]
opt-level = 1
```

这段代码覆盖了默认设置 `0`。现在当我们运行 `cargo build` 时，Cargo 将使用 `dev` 配置文件的默认值加上我们对 `opt-level` 的自定义。因为我们将 `opt-level` 设置为 `1`，Cargo 将应用比默认更多的优化，但不如发布构建中的多。

有关每个配置文件的完整配置选项和默认值列表，请参阅 Cargo 的文档：*https://doc.rust-lang.org/cargo/reference/profiles.html*。
