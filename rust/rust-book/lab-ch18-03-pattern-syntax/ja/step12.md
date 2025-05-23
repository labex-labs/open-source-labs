# `_` で値全体を無視する

私たちは、任意の値にマッチするが値にバインドしないワイルドカードパターンとしてアンダースコアを使用してきました。これは `match` 式の最後のアームとして特に便利ですが、リスト 18-17 に示すように、関数パラメータを含む任意のパターンで使用することもできます。

ファイル名：`src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("This code only uses the y parameter: {y}");
}

fn main() {
    foo(3, 4);
}
```

リスト 18-17: 関数シグネチャで `_` を使用する

このコードは、最初の引数として渡された値 `3` を完全に無視し、`This code only uses the y parameter: 4` を出力します。

ほとんどの場合、特定の関数パラメータが不要になったときは、シグネチャを変更して未使用のパラメータを含まないようにします。たとえば、特定の型シグネチャが必要なトレイトを実装する場合で、実装内の関数本体があるパラメータを必要としない場合、関数パラメータを無視することは特に便利です。そうすることで、名前を使用した場合に発生する未使用の関数パラメータに関するコンパイラの警告を回避できます。
