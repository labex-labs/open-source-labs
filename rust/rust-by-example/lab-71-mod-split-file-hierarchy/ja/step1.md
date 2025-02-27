# ファイル階層

モジュールはファイル/ディレクトリ階層にマッピングできます。ファイル内の可視性の例を分解してみましょう。

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

`split.rs` の中身：

```rust
// この宣言は、`my.rs` という名前のファイルを探し、その内容をこのスコープ内の `my` という名前のモジュールの中に挿入します
mod my;

fn function() {
    println!("called `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

`my.rs` の中身：

```rust
// 同様に、`mod inaccessible` と `mod nested` は `nested.rs` と `inaccessible.rs` ファイルを探し、それぞれのモジュールの下にここに挿入します
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("called `my::function()`");
}

fn private_function() {
    println!("called `my::private_function()`");
}

pub fn indirect_access() {
    print!("called `my::indirect_access()`, that\n> ");

    private_function();
}
```

`my/nested.rs` の中身：

```rust
pub fn function() {
    println!("called `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("called `my::nested::private_function()`");
}
```

`my/inaccessible.rs` の中身：

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("called `my::inaccessible::public_function()`");
}
```

以前と同じように動作することを確認しましょう：

```shell
$ rustc split.rs &&./split
called `my::function()`
called `function()`
called `my::indirect_access()`, that
> called `my::private_function()`
called `my::nested::function()`
```
