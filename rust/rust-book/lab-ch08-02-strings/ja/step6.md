# +演算子または format! マクロを使った連結

多くの場合、既存の 2 つの文字列を結合したいと思うでしょう。その方法の 1 つは、`+`演算子を使うことです。これはリスト 8-18 に示されています。

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // 注：s1 はここで所有権が移され、もはや使用できなくなります
```

リスト 8-18:2 つの`String`値を新しい`String`値に結合するために`+`演算子を使用する

文字列`s3`には`Hello, world!`が含まれます。追加後に`s1`がもはや有効でなくなる理由と、`s2`への参照を使用した理由は、`+`演算子を使用したときに呼び出されるメソッドのシグネチャに関係しています。`+`演算子は`add`メソッドを使用しており、そのシグネチャは次のようになっています。

```rust
fn add(self, s: &str) -> String {
```

標準ライブラリでは、`add`はジェネリックと関連型を使用して定義されています。ここでは、具体的な型を代入しています。これは、`String`値でこのメソッドを呼び出したときに起こることです。第 10 章でジェネリックについて説明します。このシグネチャは、`+`演算子の厄介な部分を理解するために必要な手がかりを与えてくれます。

まず、`s2`には`&`があります。これは、2 番目の文字列を最初の文字列に追加する際に、2 番目の文字列の「参照」を追加していることを意味します。これは`add`関数の`s`パラメータのためです。`String`には`&str`だけを追加できます。2 つの`String`値を一緒に追加することはできません。しかし、待ってください。`&s2`の型は`&String`であり、`add`の 2 番目のパラメータに指定されている`&str`ではありません。では、なぜリスト 8-18 がコンパイルされるのでしょうか？

`add`の呼び出しで`&s2`を使用できる理由は、コンパイラが`&String`引数を`&str`に「強制変換」できるからです。`add`メソッドを呼び出すとき、Rust は「参照解決強制変換」を使用します。ここでは、`&s2`を`&s2[..]`に変換します。第 15 章で参照解決強制変換についてもっと深く説明します。`add`は`s`パラメータの所有権を取得しないため、この操作の後も`s2`は有効な`String`のままです。

2 番目に、シグネチャから`add`が`self`の所有権を取得することがわかります。なぜなら`self`には`&`がないからです。これは、リスト 8-18 の`s1`が`add`呼び出しに所有権が移され、その後はもはや有効でなくなることを意味します。したがって、`let s3 = s1 + &s2;`は 2 つの文字列をコピーして新しい文字列を作成するように見えますが、このステートメントは実際には`s1`の所有権を取得し、`s2`の内容のコピーを追加してから、結果の所有権を返します。言い換えると、たくさんのコピーを作成しているように見えますが、そうではありません。実装はコピーよりも効率的です。

複数の文字列を連結する必要がある場合、`+`演算子の動作は厄介になります。

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

この時点で、`s`は`tic-tac-toe`になります。すべての`+`と`"`文字があると、何が起こっているのかがわかりにくくなります。より複雑な方法で文字列を結合する場合は、代わりに`format!`マクロを使用できます。

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

このコードも`s`を`tic-tac-toe`に設定します。`format!`マクロは`println!`と同じように機能しますが、画面に出力する代わりに、内容を持つ`String`を返します。`format!`を使用したコードのバージョンははるかに読みやすく、`format!`マクロによって生成されるコードは参照を使用するため、この呼び出しはパラメータのいずれの所有権も取得しません。
