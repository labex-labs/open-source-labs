# Rückgabe von Closures

Closures werden durch Traits repräsentiert, was bedeutet, dass Sie Closures nicht direkt zurückgeben können. In den meisten Fällen, in denen Sie einen Trait zurückgeben möchten, können Sie stattdessen den konkreten Typ verwenden, der den Trait implementiert, als Rückgabewert der Funktion. Mit Closures können Sie das jedoch nicht tun, da sie keinen konkreten Typ haben, der zurückgegeben werden kann; Sie dürfen beispielsweise nicht den Funktionszeiger `fn` als Rückgabetyp verwenden.

Der folgende Code versucht, einen Closure direkt zurückzugeben, aber er wird nicht kompilieren:

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

Der Compilerfehler lautet wie folgt:

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

Der Fehler verweist erneut auf den `Sized`-Trait! Rust weiß nicht, wie viel Speicher es zum Speichern des Closures benötigen wird. Wir haben eine Lösung für dieses Problem bereits gesehen. Wir können ein Traitobjekt verwenden:

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

Dieser Code wird problemlos kompilieren. Weitere Informationen zu Traitobjekten finden Sie in "Using Trait Objects That Allow for Values of Different Types".

Als nächstes schauen wir uns Makros an!
