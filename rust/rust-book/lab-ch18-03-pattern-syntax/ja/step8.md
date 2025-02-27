# 列挙型の分解

この本では列挙型を分解してきました（たとえば、リスト6-5）が、列挙型を分解するためのパターンが、列挙型内に格納されているデータの定義方法に対応することについては、まだ明示的に議論していません。例として、リスト18-15では、リスト6-2の `Message` 列挙型を使用し、各内部値を分解するパターンを持つ `match` を書いています。

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

リスト18-15: さまざまな種類の値を保持する列挙型のバリアントを分解する

このコードは `Change color to red 0, green 160, and blue 255` を出力します。`msg` の値を \[1\] 変更して、他のアームのコードが実行されることを確認してみてください。

データを持たない列挙型のバリアント、たとえば `Message::Quit` \[2\] の場合、値をさらに分解することはできません。`Message::Quit` のリテラル値のみでマッチすることができ、そのパターンには変数はありません。

構造体型の列挙型のバリアント、たとえば `Message::Move` \[3\] の場合、構造体をマッチさせるために指定するパターンと同じようなパターンを使うことができます。バリアント名の後に波括弧を置き、その後に変数付きのフィールドを列挙することで、このアームのコードで使用するために各部分を分解します。ここでは、リスト18-13と同じように省略形を使っています。

タプル型の列挙型のバリアント、たとえば1つの要素を持つタプルを保持する `Message::Write` \[4\] と3つの要素を持つタプルを保持する `Message::ChangeColor` \[5\] の場合、パターンはタプルをマッチさせるために指定するパターンと同じです。パターン内の変数の数は、マッチさせるバリアント内の要素の数と一致しなければなりません。