# Clauses `where`

Une contrainte peut également être exprimée en utilisant une clause `where` immédiatement avant l'ouverture `{`, plutôt qu'au premier usage du type. De plus, les clauses `where` peuvent appliquer des contraintes à des types arbitraires, plutôt qu'à seulement des paramètres de type.

Certains cas où une clause `where` est utile :

- Lorsque la spécification séparée des types génériques et des contraintes est plus claire :

```rust
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// Expression des contraintes avec une clause `where`
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

- Lorsque l'utilisation d'une clause `where` est plus expressive que l'utilisation de la syntaxe normale. L'`impl` dans cet exemple ne peut pas être directement exprimé sans une clause `where` :

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// Car sinon, nous devrions l'exprimer comme `T: Debug` ou
// utiliser une autre méthode d'approche indirecte, ce qui nécessite une clause `where` :
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // Nous voulons `Option<T>: Debug` comme contrainte car c'est ce qui est
    // affiché. Faire autrement serait utiliser la mauvaise contrainte.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```
