# 複数のimplブロック

各構造体は複数の`impl`ブロックを持つことができます。たとえば、リスト5-15は、それぞれのメソッドが独自の`impl`ブロックにあるリスト5-16に示すコードと同等です。

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

リスト5-16: 複数の`impl`ブロックを使用してリスト5-15を書き直す

ここでは、これらのメソッドを複数の`impl`ブロックに分ける理由はありませんが、これは有効な構文です。第10章でジェネリック型とトレイトについて説明する際に、複数の`impl`ブロックが役に立つケースを見ます。
