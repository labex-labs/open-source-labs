# `assert_eq!` と `assert_ne!` マクロを使った等価性のテスト

機能を検証する一般的な方法は、テスト対象のコードの結果と、コードが返すはずの値との等価性をテストすることです。これは、`assert!` マクロを使って `==` 演算子を使った式を渡すことで行うことができます。しかし、このような一般的なテストのために、標準ライブラリには2つのマクロ `assert_eq!` と `assert_ne!` が用意されており、これらを使うことでもっと便利にこのテストを行うことができます。これらのマクロは、それぞれ2つの引数を等価性または非等価性で比較します。また、アサーションが失敗した場合、2つの値を表示します。これにより、テストが失敗した理由がわかりやすくなります。逆に、`assert!` マクロは、`==` 式に対して `false` の値を取得したことを示すだけで、`false` の値に至る値を表示しません。

リスト11-7では、`add_two` という名前の関数を書きます。この関数は、引数に2を加えます。そして、`assert_eq!` マクロを使ってこの関数をテストします。

ファイル名: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

リスト11-7: `assert_eq!` マクロを使った `add_two` 関数のテスト

合格することを確認しましょう！

    running 1 test
    test tests::it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

`assert_eq!` に引数として `4` を渡しています。これは、`add_two(2)` の呼び出し結果と等しいです。このテストの行は `test tests::it_adds_two... ok` で、`ok` のテキストが表示されることで、テストが合格したことがわかります！

コードにバグを入れて、`assert_eq!` が失敗したときの様子を見てみましょう。`add_two` 関数の実装を変更して、代わりに3を加えるようにします。

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

もう一度テストを実行します。

    running 1 test
    test tests::it_adds_two... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

テストがバグを検出しました！`it_adds_two` テストが失敗し、メッセージには、失敗したアサーションが `assertion failed:`(left == right)\``\[1\] であり、`left`\[2\] と `right`\[3\] の値が何であるかが示されています。このメッセージはデバッグを始めるのに役立ちます。`left`引数は`4` でしたが、`right`引数である`add_two(2)`の結果は`5` でした。たくさんのテストを行っている場合、これが特に役立つことが想像できます。

いくつかの言語やテストフレームワークでは、等価性アサーション関数のパラメータは `expected` と `actual` と呼ばれ、引数を指定する順序が重要です。しかし、Rustでは、それらは `left` と `right` と呼ばれ、期待する値とコードが生成する値を指定する順序は重要ではありません。このテストのアサーションを `assert_eq!(add_two(2), 4)` のように書くこともできます。これにより、`assertion failed:`(left == right)\` と表示される同じ失敗メッセージが表示されます。

`assert_ne!` マクロは、与えられた2つの値が等しくなければ合格し、等しければ失敗します。このマクロは、値が何になるかはわからないが、何になるべきではないことは確かである場合に最も役立ちます。たとえば、入力を必ず何らかの方法で変更する関数をテストしている場合、入力がどのように変更されるかはテストを実行する曜日に依存する場合、関数の出力が入力と等しくないことをアサートするのが最善策かもしれません。

表面下では、`assert_eq!` と `assert_ne!` マクロはそれぞれ `==` と `!=` 演算子を使用します。アサーションが失敗した場合、これらのマクロはデバッグフォーマットを使って引数を表示します。これは、比較される値が `PartialEq` と `Debug` トレイトを実装していることを意味します。すべてのプリミティブ型とほとんどの標準ライブラリ型はこれらのトレイトを実装しています。自分で定義する構造体や列挙型の場合、それらの型の等価性をアサートするには `PartialEq` を実装する必要があります。また、アサーションが失敗したときに値を表示するには `Debug` を実装する必要があります。両方のトレイトは派生可能なトレイトであるため、リスト5-12で述べたように、これは通常、構造体や列挙型の定義に `#[derive(PartialEq, Debug)]` 注釈を追加するだけで簡単に行えます。これらの派生可能なトレイトやその他のトレイトに関する詳細については、付録Cを参照してください。
