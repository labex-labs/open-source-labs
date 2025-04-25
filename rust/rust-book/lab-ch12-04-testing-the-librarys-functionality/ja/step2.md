# 失敗するテストを書く

もはや必要ないので、`src/lib.rs`と`src/main.rs`から、プログラムの動作を確認するために使っていた`println!`文を削除しましょう。そして、`src/lib.rs`では、11 章でやったように、テスト関数を持つ`tests`モジュールを追加します。このテスト関数は、`search`関数が持つべき動作を指定します。つまり、クエリと検索対象のテキストを受け取り、テキストからクエリに一致する行のみを返すでしょう。リスト 12-15 にこのテストを示しますが、まだコンパイルされません。

ファイル名：`src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

リスト 12-15: 持ちたい`search`関数に対する失敗するテストを作成する

このテストは、文字列`"duct"`を検索します。検索対象のテキストは 3 行で、そのうち 1 行のみが`"duct"`を含んでいます（最初の二重引用符の後のバックスラッシュは、Rust にこの文字列リテラルの内容の先頭に改行文字を置かないように指示しています）。`search`関数から返される値が、期待する行のみを含んでいることをアサートします。

このテストを実行して失敗するのを見ることはまだできません。なぜなら、テスト自体がコンパイルされないからです。`search`関数がまだ存在しないのです！TDD の原則に従って、常に空のベクトルを返す`search`関数の定義を追加することで、テストがコンパイルされて実行されるように、必要なだけのコードを追加します。そうすると、空のベクトルが`"safe, fast, productive."`の行を含むベクトルと一致しないため、テストはコンパイルされて失敗するはずです。

ファイル名：`src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

リスト 12-16: テストがコンパイルされるように、`search`関数を十分に定義する

`search`のシグネチャで明示的な寿命期間`'a`を定義し、その寿命期間を`contents`引数と返り値に使用することに注意してください。10 章で思い出してください。寿命期間パラメータは、どの引数の寿命期間が返り値の寿命期間と関連付けられているかを指定します。この場合、返されるベクトルが、引数`contents`（引数`query`ではない）のスライスを参照する文字列スライスを含むことを示しています。

言い換えると、`search`関数が返すデータは、`contents`引数で`search`関数に渡されるデータと同じくらい長く生き続けることを Rust に伝えています。これは重要です！スライスによって参照されるデータは、参照が有効であるために有効でなければなりません。コンパイラが`query`の文字列スライスではなく`contents`の文字列スライスを作っていると仮定すると、安全性のチェックが誤って行われます。

寿命期間の注釈を忘れてこの関数をコンパイルしようとすると、このエラーが表示されます。

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust は、2 つの引数のどちらが必要かを知ることができません。だから、明示的に伝える必要があります。`contents`がすべてのテキストを含む引数で、一致するテキストの部分を返したいので、`contents`が寿命期間構文を使って返り値と関連付けられるべき引数であることがわかります。

他のプログラミング言語では、シグネチャで引数を返り値に関連付ける必要はありませんが、時間が経つにつれてこの方法が慣れるようになります。この例を「寿命期間で参照を検証する」の例と比較してみると良いかもしれません。

さて、テストを実行しましょう。

```bash
[object Object]
```

素晴らしい！テストは、予想通りに失敗しました。テストを通過させましょう！
