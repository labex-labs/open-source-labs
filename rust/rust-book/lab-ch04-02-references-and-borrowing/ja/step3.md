# 浮動参照

ポインタを持つ言語では、メモリの一部を解放しながらそのメモリへのポインタを保持することで、誤って「浮動ポインタ」（メモリ内の場所を参照するポインタであって、他の誰かに与えられている可能性のある場所を参照するもの）を作成してしまうことが簡単です。対照的に、Rustでは、コンパイラが参照が浮動参照になることは決してないことを保証しています。つまり、あるデータへの参照がある場合、コンパイラは、そのデータへの参照がなくなる前に、そのデータがスコープ外にならないようにします。

浮動参照を作成して、Rustがコンパイル時エラーでそれを防ぐ方法を見てみましょう。

ファイル名: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

エラーはこちらです。

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

このエラーメッセージは、まだ扱っていない機能である「生存期間」に関連しています。第10章で生存期間について詳細に説明します。ただし、生存期間に関する部分を無視すると、このエラーメッセージには、なぜこのコードが問題なのかを示す鍵が含まれています。

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

`dangle`コードの各段階で実際に何が起こっているか、もう少し詳しく見てみましょう。

    // src/main.rs
    fn dangle() -> &String { // dangleはStringへの参照を返す

        let s = String::from("hello"); // sは新しいString

        &s // String、sへの参照を返す
    } // ここで、sはスコープ外になり、破棄されます。したがって、そのメモリは消えます
      // 危険！

`s`は`dangle`の中で作成されるため、`dangle`のコードが終了すると、`s`はデアロケートされます。しかし、その参照を返そうとしました。つまり、この参照は無効な`String`を指すことになります。これは良くありません！ Rustはこれを許さないです。

ここでの解決策は、直接`String`を返すことです。

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

これは問題なく動作します。所有権が移動し、何もデアロケートされません。
