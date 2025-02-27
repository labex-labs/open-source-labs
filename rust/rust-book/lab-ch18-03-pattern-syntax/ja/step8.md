# 列挙型のデストラクチャリング

この本では列挙型をデストラクチャリングしてきました（たとえば、リスト 6-5）。しかし、列挙型をデストラクチャリングするパターンが、列挙型内に格納されているデータの定義方法に対応していることについては、まだ明示的に説明していません。例として、リスト 18-15 ではリスト 6-2 の `Message` 列挙型を使用し、各内部値をデストラクチャリングするパターンを持つ `match` 式を記述しています。

ファイル名: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "The Quit variant has no data to destructure."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Move in the x dir {x}, in the y dir {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Text message: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Change color to red {r}, green {g}, and blue {b}"
        ),
    }
}
```

リスト 18-15: さまざまな種類の値を保持する列挙型のバリアントをデストラクチャリングする

このコードは `Change color to red 0, green 160, and blue 255` を出力します。`msg` \[1\] の値を変更して、他のアームのコードが実行されるのを確認してみてください。

`Message::Quit` \[2\] のようにデータを持たない列挙型のバリアントの場合、値をさらに分解することはできません。リテラルの `Message::Quit` 値にのみマッチさせることができ、そのパターンには変数がありません。

`Message::Move` \[3\] のような構造体のような列挙型のバリアントの場合、構造体にマッチさせるために指定するパターンと同様のパターンを使用できます。バリアント名の後に中括弧を置き、その中に変数付きのフィールドを列挙することで、このアームのコードで使用するために各部品を分解します。ここでは、リスト 18-13 で行ったように省略記法を使用しています。

`Message::Write` のように 1 つの要素を持つタプルを保持する \[4\] や、`Message::ChangeColor` のように 3 つの要素を持つタプルを保持する \[5\] タプルのような列挙型のバリアントの場合、パターンはタプルにマッチさせるために指定するパターンと似ています。パターン内の変数の数は、マッチさせるバリアント内の要素の数と一致する必要があります。
