# 发布现有 crate 的新版本

当你对你的 crate 进行了更改并准备发布新版本时，你需要更改 `Cargo.toml` 文件中指定的 `version` 值，然后重新发布。根据你所做更改的类型，使用位于 *http://semver.org* 的语义化版本控制（Semantic Versioning）规则来确定下一个合适的版本号。然后运行 `cargo publish` 来上传新版本。
