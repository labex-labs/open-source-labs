# Un exemple de programme utilisant des structs

Pour comprendre dans quels cas nous pourrions vouloir utiliser des structs, écrivons un programme qui calcule l'aire d'un rectangle. Nous commencerons par utiliser des variables individuelles, puis refactoriser le programme jusqu'à ce que nous utilisions des structs à la place.

Créons un nouveau projet binaire Cargo appelé _rectangles_ qui prendra la largeur et la hauteur d'un rectangle spécifiées en pixels et calculera l'aire du rectangle. La liste 5-8 montre un programme court qui fait exactement cela d'une manière dans le `src/main.rs` de notre projet.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "L'aire du rectangle est {} pixels carrés.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
```

Liste 5-8 : Calcul de l'aire d'un rectangle spécifié par des variables de largeur et de hauteur séparées

Maintenant, exécutez ce programme avec `cargo run` :

```rust
L'aire du rectangle est 1500 pixels carrés.
```

Ce code réussit à calculer l'aire du rectangle en appelant la fonction `area` avec chaque dimension, mais nous pouvons faire plus pour rendre ce code clair et lisible.

Le problème de ce code est évident dans la signature de `area` :

```rust
fn area(width: u32, height: u32) -> u32 {
```

La fonction `area` est censée calculer l'aire d'un rectangle, mais la fonction que nous avons écrite a deux paramètres, et il n'est pas clair nulle part dans notre programme que les paramètres sont liés. Il serait plus lisible et plus facile à gérer de regrouper la largeur et la hauteur. Nous avons déjà discuté d'une manière dont nous pourrions le faire dans "Le type tuple" : en utilisant des tuples.
