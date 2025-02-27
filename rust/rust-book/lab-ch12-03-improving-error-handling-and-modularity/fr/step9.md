# Calling Config::build and Handling Errors

Pour gérer le cas d'erreur et afficher un message convivial pour l'utilisateur, nous devons mettre à jour `main` pour gérer le `Result` renvoyé par `Config::build`, comme montré dans le Listing 12-10. Nous prendrons également la responsabilité de quitter l'outil de ligne de commande avec un code d'erreur non nul, loin de `panic!`, et nous le mettrons en œuvre manuellement. Un statut de sortie non nul est une convention pour signaler au processus qui a appelé notre programme que le programme est sorti avec un état d'erreur.

Nom du fichier : `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

Listing 12-10 : Sortie avec un code d'erreur si la construction d'un `Config` échoue

Dans ce listing, nous avons utilisé une méthode que nous n'avons pas encore couverte en détail : `unwrap_or_else`, qui est définie sur `Result<T, E>` par la bibliothèque standard \[2\]. L'utilisation de `unwrap_or_else` nous permet de définir un certain traitement d'erreur personnalisé, non basé sur `panic!`. Si le `Result` est une valeur `Ok`, le comportement de cette méthode est similaire à `unwrap` : elle renvoie la valeur interne que `Ok` enveloppe. Cependant, si la valeur est une valeur `Err`, cette méthode appelle le code dans la _fermeture_, qui est une fonction anonyme que nous définissons et passons en tant qu'argument à `unwrap_or_else` \[3\]. Nous aborderons les fermetures en détail au chapitre 13. Pour l'instant, vous n'avez qu'à savoir que `unwrap_or_else` passera la valeur interne de l'`Err`, qui dans ce cas est la chaîne statique `"not enough arguments"` que nous avons ajoutée dans le Listing 12-9, à notre fermeture dans l'argument `err` qui apparaît entre les pipes verticales \[4\]. Le code dans la fermeture peut ensuite utiliser la valeur `err` lorsqu'il s'exécute.

Nous avons ajouté une nouvelle ligne `use` pour amener `process` de la bibliothèque standard dans la portée \[1\]. Le code dans la fermeture qui sera exécuté dans le cas d'erreur ne comporte que deux lignes : nous affichons la valeur `err` \[5\] puis appelons `process::exit` \[6\]. La fonction `process::exit` arrêtera immédiatement le programme et renverra le nombre qui a été passé comme code de statut de sortie. Cela est similaire au traitement basé sur `panic!` que nous avons utilisé dans le Listing 12-8, mais nous n'obtenons plus tout le surplus de sortie. Essayons :

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

Parfait! Cette sortie est bien plus conviviale pour nos utilisateurs.
