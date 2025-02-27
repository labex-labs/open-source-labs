# use

`use` 宣言を使用することで、手動でのスコープ設定が不要になります。

```rust
// 未使用のコードに対する警告を非表示にする属性。
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // 各名前を明示的に `use` することで、手動でのスコープ設定なしで利用できるようになります。
    use crate::Status::{Poor, Rich};
    // `Work` 内の各名前を自動的に `use` します。
    use crate::Work::*;

    // `Status::Poor` に相当します。
    let status = Poor;
    // `Work::Civilian` に相当します。
    let work = Civilian;

    match status {
        // 上の明示的な `use` により、スコープ設定が不要であることに注意してください。
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        // 再びスコープ設定が不要であることに注意してください。
        Civilian => println!("Civilians work!"),
        Soldier  => println!("Soldiers fight!"),
    }
}
```
