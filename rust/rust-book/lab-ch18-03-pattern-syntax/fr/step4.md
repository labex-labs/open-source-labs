# Plusieurs motifs

Dans les expressions `match`, vous pouvez correspondre plusieurs motifs en utilisant la syntaxe `|`, qui est l'opérateur _ou_ de motif. Par exemple, dans le code suivant, nous correspondons la valeur de `x` aux branches `match`, dont la première a une option _ou_, ce qui signifie que si la valeur de `x` correspond à l'une des valeurs de cette branche, le code de cette branche sera exécuté :

Nom de fichier : `src/main.rs`

```rust
let x = 1;

match x {
    1 | 2 => println!("one or two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

Ce code affiche `one or two`.
