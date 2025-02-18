# ハッシュマップと所有権

`i32` のように `Copy` トレイトを実装している型の場合、値はハッシュマップにコピーされます。`String` のような所有権を持つ値の場合、値はムーブされ、ハッシュマップがそれらの値の所有者になります。これはリスト 8-22 で示されています。

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

リスト 8-22: キーと値が挿入されると、ハッシュマップがそれらを所有することを示す

`insert` を呼び出して `field_name` と `field_value` がハッシュマップにムーブされた後は、これらの変数を使用することはできません。

値の参照をハッシュマップに挿入した場合、値はハッシュマップにムーブされません。参照が指す値は、少なくともハッシュマップが有効である間は有効でなければなりません。これらの問題については、「ライフタイムで参照を検証する」で詳しく説明します。
