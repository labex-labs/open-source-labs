# Documentation

Utilisez `cargo doc` pour générer la documentation dans `target/doc`.

Utilisez `cargo test` pour exécuter tous les tests (y compris les tests de documentation), et `cargo test --doc` pour n'exécuter que les tests de documentation.

Ces commandes invoqueront `rustdoc` (et `rustc`) de manière appropriée selon les besoins.

## Commentaires de documentation

Les commentaires de documentation sont très utiles pour les grands projets qui nécessitent de la documentation. Lors de l'exécution de `rustdoc`, ce sont ces commentaires qui sont compilés en documentation. Ils sont dénotés par un `///` et prennent en charge \[Markdown\].

````rust
#![crate_name = "doc"]

/// Un être humain est représenté ici
pub struct Person {
    /// Une personne doit avoir un nom, peu importe combien Juliette peut le détester
    name: String,
}

impl Person {
    /// Retourne une personne avec le nom qui lui est donné
    ///
    /// # Arguments
    ///
    /// * `name` - Un slice de chaîne de caractères qui contient le nom de la personne
    ///
    /// # Exemples
    ///
    /// ```
    /// // Vous pouvez avoir du code Rust entre les barrières à l'intérieur des commentaires
    /// // Si vous passez --test à `rustdoc`, il vous testera même ça!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// Donne un bonjour amical!
    ///
    /// Dit "Bonjour, [nom](Person::name)" à la `Person` sur laquelle elle est appelée.
    pub fn hello(& self) {
        println!("Bonjour, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

Pour exécuter les tests, construisez d'abord le code en tant que bibliothèque, puis indiquez à `rustdoc` où trouver la bibliothèque afin qu'il puisse la lier dans chaque programme de test de documentation :

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## Attributs de documentation

Voici quelques exemples des attributs `#[doc]` les plus courants utilisés avec `rustdoc`.

## `inline`

Utilisé pour intégrer les docs au lieu de les lier vers une page séparée.

```rust
#[doc(inline)]
pub use bar::Bar;

/// docs de bar
mod bar {
    /// les docs pour Bar
    pub struct Bar;
}
```

## `no_inline`

Utilisé pour empêcher le lien vers une page séparée ou n'importe où.

```rust
// Exemple de libcore/prelude
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

En utilisant cela, on indique à `rustdoc` de ne pas inclure cela dans la documentation :

```rust
// Exemple de la bibliothèque futures-rs
#[doc(hidden)]
pub use self::async_await::*;
```

Pour la documentation, `rustdoc` est largement utilisé par la communauté. C'est ce qui est utilisé pour générer les [docs de la bibliothèque standard](https://doc.rust-lang.org/std/).
