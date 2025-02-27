# while let

De la même manière que `if let`, `while let` peut rendre les séquences `match` embarrassantes plus supportables. Considérez la séquence suivante qui incrémente `i` :

```rust
// Crée une variable `optional` de type `Option<i32>`
let mut optional = Some(0);

// Répétez le test.
loop {
    match optional {
        // Si `optional` peut être décomposé, évaluez le bloc.
        Some(i) => {
            if i > 9 {
                println!("Plus grand que 9, arrêtez!");
                optional = None;
            } else {
                println!("`i` vaut `{:?}`. Essayez encore.", i);
                optional = Some(i + 1);
            }
            // ^ Requiert 3 indentations!
        },
        // Arrêtez la boucle lorsque la décomposition échoue :
        _ => { break; }
        // ^ Pourquoi est-ce nécessaire? Il doit y avoir une meilleure façon!
    }
}
```

En utilisant `while let`, cette séquence est bien meilleure :

```rust
fn main() {
    // Crée une variable `optional` de type `Option<i32>`
    let mut optional = Some(0);

    // Cela signifie : "tant que `let` décompose `optional` en
    // `Some(i)`, évaluez le bloc (`{}`). Sinon, `break`.
    while let Some(i) = optional {
        if i > 9 {
            println!("Plus grand que 9, arrêtez!");
            optional = None;
        } else {
            println!("`i` vaut `{:?}`. Essayez encore.", i);
            optional = Some(i + 1);
        }
        // ^ Moins d'indentation vers la droite et ne nécessite pas
        // de gérer explicitement le cas d'échec.
    }
    // ^ `if let` avait des clauses `else`/`else if` optionnelles supplémentaires. `while let` n'en a pas.
}
```
