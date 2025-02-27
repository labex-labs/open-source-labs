# Contraintes de Trait Plus Claires avec les Clauses where

Utiliser trop de contraintes de trait a ses inconvénients. Chaque type générique a ses propres contraintes de trait, donc les fonctions avec plusieurs paramètres de type générique peuvent contenir beaucoup d'informations sur les contraintes de trait entre le nom de la fonction et sa liste de paramètres, rendant la signature de la fonction difficile à lire. Pour cette raison, Rust a une syntaxe alternative pour spécifier les contraintes de trait dans une clause `where` après la signature de la fonction. Ainsi, au lieu d'écrire ceci :

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
```

nous pouvons utiliser une clause `where`, comme ceci :

```rust
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
```

La signature de cette fonction est moins encombrée : le nom de la fonction, la liste de paramètres et le type de retour sont proches les uns des autres, similaire à une fonction sans beaucoup de contraintes de trait.
