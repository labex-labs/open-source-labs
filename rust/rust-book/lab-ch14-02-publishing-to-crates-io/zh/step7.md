# 设置 Crates.io 账户

在发布任何 crate 之前，你需要在 *https://crates.io* 上创建一个账户并获取一个 API 令牌。要做到这一点，访问 *https://crates.io* 的主页并通过 GitHub 账户登录。（目前需要 GitHub 账户，但该网站未来可能会支持其他创建账户的方式。）登录后，访问 *https://crates.io/me* 的账户设置并获取你的 API 密钥。然后使用你的 API 密钥运行 `cargo login` 命令，如下所示：

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

此命令会将你的 API 令牌告知 Cargo 并将其本地存储在 _\~/.cargo/credentials_ 中。请注意，此令牌是一个 **秘密**：不要与其他任何人共享。如果你出于任何原因与他人共享了它，你应该撤销它并在 *https://crates.io* 上生成一个新的令牌。
