# テストケース: リンクリスト

リンクリストを実装する一般的な方法は、`enum` を使うことです。

```rust
use crate::List::*;

enum List {
    // Cons: 要素と次のノードへのポインタをラップするタプル構造体
    Cons(u32, Box<List>),
    // Nil: リンクリストの終端を示すノード
    Nil,
}

// メソッドを列挙型に追加できます
impl List {
    // 空のリストを作成する
    fn new() -> List {
        // `Nil` は `List` 型を持つ
        Nil
    }

    // リストを消費し、先頭に新しい要素を持つ同じリストを返す
    fn prepend(self, elem: u32) -> List {
        // `Cons` も `List` 型を持つ
        Cons(elem, Box::new(self))
    }

    // リストの長さを返す
    fn len(&self) -> u32 {
        // `self` をマッチングする必要があります。このメソッドの動作は
        // `self` のバリアントに依存するためです。
        // `self` は `&List` 型を持ち、`*self` は `List` 型を持ちます。
        // 具体的な型 `T` でのマッチングは、参照 `&T` でのマッチングよりも好ましいです。
        // Rust 2018 以降は、ここで `self` を使い、以下で `tail` (参照なし) を使うこともできます。
        // Rust は `&s` と `ref tail` を推論します。
        // https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html を参照
        match *self {
            // 末尾の所有権を取得できません。`self` は借用されているためです。
            // 代わりに末尾への参照を取得します。
            Cons(_, ref tail) => 1 + tail.len(),
            // 基本ケース: 空のリストは長さがゼロです
            Nil => 0
        }
    }

    // リストの表現を (ヒープ割り当て) 文字列として返す
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` は `print!` に似ていますが、コンソールに出力する代わりに
                // ヒープ割り当ての文字列を返します。
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // 空のリンクリストを作成する
    let mut list = List::new();

    // いくつかの要素を先頭に追加する
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // リストの最終状態を表示する
    println!("linked list has length: {}", list.len());
    println!("{}", list.stringify());
}
```
