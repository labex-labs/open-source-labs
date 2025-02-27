# Les tranches de chaîne comme paramètres

Savoir que l'on peut prendre des tranches de littéraux et de valeurs `String` nous conduit à une autre amélioration de `first_word`, et c'est sa signature :

```rust
fn first_word(s: &String) -> &str {
```

Un Rustacean plus expérimenté écrirait plutôt la signature montrée dans la Liste 4-9 car cela nous permet d'utiliser la même fonction sur des valeurs `&String` et des valeurs `&str`.

```rust
fn first_word(s: &str) -> &str {
```

Liste 4-9 : Amélioration de la fonction `first_word` en utilisant une tranche de chaîne pour le type du paramètre `s`

Si nous avons une tranche de chaîne, nous pouvons la passer directement. Si nous avons une `String`, nous pouvons passer une tranche de la `String` ou une référence à la `String`. Cette flexibilité profite des _coercitions de déréférencement_, une fonctionnalité que nous aborderons dans "Les coercitions de déréférencement implicites avec les fonctions et les méthodes".

Définir une fonction pour prendre une tranche de chaîne plutôt qu'une référence à une `String` rend notre API plus générale et utile sans perdre aucune fonctionnalité :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` fonctionne sur des tranches de `String`, que ce soit
    // partielle ou complète
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` fonctionne également sur des références à des `String`, qui
    // sont équivalentes à des tranches complètes de `String`
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` fonctionne sur des tranches de littéraux de chaîne,
    // que ce soit partielle ou complète
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Parce que les littéraux de chaîne *sont* déjà des tranches de chaîne,
    // cela fonctionne également, sans la syntaxe de tranche!
    let word = first_word(my_string_literal);
}
```
