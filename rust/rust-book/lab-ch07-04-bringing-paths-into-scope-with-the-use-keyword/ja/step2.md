# 慣用的な use パスの作成

リスト 7-11 では、なぜ `use crate::front_of_house::hosting` を指定してから、`eat_at_restaurant` で `hosting::add_to_waitlist` を呼び出したのか、リスト 7-13 のように、同じ結果を得るために `add_to_waitlist` 関数までの `use` パスを指定しなかったのか疑問に思ったかもしれません。

ファイル名: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

リスト 7-13: `use` を使って `add_to_waitlist` 関数をスコープに持ち込む、非慣用的な方法

リスト 7-11 とリスト 7-13 のどちらも同じタスクを達成していますが、リスト 7-11 が `use` を使って関数をスコープに持ち込む慣用的な方法です。`use` を使って関数の親モジュールをスコープに持ち込むことは、関数を呼び出す際に親モジュールを指定する必要があることを意味します。関数を呼び出す際に親モジュールを指定することで、関数がローカルで定義されていないことが明確になり、同時に完全なパスの繰り返しを最小限に抑えます。リスト 7-13 のコードは、`add_to_waitlist` がどこに定義されているか不明です。

一方、`use` を使って構造体、列挙体、その他の項目を持ち込む場合、完全なパスを指定するのが慣用的です。リスト 7-14 は、標準ライブラリの `HashMap` 構造体をバイナリ クレートのスコープに持ち込む慣用的な方法を示しています。

ファイル名: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

リスト 7-14: 慣用的な方法で `HashMap` をスコープに持ち込む

この慣用的な書き方には強い理由はありません。ただ、このような慣用的な書き方が生まれ、人々がこのように Rust コードを読み書きするようになっただけです。

この慣用的な書き方の例外は、同じ名前の 2 つの項目を `use` 文でスコープに持ち込む場合です。なぜなら、Rust はそれを許可していないからです。リスト 7-15 は、同じ名前で異なる親モジュールを持つ 2 つの `Result` 型をスコープに持ち込む方法と、それらを参照する方法を示しています。

ファイル名: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

リスト 7-15: 同じ名前の 2 つの型を同じスコープに持ち込むには、それらの親モジュールを使用する必要があります。

ご覧の通り、親モジュールを使用することで 2 つの `Result` 型が区別されます。代わりに `use std::fmt::Result` と `use std::io::Result` を指定した場合、同じスコープ内に 2 つの `Result` 型があり、`Result` を使用した際に Rust はどちらを意味するのかわかりません。
