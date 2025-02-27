# Devolviendo cierres

Los cierres se representan por tratados, lo que significa que no se pueden devolver cierres directamente. En la mayoría de los casos en los que puedas querer devolver un trato, en cambio, puedes usar el tipo concrete que implementa el trato como valor de retorno de la función. Sin embargo, no se puede hacer eso con los cierres porque no tienen un tipo concreto que sea devuelvable; por ejemplo, no se permite usar el puntero a función `fn` como tipo de retorno.

El siguiente código intenta devolver un cierre directamente, pero no se compilará:

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

El error del compilador es el siguiente:

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

¡El error vuelve a referirse al trato `Sized`! Rust no sabe cuánto espacio necesitará para almacenar el cierre. Vimos una solución a este problema anteriormente. Podemos usar un objeto de trato:

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

Este código se compilará sin problemas. Para más información sobre los objetos de trato, consulte "Usando objetos de trato que permiten valores de diferentes tipos".

A continuación, echemos un vistazo a los macros.
