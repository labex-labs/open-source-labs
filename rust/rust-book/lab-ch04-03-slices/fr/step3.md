# Les littéraux de chaîne comme tranches

Rappelez-vous que nous avons parlé des littéraux de chaîne étant stockés dans le binaire. Maintenant que nous connaissons les tranches, nous pouvons correctement comprendre les littéraux de chaîne :

```rust
let s = "Hello, world!";
```

Le type de `s` ici est `&str` : c'est une tranche pointant vers ce point spécifique du binaire. C'est également pourquoi les littéraux de chaîne sont immuables ; `&str` est une référence immutable.
