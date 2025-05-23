# スタックのみのデータ：Copy

まだ話していないもう 1 つの問題があります。整数を使ったこのコード（その一部はリスト 4-2 に示されています）は動作し、有効です。

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

しかし、このコードは私たちが今学んだことに矛盾しているように見えます。`clone`の呼び出しはありませんが、`x`はまだ有効で、`y`にムーブされていません。

その理由は、コンパイル時に既知のサイズを持つ整数などの型は、完全にスタックに格納されるため、実際の値のコピーを高速に作成できるからです。つまり、変数`y`を作成した後でも`x`が有効であることを阻止する理由はありません。言い換えると、ここではディープコピーとシャローコピーの違いはありません。したがって、`clone`を呼び出しても通常のシャローコピーと何も変わりません。そのため、省略することができます。

Rust には、整数のようにスタックに格納される型に対して付けることができる特別な注釈である`Copy`トレイトがあります（第 10 章でトレイトについてもっと詳しく説明します）。型が`Copy`トレイトを実装している場合、それを使用する変数はムーブせず、むしろ単純にコピーされます。したがって、別の変数に代入した後も有効になります。

型またはその一部が`Drop`トレイトを実装している場合、Rust は`Copy`で型を注釈付けさせません。値がスコープ外になるときに何か特別なことが起こる必要がある型に`Copy`注釈を追加すると、コンパイル時エラーが発生します。型に`Copy`注釈を追加してトレイトを実装する方法については、「派生可能なトレイト」を参照してください。

では、どの型が`Copy`トレイトを実装していますか？確認するには、特定の型のドキュメントを参照してくださいが、一般的なルールとして、単純なスカラー値の任意のグループは`Copy`を実装できます。割り当てが必要なものや何らかの形式のリソースは`Copy`を実装できません。以下は、`Copy`を実装する型のいくつかです。

- すべての整数型、たとえば`u32`。
- ブール型`bool`で、値は`true`と`false`。
- すべての浮動小数点数型、たとえば`f64`。
- 文字型`char`。
- タプルは、それが`Copy`を実装する型のみを含む場合に`Copy`を実装します。たとえば、`(i32, i32)`は`Copy`を実装しますが、`(i32, String)`は実装しません。
