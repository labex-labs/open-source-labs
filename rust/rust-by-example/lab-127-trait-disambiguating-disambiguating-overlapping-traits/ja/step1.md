# 重複する特性を明確に区別する

型は複数の異なる特性を実装できます。2 つの特性が同じ名前を必要とする場合どうなるでしょうか？たとえば、多くの特性には `get()` という名前のメソッドがあるかもしれません。戻り値の型が異なる場合さえあります！

良いニュース：各特性の実装には独自の `impl` ブロックがあるため、どの特性の `get` メソッドを実装しているかは明確です。

それらのメソッドを _呼び出す_ ときはどうでしょうか？それらを区別するには、完全修飾構文を使用する必要があります。

```rust
trait UsernameWidget {
    // このウィジェットから選択されたユーザー名を取得する
    fn get(&self) -> String;
}

trait AgeWidget {
    // このウィジェットから選択された年齢を取得する
    fn get(&self) -> u8;
}

// UsernameWidget と AgeWidget の両方を持つフォーム
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // この行のコメントを外すと、「複数の `get` が見つかりました」というエラーが表示されます。
    // 結局のところ、`get` という名前のメソッドが複数あるからです。
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
