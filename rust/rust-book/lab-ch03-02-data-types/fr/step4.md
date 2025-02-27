# Types à virgule flottante

Rust dispose également de deux types primitifs pour les _nombres à virgule flottante_, qui sont des nombres avec des points décimaux. Les types à virgule flottante de Rust sont `f32` et `f64`, qui ont respectivement une taille de 32 bits et 64 bits. Le type par défaut est `f64` car sur les processeurs modernes, sa vitesse est approximativement la même que celle de `f32` mais elle est capable d'une plus grande précision. Tous les types à virgule flottante sont signés.

Créez un nouveau projet appelé `data-types` :

```bash
cargo new data-types
cd data-types
```

Voici un exemple qui montre les nombres à virgule flottante en action :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
}
```

Les nombres à virgule flottante sont représentés conformément à la norme IEEE-754. Le type `f32` est un flottant simple précision, et `f64` a une double précision.
