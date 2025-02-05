# 包（Crate）

`crate_type` 属性可用于告知编译器一个包是二进制可执行文件还是库（甚至是哪种类型的库），而 `crate_name` 属性可用于设置包的名称。

不过，需要注意的是，在使用 Rust 包管理器 Cargo 时，`crate_type` 和 `crate_name` 属性都**完全**无效。由于 Cargo 被用于大多数 Rust 项目，这意味着 `crate_type` 和 `crate_name` 在实际中的使用相对有限。

```rust
// 此包是一个库
#![crate_type = "lib"]
// 该库名为 "rary"
#![crate_name = "rary"]

pub fn public_function() {
    println!("called rary's `public_function()`");
}

fn private_function() {
    println!("called rary's `private_function()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that\n> ");

    private_function();
}
```

当使用 `crate_type` 属性时，我们不再需要向 `rustc` 传递 `--crate-type` 标志。

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
