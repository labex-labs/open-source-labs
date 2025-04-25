# 凍結

データが同じ名前で不変にバインドされると、それはまた「凍結」されます。「凍結」されたデータは、不変バインドがスコープ外になるまで変更できません。

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // 不変の `_mutable_integer` によるシャドーイング
        let _mutable_integer = _mutable_integer;

        // エラー！`_mutable_integer` はこのスコープで凍結されています
        _mutable_integer = 50;
        // FIXME ^ この行をコメントアウトしてください

        // `_mutable_integer` がスコープ外になります
    }

    // オッケー！`_mutable_integer` はこのスコープでは凍結されていません
    _mutable_integer = 3;
}
```
