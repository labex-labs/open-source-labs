# Returning Errors from the run Function

Avec le reste de la logique du programme séparé dans la fonction `run`, nous pouvons améliorer la gestion des erreurs, comme nous l'avons fait avec `Config::build` dans le Listing 12-9. Au lieu de laisser le programme générer une panique en appelant `expect`, la fonction `run` renverra un `Result<T, E>` lorsqu'il y a un problème. Cela nous permettra de consolider davantage la logique autour de la gestion des erreurs dans `main` de manière conviviale pour l'utilisateur. Le Listing 12-12 montre les modifications que nous devons apporter à la signature et au corps de `run`.

Nom du fichier : `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

Listing 12-12 : Changement de la fonction `run` pour renvoyer un `Result`

Nous avons apporté trois modifications importantes ici. Premièrement, nous avons changé le type de retour de la fonction `run` en `Result<(), Box<dyn Error>>` \[2\]. Cette fonction renvoyait précédemment le type unité, `()`, et nous conservons cela comme valeur renvoyée dans le cas `Ok`.

Pour le type d'erreur, nous avons utilisé l'_objet trait_ `Box<dyn Error>` (et nous avons amené `std::error::Error` dans la portée avec une instruction `use` en haut \[1\]). Nous aborderons les objets trait au chapitre 17. Pour l'instant, sachez seulement que `Box<dyn Error>` signifie que la fonction renverra un type qui implémente le trait `Error`, mais nous n'avons pas besoin de spécifier quel type particulier la valeur de retour sera. Cela nous donne la flexibilité de renvoyer des valeurs d'erreur qui peuvent être de différents types dans différents cas d'erreur. Le mot clé `dyn` est l'abréviation de _dynamic_.

Deuxièmement, nous avons supprimé l'appel à `expect` au profit de l'opérateur `?` \[3\], comme nous l'avons discuté au chapitre 9. Au lieu de générer une panique en cas d'erreur, `?` renverra la valeur d'erreur de la fonction actuelle pour que l'appelant la gère.

Troisièmement, la fonction `run` renvoie maintenant une valeur `Ok` dans le cas de réussite \[4\]. Nous avons déclaré le type de réussite de la fonction `run` comme `()` dans la signature, ce qui signifie que nous devons envelopper la valeur de type unité dans la valeur `Ok`. Cette syntaxe `Ok(())` peut sembler un peu étrange au premier abord, mais utiliser `()` de cette manière est la manière habituelle d'indiquer que nous appelons `run` seulement pour ses effets de bord ; elle ne renvoie pas de valeur dont nous ayons besoin.

Lorsque vous exécutez ce code, il compilera mais affichera un avertissement :

    warning: unused `Result` that must be used
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = note: `#[warn(unused_must_use)]` on by default
       = note: this `Result` may be an `Err` variant, which should be
    handled

Rust nous indique que notre code a ignoré la valeur `Result` et que la valeur `Result` peut indiquer qu'une erreur s'est produite. Mais nous ne vérifions pas s'il y a eu une erreur ou non, et le compilateur nous rappelle que nous aurions probablement dû avoir du code de gestion d'erreur ici! Rectifions ce problème maintenant.
