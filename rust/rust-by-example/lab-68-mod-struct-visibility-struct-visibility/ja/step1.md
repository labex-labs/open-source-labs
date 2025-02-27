# 構造体の可視性

構造体は、そのフィールドに関して追加の可視性レベルを持っています。可視性はデフォルトで非公開になっており、`pub` 修飾子で上書きすることができます。この可視性は、構造体が定義されているモジュールの外部からアクセスされる場合にのみ重要であり、情報を隠す（カプセル化）目的があります。

```rust
mod my {
    // ジェネリック型 `T` のパブリックフィールドを持つパブリック構造体
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // ジェネリック型 `T` のプライベートフィールドを持つパブリック構造体
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // パブリックコンストラクタメソッド
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // パブリックフィールドを持つパブリック構造体は通常通り構築できます
    let open_box = my::OpenBox { contents: "public information" };

    // そしてそのフィールドに通常アクセスできます。
    println!("The open box contains: {}", open_box.contents);

    // プライベートフィールドを持つパブリック構造体は、フィールド名を使って構築できません。
    // エラー! `ClosedBox` はプライベートフィールドを持っています
    //let closed_box = my::ClosedBox { contents: "classified information" };
    // TODO ^ この行のコメントを外してみてください

    // ただし、プライベートフィールドを持つ構造体は、
    // パブリックコンストラクタを使って作成できます
    let _closed_box = my::ClosedBox::new("classified information");

    // そして、パブリック構造体のプライベートフィールドにはアクセスできません。
    // エラー! `contents` フィールドはプライベートです
    //println!("The closed box contains: {}", _closed_box.contents);
    // TODO ^ この行のコメントを外してみてください
}
```
