# 寿命について考える

寿命パラメータを指定する必要がある方法は、関数が何を行っているかに依存します。たとえば、`longest`関数の実装を変更して、常に最初のパラメータを返すようにして、最長の文字列スライスではなくする場合、`y`パラメータに寿命を指定する必要はありません。次のコードはコンパイルされます。

ファイル名：`src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

パラメータ`x`と返り値には寿命パラメータ`'a`を指定しましたが、パラメータ`y`には指定していません。なぜなら、`y`の寿命は`x`の寿命や返り値の寿命とは何の関係もありませんからです。

関数から参照を返す場合、返り値の寿命パラメータは、パラメータのうちの 1 つの寿命パラメータと一致する必要があります。返される参照がパラメータのいずれかを参照しない場合、それはこの関数内で作成された値を参照する必要があります。しかし、これはダングリング参照になります。なぜなら、値は関数の終了時にスコープ外になりますからです。コンパイルされない`longest`関数のこのような試みた実装を考えてみましょう。

ファイル名：`src/main.rs`

```rust
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

ここでは、返り値の型に寿命パラメータ`'a`を指定しましたが、この実装はコンパイルに失敗します。なぜなら、返り値の寿命はパラメータの寿命とまったく関係がないからです。得られるエラーメッセージは次の通りです。

```bash
error[E0515]: cannot return reference to local variable `result`
  --> src/main.rs:11:5
   |
11 |     result.as_str()
   |     ^^^^^^^^^^^^^^^ returns a reference to data owned by the
current function
```

問題は、`result`がスコープ外になり、`longest`関数の終了時にクリーンアップされることです。また、関数から`result`への参照を返そうとしています。ダングリング参照を変更する寿命パラメータを指定する方法はありません。そして、Rust はダングリング参照を作成させません。この場合、最善の解決策は、返される型を所有型にすることで、呼び出し元の関数に値のクリーンアップの責任を持たせることです。

結局のところ、寿命構文は、関数のさまざまなパラメータと返り値の寿命を結び付けるものです。それらが結び付けられると、Rust はメモリセーフな操作を許可し、ダングリングポインタを作成する操作やそれ以外のメモリセーフ違反を許可しないための十分な情報を持つようになります。
