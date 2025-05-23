# 名前付き変数のマッチング

名前付き変数は、あらゆる値にマッチする反駁不能パターンであり、この本で何度も使用してきました。ただし、`match` 式の中で名前付き変数を使用すると、少し複雑な状況が生じます。`match` は新しいスコープを開始するため、`match` 式内のパターンの一部として宣言された変数は、`match` 構文の外で同じ名前の変数をシャドウイングします。これはすべての変数に当てはまります。リスト 18-11 では、値が `Some(5)` の `x` という名前の変数と、値が `10` の `y` という名前の変数を宣言しています。そして、`x` の値に対して `match` 式を作成しています。マッチアームのパターンと最後の `println!` を見て、このコードを実行する前、またはこれ以降を読む前に、コードが何を出力するかを考えてみてください。

ファイル名：`src/main.rs`

```rust
fn main() {
  1 let x = Some(5);
  2 let y = 10;

    match x {
      3 Some(50) => println!("Got 50"),
      4 Some(y) => println!("Matched, y = {y}"),
      5 _ => println!("Default case, x = {:?}", x),
    }

  6 println!("at the end: x = {:?}, y = {y}", x);
}
```

リスト 18-11: シャドウイングされた変数 `y` を導入するアームを持つ `match` 式

`match` 式が実行されたときに何が起こるかを見ていきましょう。最初のマッチアーム \[3\] のパターンは、定義された `x` の値 \[1\] とマッチしないため、コードは続行されます。

2 番目のマッチアーム \[4\] のパターンは、`Some` 値の中のあらゆる値にマッチする `y` という名前の新しい変数を導入します。`match` 式の中は新しいスコープなので、これは最初に値 `10` で宣言した `y` \[2\] ではなく、新しい `y` 変数です。この新しい `y` バインディングは、`Some` の中のあらゆる値にマッチします。これは `x` に含まれるものです。したがって、この新しい `y` は `x` の `Some` の内側の値にバインドされます。その値は `5` なので、そのアームの式が実行され、`Matched, y = 5` が出力されます。

もし `x` が `Some(5)` ではなく `None` 値だった場合、最初の 2 つのアームのパターンはマッチしないため、値はアンダースコア \[5\] にマッチします。アンダースコアアームのパターンでは `x` 変数を導入していないため、式の中の `x` は依然としてシャドウイングされていない外側の `x` です。この仮定の場合、`match` は `Default case, x = None` を出力します。

`match` 式が終了すると、そのスコープも終了し、内側の `y` のスコープも終了します。最後の `println!` \[6\] は `at the end: x = Some(5), y = 10` を出力します。

シャドウイングされた変数を導入するのではなく、外側の `x` と `y` の値を比較する `match` 式を作成するには、代わりにマッチガード条件を使用する必要があります。マッチガードについては、「マッチガードによる追加条件」で説明します。
