# 列挙型

`enum` キーワードを使うと、いくつかの異なるバリアントのいずれかである型を作成できます。`struct` として有効な任意のバリアントは、`enum` でも有効です。

```rust
// ウェブイベントを分類するための `enum` を作成します。名前と型情報の両方がバリアントを指定する方法に注意してください。
// `PageLoad!= PageUnload` であり、`KeyPress(char)!= Paste(String)` です。それぞれが異なり、独立しています。
enum WebEvent {
    // `enum` のバリアントは、`ユニット型のような`
    PageLoad,
    PageUnload,
    // `タプル構造体のような`
    KeyPress(char),
    Paste(String),
    // または `C 言語のような構造体`
    Click { x: i64, y: i64 },
}

// `WebEvent` 列挙型を引数として受け取り、何も返さない関数
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        // `enum` のバリアントの中から `c` を分解します。
        WebEvent::KeyPress(c) => println!("pressed '{}'.", c),
        WebEvent::Paste(s) => println!("pasted \"{}\".", s),
        // `Click` を `x` と `y` に分解します。
        WebEvent::Click { x, y } => {
            println!("clicked at x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` は、文字列スライスから所有権のある `String` を作成します。
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## 型エイリアス

型エイリアスを使うと、列挙型の各バリアントをそのエイリアスで参照できます。列挙型の名前が長すぎたり、一般的すぎたりして、名前を変更したい場合に便利です。

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// 型エイリアスを作成
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // 長くて不便な名前ではなく、エイリアスを使って各バリアントを参照できます。
    let x = Operations::Add;
}
```

これが最も一般的に見られるのは、`Self` エイリアスを使った `impl` ブロックです。

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

列挙型と型エイリアスに関する詳細を学ぶには、この機能が Rust に安定化されたときの安定化レポートを読むことができます。
