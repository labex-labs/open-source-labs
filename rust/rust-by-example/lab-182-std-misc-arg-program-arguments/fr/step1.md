# Arguments du programme

## Bibliothèque standard

Les arguments de ligne de commande peuvent être accédés en utilisant `std::env::args`, qui renvoie un itérateur qui produit une `String` pour chaque argument :

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // Le premier argument est le chemin utilisé pour appeler le programme.
    println!("Mon chemin est {}.", args[0]);

    // Le reste des arguments sont les paramètres de ligne de commande passés.
    // Appelez le programme comme ceci :
    //   $./args arg1 arg2
    println!("J'ai reçu {:?} arguments : {:?}.", args.len() - 1, &args[1..]);
}
```

```shell
$./args 1 2 3
Mon chemin est./args.
J'ai reçu 3 arguments : ["1", "2", "3"].
```

## Crânes

Alternativement, il existe de nombreux crânes qui peuvent fournir des fonctionnalités supplémentaires lors de la création d'applications de ligne de commande. Le [Rust Cookbook] présente les meilleures pratiques sur la façon d'utiliser l'un des crânes d'arguments de ligne de commande les plus populaires, `clap`.
