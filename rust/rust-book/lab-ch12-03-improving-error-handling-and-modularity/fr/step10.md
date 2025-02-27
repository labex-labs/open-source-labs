# Extracting Logic from main

Maintenant que nous avons fini de refactoriser l'analyse de la configuration, passons à la logique du programme. Comme nous l'avons déclaré dans "Separation of Concerns for Binary Projects", nous allons extraire une fonction nommée `run` qui contiendra toute la logique actuellement dans la fonction `main` qui n'est pas impliquée dans la configuration ou la gestion des erreurs. Lorsque nous aurons fini, `main` sera concise et facile à vérifier par inspection, et nous pourrons écrire des tests pour toute l'autre logique.

Le Listing 12-11 montre la fonction `run` extraite. Pour l'instant, nous ne faisons que l'amélioration progressive modeste d'extraire la fonction. Nous la définissons toujours dans `src/main.rs`.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

Listing 12-11 : Extraction d'une fonction `run` contenant le reste de la logique du programme

La fonction `run` contient désormais toute la logique restante de `main`, à partir de la lecture du fichier. La fonction `run` prend l'instance `Config` en argument.
