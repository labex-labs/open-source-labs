# Cláusulas where

Un límite también se puede expresar utilizando una cláusula `where` inmediatamente antes de la llave de apertura `{`, en lugar de en la primera mención del tipo. Además, las cláusulas `where` pueden aplicar límites a tipos arbitrarios, en lugar de solo a parámetros de tipo.

Algunos casos en los que una cláusula `where` es útil:

- Cuando especificar tipos genéricos y límites por separado es más claro:

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// Expresando límites con una cláusula `where`
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- Cuando utilizar una cláusula `where` es más expresiva que utilizar la sintaxis normal. El `impl` en este ejemplo no se puede expresar directamente sin una cláusula `where`:

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// Debido a que de lo contrario tendríamos que expresarlo como `T: Debug` o
// utilizar otro método de enfoque indirecto, esto requiere una cláusula `where`:
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // Queremos `Option<T>: Debug` como nuestro límite porque eso es lo que
    // se está imprimiendo. Hacer lo contrario sería utilizar el límite incorrecto.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
