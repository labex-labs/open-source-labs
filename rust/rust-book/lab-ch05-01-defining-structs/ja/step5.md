# フィールドのないユニット型の構造体

フィールドがまったくない構造体も定義できます！これらは*ユニット型に似た構造体*と呼ばれます。なぜなら、「タプル型」で言及したユニット型`()`と同じように振る舞うからです。ユニット型に似た構造体は、特定の型に対してトレイトを実装する必要があるが、型自体に格納したいデータがない場合に便利です。第10章でトレイトについて説明します。以下は、`AlwaysEqual`という名前のユニット構造体を宣言してインスタンス化する例です。

ファイル名: `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

`AlwaysEqual`を定義するには、`struct`キーワードと望む名前、そしてセミコロンを使います。波括弧や丸括弧は必要ありません！その後、同じように`subject`変数に`AlwaysEqual`のインスタンスを取得できます。定義した名前を使って、波括弧や丸括弧は不要です。後でこの型に対して、`AlwaysEqual`のすべてのインスタンスが他の任意の型のすべてのインスタンスと常に等しくなるような動作を実装すると想像してみてください。たとえば、テスト目的で既知の結果を得るためです。その動作を実装するにはデータは必要ありません！第10章では、ユニット型に似た構造体を含む任意の型に対してトレイトを定義して実装する方法を説明します。

> **構造体データの所有権**
>
> リスト5-1の`User`構造体の定義では、所有権のある`String`型を`&str`文字列スライス型の代わりに使用しました。これは意図的な選択です。なぜなら、この構造体の各インスタンスがすべてのデータを所有し、そのデータが構造体全体が有効な限り有効であることを望むからです。
>
> 構造体が他のものが所有するデータへの参照を格納することも可能ですが、そのためには*寿命期間指定子*を使用する必要があります。これはRustの機能で、第10章で説明します。寿命期間指定子は、構造体が参照するデータが構造体が有効な限り有効であることを保証します。`src/main.rs`に以下のように、寿命期間指定子を指定せずに構造体に参照を格納しようとすると、うまくいきません。
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> コンパイラは寿命期間指定子が必要だとエラーを表示します。
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> 第10章では、これらのエラーを修正して構造体に参照を格納できるようにする方法について説明しますが、今のところ、このようなエラーを修正するために、`&str`のような参照の代わりに`String`のような所有権のある型を使用します。
