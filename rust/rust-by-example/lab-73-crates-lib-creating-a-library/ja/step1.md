# ライブラリの作成

ライブラリを作成し、その後、別のクレートにリンクする方法を見てみましょう。

`rary.rs` で：

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

ライブラリは "lib" で始まり、デフォルトではクレートファイルの名前に基づいて命名されますが、このデフォルト名は、`rustc` に `--crate-name` オプションを渡すか、\[`crate_name` 属性\]\[crate-name\] を使用することで上書きできます。
