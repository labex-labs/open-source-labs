# Saving the Argument Values in Variables

Le programme est actuellement capable d'accéder aux valeurs spécifiées comme arguments de ligne de commande. Maintenant, nous devons enregistrer les valeurs des deux arguments dans des variables pour pouvoir utiliser les valeurs dans le reste du programme. Nous le faisons dans la liste 12-2.

Nom de fichier : `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Liste 12-2 : Création de variables pour stocker l'argument de requête et l'argument de chemin de fichier

Comme nous l'avons vu lorsque nous avons imprimé le vecteur, le nom du programme occupe la première valeur dans le vecteur à `args[0]`, donc nous commençons les arguments à l'index 1. Le premier argument que `minigrep` prend est la chaîne de caractères que nous recherchons, donc nous plaçons une référence au premier argument dans la variable `query`. Le second argument sera le chemin du fichier, donc nous plaçons une référence au second argument dans la variable `file_path`.

Nous imprimons temporairement les valeurs de ces variables pour prouver que le code fonctionne comme prévu. Exécutons à nouveau ce programme avec les arguments `test` et `sample.txt` :

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Parfait, le programme fonctionne! Les valeurs des arguments dont nous avons besoin sont enregistrées dans les bonnes variables. Plus tard, nous ajouterons une gestion des erreurs pour traiter certaines situations potentielles erronées, telles que lorsque l'utilisateur ne fournit aucun argument ; pour l'instant, nous allons ignorer cette situation et travailler sur l'ajout de capacités de lecture de fichiers.
