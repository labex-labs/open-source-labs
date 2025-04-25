# 構造体定義における寿命注釈

これまでに定義した構造体はすべて、所有型を保持していました。構造体を参照を保持するように定義することもできますが、その場合、構造体定義内の各参照に寿命注釈を付ける必要があります。リスト 10-24 には、文字列スライスを保持する`ImportantExcerpt`という名前の構造体があります。

ファイル名：`src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
       .split('.')
       .next()
       .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

リスト 10-24：参照を保持する構造体で、寿命注釈が必要

この構造体には、文字列スライス（参照）を保持する単一のフィールド`part`があります \[2\]。ジェネリックデータ型と同様に、構造体名の後に角括弧の中にジェネリック寿命パラメータの名前を宣言します。これにより、構造体定義の本体で寿命パラメータを使用できるようになります \[1\]。この注釈は、`ImportantExcerpt`のインスタンスが、その`part`フィールドに保持する参照よりも長生きすることはできないことを意味します。

ここの`main`関数は、`ImportantExcerpt`構造体のインスタンスを作成します \[5\]。このインスタンスは、変数`novel` \[3\]が所有する`String`の最初の文への参照を保持しています \[4\]。`novel`のデータは、`ImportantExcerpt`インスタンスが作成される前に存在します。また、`novel`は`ImportantExcerpt`がスコープ外になるまでスコープ外になりません。したがって、`ImportantExcerpt`インスタンス内の参照は有効です。
