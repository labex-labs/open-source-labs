# ハッシュマップ内の値にアクセスする

リスト 8-21 に示すように、`get` メソッドにキーを指定することで、ハッシュマップから値を取得することができます。

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

リスト 8-21: ハッシュマップに格納された Blue チームの得点にアクセスする

ここで、`score` は Blue チームに関連付けられた値を持ち、結果は `10` になります。`get` メソッドは `Option<&V>` を返します。ハッシュマップにそのキーに対応する値がない場合、`get` は `None` を返します。このプログラムでは、`copied` を呼び出して `Option<&i32>` ではなく `Option<i32>` を取得し、その後 `unwrap_or` を使用して、`scores` にキーのエントリがない場合に `score` をゼロに設定することで、`Option` を処理しています。

ベクターと同様に、`for` ループを使用してハッシュマップ内の各キー - 値のペアを反復処理することができます。

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

このコードは、各ペアを任意の順序で出力します。

```rust
Yellow: 50
Blue: 10
```
