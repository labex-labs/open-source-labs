# Rendre le code plus clair avec des adaptateurs d'itérateurs

Nous pouvons également tirer parti des itérateurs dans la fonction `search` de notre projet E/S. Elle est reproduite ici dans la liste 13-21 telle qu'elle était dans la liste 12-19.

Nom de fichier : `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Liste 13-21 : L'implémentation de la fonction `search` de la liste 12-19

Nous pouvons écrire ce code d'une manière plus concise en utilisant des méthodes d'adaptateurs d'itérateurs. Cela nous permet également d'éviter d'avoir un vecteur intermédiaire mutable `results`. Le style de programmation fonctionnelle préfère minimiser la quantité d'état mutable pour rendre le code plus clair. Supprimer l'état mutable pourrait permettre une amélioration future pour effectuer la recherche en parallèle car nous n'aurions pas à gérer l'accès concurrent au vecteur `results`. La liste 13-22 montre ce changement.

Nom de fichier : `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
     .lines()
     .filter(|line| line.contains(query))
     .collect()
}
```

Liste 13-22 : Utilisation de méthodes d'adaptateurs d'itérateurs dans l'implémentation de la fonction `search`

Rappelez-vous que le but de la fonction `search` est de renvoyer toutes les lignes de `contents` qui contiennent la `query`. De manière similaire à l'exemple de `filter` dans la liste 13-16, ce code utilise l'adaptateur `filter` pour ne conserver que les lignes pour lesquelles `line.contains(query)` renvoie `true`. Nous collectons ensuite les lignes correspondantes dans un autre vecteur avec `collect`. Beaucoup plus simple! N'hésitez pas à apporter le même changement pour utiliser des méthodes d'itérateurs dans la fonction `search_case_insensitive` également.
