# Écrire un test qui échoue

Puisque nous n'avons plus besoin de ces instructions, supprimons les instructions `println!` de `src/lib.rs` et `src/main.rs` que nous avons utilisées pour vérifier le comportement du programme. Ensuite, dans `src/lib.rs`, nous allons ajouter un module `tests` avec une fonction de test, comme nous l'avons fait au chapitre 11. La fonction de test spécifie le comportement que nous souhaitons que la fonction `search` ait : elle prendra une requête et le texte à rechercher, et elle retournera uniquement les lignes du texte qui contiennent la requête. Le listing 12-15 montre ce test, qui ne compilera pas encore.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

Listing 12-15 : Création d'un test qui échoue pour la fonction `search` que nous aimerions avoir

Ce test recherche la chaîne de caractères `"duct"`. Le texte que nous recherchons est composé de trois lignes, dont seulement une contient `"duct"` (remarquez que le backslash après la double quote ouvrante indique à Rust de ne pas insérer un caractère de nouvelle ligne au début du contenu de cette chaîne littérale). Nous affirmons que la valeur retournée par la fonction `search` contient uniquement la ligne que nous attendons.

Nous ne sommes pas encore en mesure d'exécuter ce test et de le voir échouer car le test ne compile même pas : la fonction `search` n'existe pas encore! Conformément aux principes du TDD, nous allons ajouter juste assez de code pour que le test compile et s'exécute en ajoutant une définition de la fonction `search` qui renvoie toujours un vecteur vide, comme montré dans le listing 12-16. Ensuite, le test devrait compiler et échouer car un vecteur vide ne correspond pas à un vecteur contenant la ligne `"safe, fast, productive."`.

Nom de fichier : `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

Listing 12-16 : Définition suffisante de la fonction `search` pour que notre test compile

Remarquez que nous devons définir une durée de vie explicite `'a` dans la signature de `search` et utiliser cette durée de vie avec l'argument `contents` et la valeur de retour. Rappelez-vous au chapitre 10 que les paramètres de durée de vie spécifient quelle durée de vie d'argument est connectée à la durée de vie de la valeur de retour. Dans ce cas, nous indiquons que le vecteur retourné devrait contenir des fragments de chaîne qui font référence à des fragments de l'argument `contents` (plutôt que de l'argument `query`).

En d'autres termes, nous disons à Rust que les données retournées par la fonction `search` existeront aussi longtemps que les données passées à la fonction `search` dans l'argument `contents`. C'est important! Les données référencées _par_ un fragment doivent être valides pour que la référence soit valide ; si le compilateur suppose que nous créons des fragments de chaîne de `query` plutôt que de `contents`, il effectuera son contrôle de sécurité de manière incorrecte.

Si nous oublions les annotations de durée de vie et essayons de compiler cette fonction, nous obtiendrons cette erreur :

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust ne peut pas savoir lequel des deux arguments nous avons besoin, donc nous devons le lui dire explicitement. Puisque `contents` est l'argument qui contient tout notre texte et que nous voulons retourner les parties de ce texte qui correspondent, nous savons que `contents` est l'argument qui devrait être connecté à la valeur de retour en utilisant la syntaxe de durée de vie.

D'autres langages de programmation ne vous obligent pas à connecter les arguments à la valeur de retour dans la signature, mais cette pratique deviendra plus facile avec le temps. Vous pouvez vouloir comparer cet exemple avec les exemples de "Validation des références avec les durées de vie".

Maintenant, exécutons le test :

```bash

```

Parfait, le test échoue, exactement comme nous l'attendions. Faisons passer le test!
