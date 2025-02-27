# Using External Packages

Dans le Chapitre 2, nous avons programmé un projet de jeu de devinette qui utilisait un package externe appelé `rand` pour obtenir des nombres aléatoires. Pour utiliser `rand` dans notre projet, nous avons ajouté cette ligne à `Cargo.toml` :

Nom de fichier : `Cargo.toml`

```tomltoml
rand = "0.8.5"
```

Ajouter `rand` comme dépendance dans `Cargo.toml` indique à Cargo de télécharger le package `rand` et toutes ses dépendances depuis *https://crates.io*, et de rendre `rand` disponible pour notre projet.

Ensuite, pour amener les définitions de `rand` dans la portée de notre package, nous avons ajouté une ligne `use` commençant par le nom de la crate, `rand`, et avons listé les éléments que nous voulions amener dans la portée. Rappelez-vous que dans "Generating a Random Number", nous avons amené la trait `Rng` dans la portée et avons appelé la fonction `rand::thread_rng` :

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Les membres de la communauté Rust ont mis à disposition de nombreux packages sur *https://crates.io*, et inclure l'un d'entre eux dans votre package implique les mêmes étapes : les lister dans le fichier `Cargo.toml` de votre package et utiliser `use` pour amener des éléments de leurs crates dans la portée.

Notez que la bibliothèque standard `std` est également une crate externe à notre package. Étant donné que la bibliothèque standard est distribuée avec le langage Rust, nous n'avons pas besoin de modifier `Cargo.toml` pour inclure `std`. Mais nous devons la référencer avec `use` pour amener des éléments de là dans la portée de notre package. Par exemple, avec `HashMap` nous utiliserions cette ligne :

```rust
use std::collections::HashMap;
```

Il s'agit d'un chemin absolu commençant par `std`, le nom de la crate de la bibliothèque standard.
