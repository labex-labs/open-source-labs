# for ループ

`for` ループでは、キーワード `for` の直後の値はパターンです。たとえば、`for x in y` では、`x` がパターンです。リスト18-3は、`for` ループの一部としてタプルを分解するために、`for` ループでパターンを使用する方法を示しています。

ファイル名: `src/main.rs`

```rust
let v = vec!['a', 'b', 'c'];

for (index, value) in v.iter().enumerate() {
    println!("{value} is at index {index}");
}
```

リスト18-3: `for` ループでパターンを使用してタプルを分解する

リスト18-3のコードは、次のように表示されます。

    a is at index 0
    b is at index 1
    c is at index 2

`enumerate` メソッドを使用して反復子を調整することで、その値とその値のインデックスをタプルに格納した値を生成します。生成される最初の値はタプル `(0, 'a')` です。この値がパターン `(index, value)` と一致すると、`index` は `0` になり、`value` は `'a'` になり、出力の最初の行が表示されます。
