# Correspondance avec des littéraux

Comme vous l'avez vu au chapitre 6, vous pouvez correspondre des motifs avec des littéraux directement. Le code suivant donne quelques exemples :

Nom de fichier : `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

Ce code affiche `one` car la valeur de `x` est `1`. Cette syntaxe est utile lorsque vous voulez que votre code prenne une action si elle reçoit une valeur concrète particulière.
