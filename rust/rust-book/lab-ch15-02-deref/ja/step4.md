# 独自のスマートポインタを定義する

標準ライブラリに提供されている`Box<T>`型に似たスマートポインタを作成して、デフォルトではスマートポインタが参照とどのように異なる動作をするかを体験しましょう。そして、参照演算子を使用できる機能を追加する方法を見てみましょう。

`Box<T>`型は最終的には 1 つの要素を持つタプル構造体として定義されているので、リスト 15-8 では同じように`MyBox<T>`型を定義します。また、`Box<T>`に定義されている`new`関数に合わせて`new`関数も定義します。

ファイル名：`src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

リスト 15-8: `MyBox<T>`型を定義する

`MyBox`という構造体を定義し、ジェネリックパラメータ`T`を宣言します\[1\]。なぜなら、任意の型の値を保持するようにしたいからです。`MyBox`型は型`T`の 1 つの要素を持つタプル構造体です。`MyBox::new`関数は型`T`の 1 つのパラメータを受け取り\[2\]、渡された値を保持する`MyBox`インスタンスを返します\[3\]。

リスト 15-7 の`main`関数をリスト 15-8 に追加し、`Box<T>`の代わりに定義した`MyBox<T>`型を使うように変更してみましょう。リスト 15-9 のコードはコンパイルされません。なぜなら、Rust は`MyBox`を参照解除する方法を知らないからです。

ファイル名：`src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

リスト 15-9: 参照と`Box<T>`を使った方法と同じように`MyBox<T>`を使用しようとする

結果として得られるコンパイルエラーは次の通りです。

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

`MyBox<T>`型は参照解除できません。なぜなら、その型にその機能を実装していないからです。`*`演算子で参照解除を可能にするには、`Deref`トレイトを実装します。
