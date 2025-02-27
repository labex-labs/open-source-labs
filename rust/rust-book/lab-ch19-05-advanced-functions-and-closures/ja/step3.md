# クロージャの返却

クロージャはトレイトによって表されるため、直接クロージャを返すことはできません。トレイトを返したい場合のほとんどのケースでは、代わりにトレイトを実装する具体的な型を関数の返却値として使うことができます。しかし、クロージャの場合はそれができません。なぜなら、返却可能な具体的な型がないからです。例えば、関数ポインタ `fn` を返却型として使うことはできません。

次のコードは、直接クロージャを返そうとしていますが、コンパイルされません。

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

コンパイラのエラーは次の通りです。

```bash
error[E0746]: return type cannot have an unboxed trait object
 --> src/lib.rs:1:25
  |
1 | fn returns_closure() -> dyn Fn(i32) -> i32 {
  |                         ^^^^^^^^^^^^^^^^^^ doesn't have a size known at
compile-time
  |
  = note: for information on `impl Trait`, see
<https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-
implement-traits>
help: use `impl Fn(i32) -> i32` as the return type, as all return paths are of
type `[closure@src/lib.rs:2:5: 2:14]`, which implements `Fn(i32) -> i32`
  |
1 | fn returns_closure() -> impl Fn(i32) -> i32 {
  |                         ~~~~~~~~~~~~~~~~~~~
```

エラーは再び `Sized` トレイトを参照しています！Rustは、クロージャを格納するのにどれだけのスペースが必要かを知りません。この問題の解決策を前に見たことがあります。トレイトオブジェクトを使うことができます。

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

このコードは正常にコンパイルされます。トレイトオブジェクトに関する詳細は、「異なる型の値を許容するトレイトオブジェクトの使用」を参照してください。

次に、マクロを見てみましょう！
