# Opérations numériques

Rust prend en charge les opérations mathématiques de base que vous attendriez pour tous les types de nombres : addition, soustraction, multiplication, division et reste. La division entière tronque vers zéro jusqu'au plus proche entier. Le code suivant montre comment utiliser chaque opération numérique dans une instruction `let` :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    // addition
    let sum = 5 + 10;

    // soustraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // Résulte en -1

    // reste
    let remainder = 43 % 5;
}
```

Chaque expression dans ces instructions utilise un opérateur mathématique et évalue à une seule valeur, qui est ensuite liée à une variable. L'annexe B contient une liste de tous les opérateurs que Rust fournit.
