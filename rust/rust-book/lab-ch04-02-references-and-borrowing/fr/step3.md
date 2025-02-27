# Références périssantes

Dans les langages avec des pointeurs, il est facile de créer erronément un _pointeur périssant_ --- un pointeur qui référence un emplacement en mémoire qui peut avoir été donné à quelqu'un d'autre --- en libérant une partie de la mémoire tout en conservant un pointeur vers cette mémoire. En revanche, en Rust, le compilateur garantit que les références ne seront jamais des références périssantes : si vous avez une référence à certaines données, le compilateur vous assurera que les données ne sortiront pas de portée avant que la référence aux données ne le fasse.

Essayons de créer une référence périssante pour voir comment Rust les empêche avec une erreur de compilation :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Voici l'erreur :

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

Ce message d'erreur fait référence à une fonctionnalité que nous n'avons pas encore abordée : les durées de vie. Nous aborderons les durées de vie en détail au chapitre 10. Mais, si vous ignorez les parties sur les durées de vie, le message contient bien la clé du problème de ce code :

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

Examillons de plus près ce qui se passe à chaque étape de notre code `dangle` :

    // src/main.rs
    fn dangle() -> &String { // dangle renvoie une référence à une String

        let s = String::from("hello"); // s est une nouvelle String

        &s // nous renvoyons une référence à la String, s
    } // Ici, s sort de portée et est supprimé, donc sa mémoire disparaît
      // Danger!

Comme `s` est créé à l'intérieur de `dangle`, lorsque le code de `dangle` est terminé, `s` sera désalloué. Mais nous avons essayé de renvoyer une référence à elle. Cela signifie que cette référence pointerait vers une `String` invalide. C'est pas bon! Rust ne nous laissera pas faire.

La solution ici est de renvoyer directement la `String` :

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

Cela fonctionne sans problème. La propriété est transférée, et rien n'est désalloué.
