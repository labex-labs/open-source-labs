# Binding

Accéder indirectement à une variable rend impossible de créer des branches et d'utiliser cette variable sans la relier. `match` fournit le sigle `@` pour lier des valeurs à des noms :

```rust
// Une fonction `age` qui renvoie un `u32`.
fn age() -> u32 {
    15
}

fn main() {
    println!("Dites-moi quel type de personne vous êtes");

    match age() {
        0             => println!("Je n'ai pas encore fêté mon premier anniversaire"),
        // On pourrait directement `match` 1..= 12, mais alors quel âge
        // aurait l'enfant? Au lieu de cela, liez à `n` pour la
        // séquence de 1..= 12. Maintenant, l'âge peut être rapporté.
        n @ 1 ..= 12 => println!("Je suis un enfant de {:?} ans", n),
        n @ 13..= 19 => println!("Je suis un ado de {:?} ans", n),
        // Rien n'est lié. Retournez le résultat.
        n             => println!("Je suis une personne âgée de {:?} ans", n),
    }
}
```

Vous pouvez également utiliser la liaison pour "déstructurer" des variantes `enum`, telles que `Option` :

```rust
fn some_number() -> Option<u32> {
    Some(42)
}

fn main() {
    match some_number() {
        // On a obtenu la variante `Some`, vérifiez si sa valeur, liée à `n`,
        // est égale à 42.
        Some(n @ 42) => println!("La réponse : {}!", n),
        // Vérifiez tout autre nombre.
        Some(n)      => println!("Pas intéressant... {}", n),
        // Vérifiez tout autre chose (`None` variant).
        _            => (),
    }
}
```
