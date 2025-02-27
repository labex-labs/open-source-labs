# `where`-Klauseln

Eine Grenze kann auch mithilfe einer `where`-Klausel direkt vor der öffnenden `{` ausgedrückt werden, anstatt beim ersten Erwähnung des Typs. Darüber hinaus können `where`-Klauseln Grenzen auf beliebige Typen anwenden, nicht nur auf Typparameter.

Einige Fälle, in denen eine `where`-Klausel nützlich ist:

- Wenn die separate Angabe von generischen Typen und Grenzen klarer ist:

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// Ausdrücken von Grenzen mit einer `where`-Klausel
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- Wenn das Verwenden einer `where`-Klausel ausdrucksstärker ist als das Verwenden der normalen Syntax. Die `impl` in diesem Beispiel kann ohne eine `where`-Klausel nicht direkt ausgedrückt werden:

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// Da wir andernfalls diese als `T: Debug` ausdrücken müssten oder
// eine andere indirekte Methode verwenden, erfordert dies eine `where`-Klausel:
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // Wir wollen `Option<T>: Debug` als unsere Grenze, weil das, was gedruckt wird. Andernfalls würden wir die falsche Grenze verwenden.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
