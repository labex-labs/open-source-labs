# Stockage des lignes correspondantes

Pour terminer cette fonction, nous avons besoin d'un moyen de stocker les lignes correspondantes que nous souhaitons retourner. Pour cela, nous pouvons créer un vecteur mutable avant la boucle `for` et appeler la méthode `push` pour stocker une `line` dans le vecteur. Après la boucle `for`, nous retournons le vecteur, comme indiqué dans le listing 12-19.

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

Listing 12-19 : Stockage des lignes correspondantes pour pouvoir les retourner

Maintenant, la fonction `search` devrait retourner uniquement les lignes qui contiennent `query`, et notre test devrait passer. Exécutons le test :

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

Notre test a passé, donc nous savons que ça fonctionne!

À ce stade, nous pourrions considérer des opportunités de refactoring de l'implémentation de la fonction de recherche tout en maintenant les tests en cours pour maintenir la même fonctionnalité. Le code dans la fonction de recherche n'est pas trop mauvais, mais il ne profite pas de certaines fonctionnalités utiles des itérateurs. Nous reviendrons sur cet exemple au chapitre 13, où nous explorerons les itérateurs en détail et verrons comment l'améliorer.
