# constantes

Rust a deux types différents de constantes qui peuvent être déclarées dans n'importe quel contexte, y compris le contexte global. Les deux nécessitent une annotation de type explicite :

- `const` : Une valeur inchangeable (le cas le plus courant).
- `static` : Une variable potentiellement `mut`able avec une durée de vie `'static`. La durée de vie statique est déduite et n'a pas besoin d'être spécifiée. Accéder ou modifier une variable statique mutable est `unsafe`.

```rust
// Les variables globales sont déclarées en dehors de tous les autres contextes.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Accéder à une constante dans une fonction
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Accéder à une constante dans le fil principal
    println!("Ceci est {}", LANGUAGE);
    println!("Le seuil est {}", THRESHOLD);
    println!("{} est {}", n, if is_big(n) { "grand" } else { "petit" });

    // Erreur! Impossible de modifier une `const`.
    THRESHOLD = 5;
    // FIXME ^ Commenter cette ligne
}
```
