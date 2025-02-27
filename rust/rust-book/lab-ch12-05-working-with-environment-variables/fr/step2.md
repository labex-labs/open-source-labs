# Écrire un test qui échoue pour la fonction de recherche insensible à la casse

Nous commençons par ajouter une nouvelle fonction `search_case_insensitive` qui sera appelée lorsque la variable d'environnement a une valeur. Nous allons continuer à suivre le processus TDD, donc la première étape est encore d'écrire un test qui échoue. Nous allons ajouter un nouveau test pour la nouvelle fonction `search_case_insensitive` et renommer notre ancien test de `one_result` en `case_sensitive` pour clarifier les différences entre les deux tests, comme montré dans la Liste 12-20.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Duct tape.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

Liste 12-20 : Ajout d'un nouveau test qui échoue pour la fonction insensible à la casse que nous allons ajouter

Notez que nous avons également modifié le `contenu` de l'ancien test. Nous avons ajouté une nouvelle ligne avec le texte `"Duct tape."` en utilisant une majuscule _D_ qui ne devrait pas correspondre à la requête `"duct"` lorsque nous effectuons une recherche sensible à la casse. Modifier l'ancien test de cette manière aide à s'assurer que nous ne brisons pas accidentellement la fonctionnalité de recherche sensible à la casse que nous avons déjà implémentée. Ce test devrait passer maintenant et devrait continuer à passer tandis que nous travaillons sur la recherche insensible à la casse.

Le nouveau test pour la recherche _insensible à la casse_ utilise `"rUsT"` comme requête. Dans la fonction `search_case_insensitive` que nous allons ajouter, la requête `"rUsT"` devrait correspondre à la ligne contenant `"Rust:"` avec une majuscule _R_ et correspondre à la ligne `"Trust me."` même si les deux ont une mise en majuscule différente de la requête. C'est notre test qui échoue, et il échouera à compiler car nous n'avons pas encore défini la fonction `search_case_insensitive`. N'hésitez pas à ajouter une implémentation de base qui renvoie toujours un vecteur vide, de la même manière que nous l'avons fait pour la fonction `search` dans la Liste 12-16 pour voir le test compiler et échouer.
