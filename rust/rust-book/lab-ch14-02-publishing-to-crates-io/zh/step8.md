# 为新 crate 添加元数据

假设你有一个想要发布的 crate。在发布之前，你需要在 crate 的 `Cargo.toml` 文件的 `[package]` 部分添加一些元数据。

你的 crate 需要一个唯一的名称。当你在本地处理一个 crate 时，你可以给它取任何你想要的名字。然而，*https://crates.io* 上的 crate 名称是先到先得的。一旦一个 crate 名称被占用，其他人就不能再发布使用该名称的 crate 了。在尝试发布 crate 之前，搜索你想要使用的名称。如果该名称已被使用，你将需要找到另一个名称，并编辑 `Cargo.toml` 文件中 `[package]` 部分下的 `name` 字段，以使用新名称进行发布，如下所示：

文件名：`Cargo.toml`

```tomlrust
[package]
name = "guessing_game"
```

即使你选择了一个唯一的名称，当你此时运行 `cargo publish` 来发布 crate 时，你会收到一个警告，然后是一个错误：

```bash
$ cargo publish
    Updating crates.io index
warning: manifest has no description, license, license-file, documentation,
homepage or repository.
See https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata
for more info.
--snip--
error: failed to publish to registry at https://crates.io

Caused by:
  the remote server responded with an error: missing or empty metadata fields:
description, license. Please see https://doc.rust-
lang.org/cargo/reference/manifest.html for how to upload metadata
```

这会导致错误，因为你缺少一些关键信息：需要一个描述和许可证，这样人们才能知道你的 crate 是做什么的以及他们可以在什么条款下使用它。在 `Cargo.toml` 中，添加一个一两句话的描述，因为它会和你的 crate 一起出现在搜索结果中。对于 `license` 字段，你需要给出一个 **许可证标识符值**。位于 *http://spdx.org/licenses* 的 Linux 基金会的软件包数据交换 (SPDX) 列出了你可以用于此值的标识符。例如，要指定你已根据 MIT 许可证对你的 crate 进行了许可，添加 `MIT` 标识符：

文件名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
license = "MIT"
```

如果你想使用 SPDX 中未出现的许可证，你需要将该许可证的文本放在一个文件中，将该文件包含在你的项目中，然后使用 `license-file` 来指定该文件的名称，而不是使用 `license` 键。

关于哪种许可证适合你的项目的指导超出了本书的范围。Rust 社区中的许多人通过使用 `MIT OR Apache-2.0` 的双重许可证，以与 Rust 相同的方式为他们的项目许可。这种做法表明，你也可以指定由 `OR` 分隔的多个许可证标识符，以便为你的项目拥有多个许可证。

有了唯一的名称、版本、描述和许可证后，一个准备好发布的项目的 `Cargo.toml` 文件可能如下所示：

文件名：`Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"
description = "A fun game where you guess what number the
computer has chosen."
license = "MIT OR Apache-2.0"

[dependencies]
```

Cargo 在 *https://doc.rust-lang.org/cargo* 的文档描述了你可以指定的其他元数据，以确保其他人能够更轻松地发现和使用你的 crate。
