# Traits

Bien sûr, les `trait`s peuvent également être génériques. Ici, nous définissons l'un qui réimplémente le `trait` `Drop` en tant que méthode générique pour se `détruire` lui-même et une entrée.

```rust
// Types non copiables.
struct Empty;
struct Null;

// Un trait générique sur `T`.
trait DoubleDrop<T> {
    // Définissez une méthode sur le type appelant qui prend un
    // paramètre unique supplémentaire `T` et ne fait rien avec lui.
    fn double_drop(self, _: T);
}

// Implémentez `DoubleDrop<T>` pour tout paramètre générique `T` et
// appelant `U`.
impl<T, U> DoubleDrop<T> for U {
    // Cette méthode prend la propriété des deux arguments passés,
    // les désallocant tous les deux.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // Désalloue `empty` et `null`.
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: Essayez de décommenter ces lignes.
}
```
