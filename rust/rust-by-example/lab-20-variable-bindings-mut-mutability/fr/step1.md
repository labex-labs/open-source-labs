# Mutabilité

Les liaisons de variables sont immuables par défaut, mais cela peut être contourné à l'aide du modificateur `mut`.

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Avant la mutation: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("Après la mutation: {}", mutable_binding);

    // Erreur! Impossible d'affecter une nouvelle valeur à une variable immutable
    _immutable_binding += 1;
}
```

Le compilateur lancera un diagnostic détaillé sur les erreurs de mutabilité.
