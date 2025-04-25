# 複数の impl ブロック

各構造体は複数の`impl`ブロックを持つことができます。たとえば、リスト 5-15 は、それぞれのメソッドが独自の`impl`ブロックにあるリスト 5-16 に示すコードと同等です。

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

リスト 5-16: 複数の`impl`ブロックを使用してリスト 5-15 を書き直す

ここでは、これらのメソッドを複数の`impl`ブロックに分ける理由はありませんが、これは有効な構文です。第 10 章でジェネリック型とトレイトについて説明する際に、複数の`impl`ブロックが役に立つケースを見ます。
