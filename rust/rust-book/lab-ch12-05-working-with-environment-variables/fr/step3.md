# Implémentation de la fonction `search_case_insensitive`

La fonction `search_case_insensitive`, présentée dans la Liste 12-21, sera presque identique à la fonction `search`. La seule différence est que nous allons convertir en minuscules la `query` et chaque `ligne` afin que, quelle que soit la casse des arguments d'entrée, elles auront la même casse lorsque nous vérifions si la ligne contient la requête.

Nom de fichier : `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Liste 12-21 : Définition de la fonction `search_case_insensitive` pour convertir en minuscules la requête et la ligne avant de les comparer

Tout d'abord, nous convertissons en minuscules la chaîne `query` et la stockons dans une variable masquée avec le même nom \[1\]. Appeler `to_lowercase` sur la requête est nécessaire afin que, que la requête de l'utilisateur soit `"rust"`, `"RUST"`, `"Rust"` ou `"rUsT"`, nous traitons la requête comme si elle était `"rust"` et soyons insensibles à la casse. Bien que `to_lowercase` gère les caractères Unicode de base, il ne sera pas 100 % précis. Si nous écrivions une application réelle, nous voudrions faire un peu plus de travail ici, mais cette section porte sur les variables d'environnement, pas sur Unicode, donc nous laissons les choses comme ça pour l'instant.

Notez que `query` est maintenant une `String` plutôt qu'un slice de chaîne car appeler `to_lowercase` crée de nouvelles données plutôt que de référencer des données existantes. Par exemple, disons que la requête est `"rUsT"`: ce slice de chaîne ne contient pas de `u` ou de `t` en minuscules pour nous l'utiliser, donc nous devons allouer une nouvelle `String` contenant `"rust"`. Lorsque nous passons `query` en tant qu'argument à la méthode `contains` maintenant, nous devons ajouter un ampersand \[3\] car la signature de `contains` est définie pour prendre un slice de chaîne.

Ensuite, nous ajoutons un appel à `to_lowercase` sur chaque `ligne` pour convertir tous les caractères en minuscules \[2\]. Maintenant que nous avons converti `ligne` et `query` en minuscules, nous trouverons des correspondances quelle que soit la casse de la requête.

Voyons si cette implémentation passe les tests :

    running 2 tests
    test tests::case_insensitive... ok
    test tests::case_sensitive... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Génial! Ils ont passé. Maintenant, appelons la nouvelle fonction `search_case_insensitive` depuis la fonction `run`. Tout d'abord, nous allons ajouter une option de configuration à la structure `Config` pour basculer entre une recherche sensible à la casse et une recherche insensible à la casse. Ajouter ce champ entraînera des erreurs de compilation car nous n'initialisons pas ce champ nulle part pour le moment :

Nom de fichier : `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

Nous avons ajouté le champ `ignore_case` qui contient un booléen. Ensuite, nous avons besoin que la fonction `run` vérifie la valeur du champ `ignore_case` et utilise cela pour décider d'appeler la fonction `search` ou la fonction `search_case_insensitive`, comme montré dans la Liste 12-22. Cela ne compilera toujours pas pour le moment.

Nom de fichier : `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Liste 12-22 : Appel de `search` ou `search_case_insensitive` en fonction de la valeur de `config.ignore_case`

Enfin, nous devons vérifier la variable d'environnement. Les fonctions pour travailler avec les variables d'environnement se trouvent dans le module `env` de la bibliothèque standard, donc nous importons ce module dans la portée en haut de `src/lib.rs`. Ensuite, nous utiliserons la fonction `var` du module `env` pour vérifier si une valeur a été définie pour une variable d'environnement nommée `IGNORE_CASE`, comme montré dans la Liste 12-23.

Nom de fichier : `src/lib.rs`

```rust
use std::env;
--snip--

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

Liste 12-23 : Vérification de la présence d'une valeur dans une variable d'environnement nommée `IGNORE_CASE`

Ici, nous créons une nouvelle variable, `ignore_case`. Pour définir sa valeur, nous appelons la fonction `env::var` et lui passons le nom de la variable d'environnement `IGNORE_CASE`. La fonction `env::var` renvoie un `Result` qui sera la variante `Ok` réussie qui contient la valeur de la variable d'environnement si la variable d'environnement est définie avec n'importe quelle valeur. Elle renverra la variante `Err` si la variable d'environnement n'est pas définie.

Nous utilisons la méthode `is_ok` sur le `Result` pour vérifier si la variable d'environnement est définie, ce qui signifie que le programme devrait effectuer une recherche insensible à la casse. Si la variable d'environnement `IGNORE_CASE` n'est pas définie à rien, `is_ok` renverra `false` et le programme effectuera une recherche sensible à la casse. Nous ne nous intéressons pas à la _valeur_ de la variable d'environnement, seulement à savoir si elle est définie ou non, donc nous vérifions `is_ok` plutôt qu'en utilisant `unwrap`, `expect` ou l'une des autres méthodes que nous avons vues sur `Result`.

Nous passons la valeur de la variable `ignore_case` à l'instance `Config` afin que la fonction `run` puisse lire cette valeur et décider d'appeler `search_case_insensitive` ou `search`, comme nous l'avons implémenté dans la Liste 12-22.

Essayons ça! Tout d'abord, nous exécutons notre programme sans la variable d'environnement définie et avec la requête `to`, qui devrait correspondre à toute ligne qui contient le mot _to_ en minuscules :

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

Il semble que ça fonctionne toujours! Maintenant, exécutons le programme avec `IGNORE_CASE` défini sur `1` mais avec la même requête `to` :

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

Si vous utilisez PowerShell, vous devrez définir la variable d'environnement et exécuter le programme en tant que commandes séparées :

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

Cela fera en sorte que `IGNORE_CASE` persiste pour le reste de votre session de shell. Elle peut être supprimée avec l'applet de commande `Remove-Item` :

```rust
PS> Remove-Item Env:IGNORE_CASE
```

Nous devrions obtenir les lignes qui contiennent _to_ qui peuvent avoir des lettres majuscules :

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

Excellent, nous avons également obtenu les lignes contenant _To_! Notre programme `minigrep` peut maintenant effectuer une recherche insensible à la casse contrôlée par une variable d'environnement. Maintenant, vous savez comment gérer les options définies à l'aide d'arguments de ligne de commande ou de variables d'environnement.

Certains programmes autorisent les arguments _et_ les variables d'environnement pour la même configuration. Dans ces cas, les programmes décident que l'un ou l'autre prend le pas. Pour une autre exercice à vous-même, essayez de contrôler la sensibilité à la casse via un argument de ligne de commande ou une variable d'environnement. Décidez si l'argument de ligne de commande ou la variable d'environnement devrait prendre le pas si le programme est exécuté avec l'un défini pour être sensible à la casse et l'autre défini pour ignorer la casse.

Le module `std::env` contient de nombreuses autres fonctionnalités utiles pour traiter les variables d'environnement : consultez sa documentation pour voir ce qui est disponible.
