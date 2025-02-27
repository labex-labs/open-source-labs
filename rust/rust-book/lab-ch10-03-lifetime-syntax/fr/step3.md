# The Borrow Checker

Le compilateur Rust a un _vérificateur d'emprunt_ qui compare les portées pour déterminer si tous les emprunts sont valides. La Liste 10-17 montre le même code que la Liste 10-16 mais avec des annotations montrant les durées de vie des variables.

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

Liste 10-17: Annotations des durées de vie de `r` et `x`, nommées `'a` et `'b` respectivement

Ici, nous avons annoté la durée de vie de `r` avec `'a` et la durée de vie de `x` avec `'b`. Comme vous pouvez le voir, le bloc interne `'b` est beaucoup plus petit que le bloc de durée de vie externe `'a`. À la compilation, Rust compare la taille des deux durées de vie et constate que `r` a une durée de vie de `'a` mais qu'il fait référence à une mémoire avec une durée de vie de `'b`. Le programme est rejeté car `'b` est plus courte que `'a` : l'objet de la référence ne vit pas aussi longtemps que la référence.

La Liste 10-18 corrige le code pour qu'il n'ait pas de référence fausse et qu'il compile sans erreur.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Liste 10-18: Une référence valide car les données ont une durée de vie plus longue que la référence

Ici, `x` a la durée de vie `'b`, qui dans ce cas est plus grande que `'a`. Cela signifie que `r` peut faire référence à `x` car Rust sait que la référence dans `r` sera toujours valide tant que `x` est valide.

Maintenant que vous savez où sont les durées de vie des références et comment Rust analyse les durées de vie pour vous pouvez être certain que les références seront toujours valides, explorons les durées de vie génériques des paramètres et des valeurs de retour dans le contexte des fonctions.
