# Le type booléen

Comme dans la plupart des autres langues de programmation, un type booléen en Rust a deux valeurs possibles : `true` et `false`. Les booléens ont une taille d'un octet. Le type booléen en Rust est spécifié en utilisant `bool`. Par exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // avec annotation de type explicite
}
```

La principale manière d'utiliser des valeurs booléennes est à travers des conditionnels, tels qu'une expression `if`. Nous aborderons comment fonctionnent les expressions `if` en Rust dans "Flux de contrôle".
