# クレート

`crate_type` 属性を使用すると、コンパイラにクレートがバイナリであるかライブラリであるか（さらにはどの種類のライブラリであるか）を伝えることができ、`crate_name` 属性を使用すると、クレートの名前を設定することができます。

ただし、重要なことは、Rust パッケージマネージャである Cargo を使用する場合、`crate_type` および `crate_name` 属性の両方がまったく効果を持たないことです。Cargo は大多数の Rust プロジェクトで使用されるため、これは `crate_type` と `crate_name` の実際の使用例が比較的限られていることを意味します。

```rust
// このクレートはライブラリです
#![crate_type = "lib"]
// ライブラリの名前は "rary" です
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

`crate_type` 属性を使用するとき、`--crate-type` フラグを `rustc` に渡す必要はありません。

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
