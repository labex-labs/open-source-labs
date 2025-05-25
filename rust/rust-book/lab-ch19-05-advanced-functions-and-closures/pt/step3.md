# Retornando Closures

Closures são representadas por traits, o que significa que você não pode retornar closures diretamente. Na maioria dos casos em que você pode querer retornar um trait, você pode, em vez disso, usar o tipo concreto que implementa o trait como o valor de retorno da função. No entanto, você não pode fazer isso com closures porque elas não têm um tipo concreto que possa ser retornado; você não tem permissão para usar o ponteiro de função `fn` como um tipo de retorno, por exemplo.

O código a seguir tenta retornar uma closure diretamente, mas não compilará:

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

O erro do compilador é o seguinte:

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

O erro faz referência ao trait `Sized` novamente! Rust não sabe quanto espaço precisará para armazenar a closure. Vimos uma solução para esse problema anteriormente. Podemos usar um objeto de trait:

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

Este código compilará perfeitamente. Para saber mais sobre objetos de trait, consulte "Usando Objetos de Trait que Permitem Valores de Diferentes Tipos".

Em seguida, vamos analisar macros!
