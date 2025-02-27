# より多くのパラメータを持つメソッド

`Rectangle`構造体に2番目のメソッドを実装することで、メソッドの使用方法を練習しましょう。今回は、`Rectangle`のインスタンスに別の`Rectangle`のインスタンスを渡し、2番目の`Rectangle`が`self`（最初の`Rectangle`）の中に完全に収まる場合に`true`を返します。そうでない場合は`false`を返します。つまり、`can_hold`メソッドを定義した後は、リスト5-14に示すプログラムを書けるようになります。

ファイル名: `src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

リスト5-14: まだ書かれていない`can_hold`メソッドを使用する

期待される出力は次のようになります。`rect2`の両方の寸法が`rect1`の寸法より小さいためですが、`rect3`は`rect1`よりも幅が広いです。

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

メソッドを定義することがわかっているので、`impl Rectangle`ブロック内にあるはずです。メソッド名は`can_hold`になり、別の`Rectangle`の不変借用をパラメータとして取ります。メソッドを呼び出すコードを見ることで、パラメータの型を判断できます。`rect1.can_hold(&rect2)`は`&rect2`を渡しています。これは`rect2`（`Rectangle`のインスタンス）への不変借用です。これは理にかなっています。なぜなら、`rect2`を読み取るだけで済む（書き込む場合は可変借用が必要になります）ため、`main`が`rect2`の所有権を保持して、`can_hold`メソッドを呼び出した後も再利用できるようにするためです。`can_hold`の戻り値はブール値になり、実装では`self`の幅と高さがそれぞれ他の`Rectangle`の幅と高さより大きいかどうかを確認します。リスト5-13の`impl`ブロックに新しい`can_hold`メソッドを追加しましょう。リスト5-15に示します。

ファイル名: `src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

リスト5-15: 別の`Rectangle`インスタンスをパラメータとして持つ`Rectangle`に`can_hold`メソッドを実装する

リスト5-14の`main`関数でこのコードを実行すると、期待される出力が得られます。メソッドは`self`パラメータの後にシグネチャに追加する複数のパラメータを持つことができ、それらのパラメータは関数のパラメータと同じように機能します。
