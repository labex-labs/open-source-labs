# Indexing into Strings

Dans de nombreux autres langages de programmation, accéder à des caractères individuels dans une chaîne de caractères en les référencant par indice est une opération valide et courante. Cependant, si vous essayez d'accéder à des parties d'une `String` en utilisant la syntaxe d'indexation en Rust, vous obtiendrez une erreur. Considérez le code invalide de la Liste 8-19.

```rust
let s1 = String::from("hello");
let h = s1[0];
```

Liste 8-19: Tentative d'utilisation de la syntaxe d'indexation avec une `String`

Ce code entraînera l'erreur suivante :

```bash
error[E0277]: the type `String` cannot be indexed by `{integer}`
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` cannot be indexed by `{integer}`
  |
  = help: the trait `Index<{integer}>` is not implemented for
`String`
```

L'erreur et la note racontent l'histoire : les chaînes de caractères Rust ne prennent pas en charge l'indexation. Mais pourquoi pas? Pour répondre à cette question, nous devons discuter de la manière dont Rust stocke les chaînes de caractères en mémoire.
