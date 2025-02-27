# Debug

Tous les types qui souhaitent utiliser les `traits` de formatage `std::fmt` nécessitent une implémentation pour être imprimables. Les implémentations automatiques ne sont fournies que pour les types tels que ceux de la bibliothèque `std`. Tous les autres doivent être implémentés manuellement d'une manière ou d'une autre.

Le `trait` `fmt::Debug` en fait très simple. Tous les types peuvent `dériver` (créer automatiquement) l'implémentation de `fmt::Debug`. Ce n'est pas le cas de `fmt::Display` qui doit être implémenté manuellement.

```rust
// Cette structure ne peut pas être imprimée avec `fmt::Display` ni
// avec `fmt::Debug`.
struct UnPrintable(i32);

// L'attribut `derive` crée automatiquement l'implémentation
// nécessaire pour rendre cette `struct` imprimable avec `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);
```

Tous les types de la bibliothèque `std` sont automatiquement imprimables avec `{:?}` également :

```rust
// Dérive l'implémentation de `fmt::Debug` pour `Structure`. `Structure`
// est une structure qui contient un seul `i32`.
#[derive(Debug)]
struct Structure(i32);

// Place une `Structure` à l'intérieur de la structure `Deep`. Rendez-la
// également imprimable.
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // L'impression avec `{:?}` est similaire à celle avec `{}`.
    println!("{:?} mois dans une année.", 12);
    println!("{1:?} {0:?} est le {actor:?} nom.",
             "Slater",
             "Christian",
             actor="nom de l'");

    // `Structure` est imprimable!
    println!("Maintenant {:?} va s'imprimer!", Structure(3));

    // Le problème avec `derive` est qu'il n'y a pas de contrôle sur la
    // façon dont les résultats apparaissent. Que faire si je veux que cela
    // n'affiche que un `7`?
    println!("Maintenant {:?} va s'imprimer!", Deep(Structure(7)));
}
```

Donc `fmt::Debug` rend certainement cela imprimable mais sacrifie un peu d'élégance. Rust propose également une "impression jolie" avec `{:#?}`.

```rust
#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

fn main() {
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    // Impression jolie
    println!("{:#?}", peter);
}
```

On peut implémenter manuellement `fmt::Display` pour contrôler l'affichage.
