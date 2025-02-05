# 创建一个库

让我们创建一个库，然后看看如何将它链接到另一个 crate。

在 `rary.rs` 中：

```rust
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

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

库的文件名前缀为 "lib"，并且默认情况下它们会根据其 crate 文件命名，但可以通过向 `rustc` 传递 `--crate-name` 选项或使用 \[`crate_name` 属性\]\[crate-name\] 来覆盖这个默认名称。
