# RefCell`<T>` を使って実行時に借用を追跡する

不変参照と可変参照を作成する際、それぞれ `&` と `&mut` の構文を使用します。`RefCell<T>` では、`borrow` と `borrow_mut` メソッドを使用します。これらは、`RefCell<T>` に属する安全な API の一部です。`borrow` メソッドはスマートポインタ型 `Ref<T>` を返し、`borrow_mut` はスマートポインタ型 `RefMut<T>` を返します。両方の型は `Deref` を実装しているため、通常の参照のように扱うことができます。

`RefCell<T>` は、現在アクティブな `Ref<T>` と `RefMut<T>` スマートポインタの数を追跡します。`borrow` を呼び出すたびに、`RefCell<T>` はアクティブな不変借用の数をカウントアップします。`Ref<T>` 値がスコープ外になると、不変借用の数は 1 減少します。コンパイル時の借用規則と同様に、`RefCell<T>` はいつでも複数の不変借用または 1 つの可変借用を許可します。

これらの規則に違反しようとすると、参照の場合と同じようにコンパイラエラーが発生するのではなく、`RefCell<T>` の実装は実行時にパニックになります。リスト 15-23 は、リスト 15-22 の `send` の実装の修正版を示しています。同じスコープ内に 2 つの可変借用を作成して、`RefCell<T>` が実行時にこれを防ぐことを示すために、意図的に違反しています。

ファイル名：`src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

リスト 15-23：`RefCell<T>` がパニックになることを確認するために、同じスコープ内に 2 つの可変参照を作成する

`borrow_mut` から返される `RefMut<T>` スマートポインタ用に変数 `one_borrow` を作成します。その後、同じ方法で変数 `two_borrow` に別の可変借用を作成します。これにより、同じスコープ内に 2 つの可変参照が作成され、これは許可されていません。ライブラリのテストを実行すると、リスト 15-23 のコードはエラーなくコンパイルされますが、テストは失敗します。

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

メッセージ `already borrowed: BorrowMutError` でパニックになったことに注意してください。これが、`RefCell<T>` が実行時に借用規則の違反を処理する方法です。

ここで行ったように、コンパイル時ではなく実行時に借用エラーをキャッチすることを選ぶと、開発プロセスの後半でコードの間違いを見つける可能性があります。おそらく、コードが本番環境にデプロイされるまでになるかもしれません。また、実行時に借用を追跡する代わりにコンパイル時に追跡することで、コードにはわずかな実行時のパフォーマンスペナルティがかかります。ただし、`RefCell<T>` を使用することで、不変値のみが許可されるコンテキストで使用している間、自身を変更して見たメッセージを追跡できるモックオブジェクトを書くことができます。通常の参照が提供する機能よりも多くの機能を得るために、トレードオフがあるにもかかわらず、`RefCell<T>` を使用することができます。
