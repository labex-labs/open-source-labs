# Creating a Constructor for Config

Jusqu'à présent, nous avons extrait la logique responsable de l'analyse des arguments de ligne de commande de `main` et l'avons placée dans la fonction `parse_config`. Cela nous a aidé à voir que les valeurs `query` et `file_path` étaient liées, et cette relation devrait être exprimée dans notre code. Nous avons ensuite ajouté une structure `Config` pour nommer le but commun de `query` et `file_path` et pour pouvoir renvoyer les noms des valeurs comme noms de champs de structure à partir de la fonction `parse_config`.

Maintenant que le but de la fonction `parse_config` est de créer une instance de `Config`, nous pouvons transformer `parse_config` d'une fonction simple en une fonction nommée `new` associée à la structure `Config`. Apporter ce changement rendra le code plus idiomatique. Nous pouvons créer des instances de types de la bibliothèque standard, tels que `String`, en appelant `String::new`. De même, en transformant `parse_config` en une fonction `new` associée à `Config`, nous pourrons créer des instances de `Config` en appelant `Config::new`. Le Listing 12-7 montre les modifications que nous devons apporter.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Listing 12-7 : Transformation de `parse_config` en `Config::new`

Nous avons mis à jour `main` où nous appelions `parse_config` pour appeler `Config::new` à la place \[1\]. Nous avons changé le nom de `parse_config` en `new` \[3\] et l'avons déplacé à l'intérieur d'un bloc `impl` \[2\], qui associe la fonction `new` à `Config`. Essayez de compiler à nouveau ce code pour vous assurer qu'il fonctionne.
