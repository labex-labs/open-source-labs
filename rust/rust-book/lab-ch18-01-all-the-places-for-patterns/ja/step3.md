# 条件付き if let 式

第 6 章では、主に 1 つのケースのみを照合する `match` と同等のものを書くための短い方法として `if let` 式をどのように使用するかについて説明しました。任意で、`if let` には、`if let` のパターンが一致しない場合に実行するコードを含む対応する `else` を持つことができます。

リスト 18-1 に示すように、`if let`、`else if`、および `else if let` 式を組み合わせることも可能です。これにより、パターンと比較する値を 1 つだけ表現できる `match` 式よりも柔軟性が高くなります。また、Rust では、一連の `if let`、`else if`、および `else if let` アームの条件が互いに関連している必要はありません。

リスト 18-1 のコードは、いくつかの条件を一連のチェックに基づいて背景色を決定します。この例では、実際のプログラムがユーザー入力から受け取る可能性のあるハードコードされた値を持つ変数を作成しました。

ファイル名：`src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

リスト 18-1: `if let`、`else if`、`else if let`、および `else` の組み合わせ

ユーザーがお気に入りの色を指定している場合 \[1\]、その色が背景色として使用されます \[2\]。お気に入りの色が指定されておらず、今日が火曜日の場合 \[3\]、背景色は緑になります \[4\]。それ以外の場合、ユーザーが年齢を文字列として指定し、それを数値として正常に解析できる場合 \[5\]、数値の値に応じて色は紫色 \[7\] またはオレンジ色 \[8\] になります \[6\]。これらの条件がすべて当てはまらない場合 \[9\]、背景色は青色になります \[10\]。

この条件付き構造により、複雑な要件に対応できます。ここではハードコードされた値を使用していますが、この例では `Using purple as the background color` が表示されます。

`if let` 式を使用する欠点は、コンパイラが網羅性をチェックしないことです。一方、`match` 式の場合はチェックします。最後の `else` ブロック \[9\] を省略し、いくつかのケースを処理しないままにした場合、コンパイラは潜在的な論理バグについて警告しません。
