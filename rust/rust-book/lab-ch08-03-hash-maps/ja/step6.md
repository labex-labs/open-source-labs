# 値を上書きする

ハッシュマップにキーと値を挿入し、その後同じキーに異なる値を挿入すると、そのキーに関連付けられた値は置き換えられます。リスト 8-23 のコードでは `insert` を 2 回呼び出していますが、2 回とも Blue チームのキーに対する値を挿入しているため、ハッシュマップには 1 つのキー - 値のペアしか含まれません。

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

リスト 8-23: 特定のキーに格納された値を置き換える

このコードは `{"Blue": 25}` を出力します。元の値 `10` は上書きされています。
