# Extracting the Argument Parser

Nous allons extraire la fonctionnalité d'analyse des arguments dans une fonction que `main` appellera pour préparer le déplacement de la logique d'analyse des arguments de ligne de commande vers `src/lib.rs`. Le Listing 12-5 montre le nouveau début de `main` qui appelle une nouvelle fonction `parse_config`, que nous définirons pour le moment dans `src/main.rs`.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

Listing 12-5 : Extraction d'une fonction `parse_config` à partir de `main`

Nous continuons à collecter les arguments de ligne de commande dans un vecteur, mais au lieu d'affecter la valeur de l'argument à l'index 1 à la variable `query` et la valeur de l'argument à l'index 2 à la variable `file_path` dans la fonction `main`, nous passons le vecteur entier à la fonction `parse_config`. La fonction `parse_config` contient ensuite la logique qui détermine quel argument doit être affecté à quelle variable et renvoie les valeurs à `main`. Nous créons toujours les variables `query` et `file_path` dans `main`, mais `main` n'a plus la responsabilité de déterminer comment les arguments de ligne de commande et les variables correspondent.

Ce réaménagement peut sembler superflu pour notre petit programme, mais nous refactorisons par petites étapes incrémentales. Après avoir effectué ce changement, exécutez le programme à nouveau pour vérifier que l'analyse des arguments fonctionne toujours. Il est bon de vérifier régulièrement votre progression pour aider à identifier la cause des problèmes lorsqu'ils se produisent.
