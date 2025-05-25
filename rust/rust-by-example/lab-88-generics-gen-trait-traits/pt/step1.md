# Traits

É claro que os `traits` também podem ser genéricos. Aqui, definimos um que reimplementa o `trait` `Drop` como um método genérico para `drop`ar a si próprio e uma entrada.

```rust
// Tipos não copiáveis.
struct Empty;
struct Null;

// Um trait genérico sobre `T`.
trait DoubleDrop<T> {
    // Defina um método no tipo chamador que recebe um
    // parâmetro único adicional `T` e não faz nada com ele.
    fn double_drop(self, _: T);
}

// Implemente `DoubleDrop<T>` para qualquer parâmetro genérico `T` e
// chamador `U`.
impl<T, U> DoubleDrop<T> for U {
    // Este método assume a propriedade de ambos os argumentos passados,
    // desalocando ambos.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // Desalocar `empty` e `null`.
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: Tente descomentar estas linhas.
}
```
