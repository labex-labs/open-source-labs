# ライブラリの使用

この新しいライブラリにクレートをリンクするには、`rustc` の `--extern` フラグを使用できます。その後、そのすべての項目は、ライブラリと同じ名前のモジュールの下にインポートされます。このモジュールは一般的に、他の任意のモジュールと同じように動作します。

```rust
// extern crate rary; // Rust 2015 エディション以前では必要な場合があります

fn main() {
    rary::public_function();

    // エラー！`private_function` は非公開です
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# library.rlib がコンパイル済みライブラリのパスで、ここでは同じディレクトリにあると仮定します。
$ rustc executable.rs --extern rary=library.rlib &&./executable
rary の `public_function()` を呼び出しました
rary の `indirect_access()` を呼び出しました。それは
> rary の `private_function()` を呼び出しました
```
