# Accès invalide à un élément de tableau

Voyons ce qui se passe si vous essayez d'accéder à un élément d'un tableau qui est au-delà de la fin du tableau. Disons que vous exécutez ce code, similaire au jeu de devinette du chapitre 2, pour obtenir un index de tableau à partir de l'utilisateur :

Nom de fichier : `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Veuillez entrer un index de tableau.");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("Échec de lecture de la ligne");

    let index: usize = index
     .trim()
     .parse()
     .expect("L'index entré n'était pas un nombre");

    let element = a[index];

    println!(
        "La valeur de l'élément à l'index {index} est : {element}"
    );
}
```

Ce code se compile avec succès. Si vous exécutez ce code en utilisant `cargo run` et que vous entrez `0`, `1`, `2`, `3` ou `4`, le programme affichera la valeur correspondante à cet index dans le tableau. Si vous entrez au lieu de cela un nombre au-delà de la fin du tableau, tel que `10`, vous verrez une sortie comme celle-ci :

    thread'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Le programme a entraîné une erreur _au moment de l'exécution_ au niveau de l'utilisation d'une valeur invalide dans l'opération d'indexation. Le programme est sorti avec un message d'erreur et n'a pas exécuté l'instruction `println!` finale. Lorsque vous essayez d'accéder à un élément en utilisant l'indexation, Rust vérifiera que l'index que vous avez spécifié est inférieur à la longueur du tableau. Si l'index est supérieur ou égal à la longueur, Rust générera une panique. Ce contrôle doit se produire au moment de l'exécution, surtout dans ce cas, car le compilateur ne peut pas savoir quelle valeur un utilisateur entrera lorsqu'il exécutera le code plus tard.

C'est un exemple des principes de sécurité mémoire de Rust en action. Dans de nombreux langages de bas niveau, ce genre de contrôle n'est pas effectué, et lorsque vous fournissez un index incorrect, une mémoire invalide peut être accédée. Rust vous protège contre ce genre d'erreur en sortant immédiatement au lieu de permettre l'accès mémoire et de continuer. Le chapitre 9 traite davantage de la gestion d'erreurs de Rust et de la manière dont vous pouvez écrire un code lisible et sécurisé qui ne génère ni panique ni accès mémoire invalide.
