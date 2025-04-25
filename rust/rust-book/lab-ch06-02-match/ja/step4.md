# マッチは網羅的である

`match` について議論する必要があるもう一つの点があります。アームのパターンはすべての可能性を網羅しなければなりません。`plus_one` 関数のこのバージョンを見てみましょう。これにはバグがあり、コンパイルされません。

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

`None` のケースを処理していないので、このコードはバグを引き起こします。幸いなことに、これは Rust がキャッチする方法を知っているバグです。このコードをコンパイルしようとすると、このエラーが表示されます。

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust は、私たちがすべての可能なケースを網羅していないことを知っており、忘れたパターンさえ知っています！Rust のマッチは網羅的です。コードが有効になるためには、最後の可能性まですべて網羅しなければなりません。特に `Option<T>` の場合、Rust が明示的に `None` のケースを処理することを忘れないように防いでくれるので、値が null の場合に値があると仮定することから免れ、前述の 10 億ドルのミスを引き起こすことができなくなります。
