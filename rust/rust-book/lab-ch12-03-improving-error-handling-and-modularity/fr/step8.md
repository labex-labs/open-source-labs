# Returning a Result Instead of Calling panic!

Au lieu de cela, nous pouvons renvoyer une valeur `Result` qui contiendra une instance de `Config` dans le cas de réussite et qui décrira le problème dans le cas d'erreur. Nous allons également changer le nom de la fonction de `new` à `build` car de nombreux programmeurs s'attendent à ce que les fonctions `new` ne rencontrent jamais d'erreur. Lorsque `Config::build` communique avec `main`, nous pouvons utiliser le type `Result` pour signaler qu'il y a eu un problème. Ensuite, nous pouvons modifier `main` pour convertir une variante `Err` en une erreur plus pratique pour nos utilisateurs sans le texte environnant concernant `thread'main'` et `RUST_BACKTRACE` que provoque un appel à `panic!`.

Le Listing 12-9 montre les modifications que nous devons apporter à la valeur de retour de la fonction que nous appelons désormais `Config::build` et au corps de la fonction nécessaire pour renvoyer un `Result`. Notez que cela ne compilera pas jusqu'à ce que nous ayons également mis à jour `main`, ce que nous ferons dans le prochain listing.

Nom du fichier : `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

Listing 12-9 : Retour d'un `Result` depuis `Config::build`

Notre fonction `build` renvoie un `Result` avec une instance de `Config` dans le cas de réussite et une `&'static str` dans le cas d'erreur. Nos valeurs d'erreur seront toujours des littéraux de chaîne qui ont la durée de vie `'static`.

Nous avons apporté deux modifications dans le corps de la fonction : au lieu d'appeler `panic!` lorsque l'utilisateur ne passe pas assez d'arguments, nous renvoyons maintenant une valeur `Err`, et nous avons enveloppé la valeur de retour `Config` dans un `Ok`. Ces modifications rendent la fonction conforme à sa nouvelle signature de type.

Le retour d'une valeur `Err` depuis `Config::build` permet à la fonction `main` de gérer la valeur `Result` renvoyée par la fonction `build` et de quitter le processus de manière plus propre dans le cas d'erreur.
