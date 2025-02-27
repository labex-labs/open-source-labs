# Utiliser des méthodes du trait Itérateur au lieu d'indexation

Ensuite, nous allons corriger le corps de `Config::build`. Puisque `args` implémente le trait `Iterator`, nous savons que nous pouvons appeler la méthode `next` dessus! La liste 13-20 met à jour le code de la liste 12-23 pour utiliser la méthode `next`.

Nom de fichier : `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Liste 13-20 : Changement du corps de `Config::build` pour utiliser des méthodes d'itérateur

Rappelez-vous que la première valeur dans la valeur de retour de `env::args` est le nom du programme. Nous voulons l'ignorer et passer à la valeur suivante, donc tout d'abord nous appelons `next` et ne faisons rien avec la valeur de retour. Ensuite, nous appelons `next` pour obtenir la valeur que nous voulons mettre dans le champ `query` de `Config`. Si `next` renvoie `Some`, nous utilisons un `match` pour extraire la valeur. Si elle renvoie `None`, cela signifie qu'il n'y a pas eu assez d'arguments et nous retournons rapidement avec une valeur `Err`. Nous faisons la même chose pour la valeur `filename`.
