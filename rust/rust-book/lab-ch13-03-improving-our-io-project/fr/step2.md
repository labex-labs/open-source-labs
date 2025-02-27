# Suppression d'un clonage à l'aide d'un itérateur

Dans la liste 12-6, nous avons ajouté du code qui prenait une tranche de valeurs de type `String` et créait une instance de la structure `Config` en utilisant l'indexation dans la tranche et en clonant les valeurs, permettant à la structure `Config` de posséder ces valeurs. Dans la liste 13-17, nous avons reproduit l'implémentation de la fonction `Config::build` telle qu'elle était dans la liste 12-23.

Nom de fichier : `src/lib.rs`

```rust
impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Liste 13-17 : Reproduction de la fonction `Config::build` de la liste 12-23

À l'époque, nous avons dit de ne pas nous inquiéter des appels de `clone` inefficaces car nous les supprimerions plus tard. Eh bien, ce moment est maintenant!

Nous avons eu besoin de `clone` ici car nous avons une tranche avec des éléments de type `String` dans le paramètre `args`, mais la fonction `build` ne possède pas `args`. Pour renvoyer la propriété d'une instance de `Config`, nous avons dû cloner les valeurs des champs `query` et `filename` de `Config` afin que l'instance de `Config` puisse posséder ses valeurs.

Avec nos nouvelles connaissances sur les itérateurs, nous pouvons modifier la fonction `build` pour prendre la propriété d'un itérateur en tant qu'argument au lieu d'emprunter une tranche. Nous utiliserons les fonctionnalités de l'itérateur au lieu du code qui vérifie la longueur de la tranche et effectue des indexations dans des emplacements spécifiques. Cela clarifiera ce que fait la fonction `Config::build` car l'itérateur accédera aux valeurs.

Une fois que `Config::build` prend la propriété de l'itérateur et cesse d'utiliser des opérations d'indexation qui empruntent, nous pouvons déplacer les valeurs de type `String` de l'itérateur dans `Config` plutôt que d'appeler `clone` et de faire une nouvelle allocation.
