# 配列要素のアクセス

配列は、スタックに割り当てることができる既知の固定サイズの単一のメモリチャンクです。インデックスを使って配列の要素にアクセスすることができます。例えば：

ファイル名：`src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

この例では、`first`と名付けられた変数は値`1`を取得します。なぜなら、それは配列のインデックス`[0]`にある値だからです。`second`と名付けられた変数は、配列のインデックス`[1]`から値`2`を取得します。
