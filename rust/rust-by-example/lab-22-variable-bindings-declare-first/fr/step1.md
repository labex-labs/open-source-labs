# Déclarer d'abord

Il est possible de déclarer des liaisons de variables d'abord, puis de les initialiser plus tard. Cependant, cette forme est rarement utilisée, car elle peut entraîner l'utilisation de variables non initialisées.

```rust
fn main() {
    // Déclare une liaison de variable
    let a_binding;

    {
        let x = 2;

        // Initialise la liaison
        a_binding = x * x;
    }

    println!("une liaison : {}", a_binding);

    let another_binding;

    // Erreur! Utilisation d'une liaison non initialisée
    println!("une autre liaison : {}", another_binding);
    // FIXME ^ Commenter cette ligne

    another_binding = 1;

    println!("une autre liaison : {}", another_binding);
}
```

Le compilateur interdit l'utilisation de variables non initialisées, car cela entraînerait un comportement indéfini.
