# 関数におけるジェネリックな寿命

2つの文字列スライスのうち、長い方を返す関数を書きます。この関数は2つの文字列スライスを受け取り、1つの文字列スライスを返します。`longest`関数を実装した後、リスト10-19のコードは`The longest string is abcd`と表示するはずです。

ファイル名: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

リスト10-19：2つの文字列スライスのうち、長い方を見つけるために`longest`関数を呼び出す`main`関数

`longest`関数には、所有権を持たないように、参照である文字列スライスを引数として渡したいことに注意してください。リスト10-19で使用している引数がなぜ必要なのかについては、「引数としての文字列スライス」を参照してください。

リスト10-20に示すように`longest`関数を実装しようとすると、コンパイルされません。

ファイル名: `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

リスト10-20：2つの文字列スライスのうち、長い方を返す`longest`関数の実装例ですが、まだコンパイルできません

代わりに、寿命に関する次のエラーが表示されます。

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

ヘルプメッセージによると、返り値にはジェネリックな寿命パラメータが必要です。なぜなら、Rustは返される参照が`x`または`y`を参照しているかどうかを判断できないからです。実際、この関数の本体の`if`ブロックは`x`への参照を返し、`else`ブロックは`y`への参照を返すため、私たち自身もわかりません！

この関数を定義するとき、この関数に渡される具体的な値はわかりません。したがって、`if`の場合と`else`の場合のどちらが実行されるかわかりません。また、渡される参照の具体的な寿命もわかりません。したがって、リスト10-17と10-18のようにスコープを見て、返す参照が常に有効であるかどうかを判断することはできません。借用チェッカーもこれを判断できません。なぜなら、`x`と`y`の寿命が返り値の寿命とどのように関係しているかを知らないからです。このエラーを修正するには、参照間の関係を定義するジェネリックな寿命パラメータを追加して、借用チェッカーが分析を行えるようにします。
