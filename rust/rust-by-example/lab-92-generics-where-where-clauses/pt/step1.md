# Cláusulas where

Um limite também pode ser expresso usando uma cláusula `where` imediatamente antes da abertura `{`, em vez de na primeira menção do tipo. Além disso, as cláusulas `where` podem aplicar limites a tipos arbitrários, e não apenas a parâmetros de tipo.

Alguns casos em que uma cláusula `where` é útil:

- Quando especificar tipos genéricos e limites separadamente é mais claro:

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// Expressando limites com uma cláusula `where`
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- Quando usar uma cláusula `where` é mais expressivo do que usar a sintaxe normal. O `impl` neste exemplo não pode ser expresso diretamente sem uma cláusula `where`:

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// Como, caso contrário, teríamos que expressar isso como `T: Debug` ou
// usar outro método de abordagem indireta, isso requer uma cláusula `where`:
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // Queremos `Option<T>: Debug` como nosso limite porque é isso que está sendo impresso. Fazer o contrário seria usar o limite errado.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
