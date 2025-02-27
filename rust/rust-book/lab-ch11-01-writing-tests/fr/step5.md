# Ajouter des messages d'erreur personnalisés

Vous pouvez également ajouter un message personnalisé à imprimer avec le message d'erreur en tant qu'arguments optionnels aux macros `assert!`, `assert_eq!` et `assert_ne!`. Tous les arguments spécifiés après les arguments requis sont transmis à la macro `format!` (discutée dans "Concaténation avec l'opérateur + ou la macro format!"), de sorte que vous pouvez passer une chaîne de formatage qui contient des emplacements `{}` et des valeurs à insérer dans ces emplacements. Les messages personnalisés sont utiles pour documenter ce qu'une assertion signifie ; lorsqu'un test échoue, vous aurez une meilleure idée du problème avec le code.

Par exemple, disons que nous avons une fonction qui salue les gens par leur nom et que nous voulons tester que le nom que nous passons à la fonction apparaît dans la sortie :

Nom de fichier : `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

Les exigences de ce programme n'ont pas encore été convenues, et nous sommes assez sûrs que le texte `Hello` au début de la salutation changera. Nous avons décidé que nous ne voulons pas devoir mettre à jour le test lorsque les exigences changent, donc au lieu de vérifier l'égalité exacte avec la valeur renvoyée par la fonction `greeting`, nous allons simplement affirmer que la sortie contient le texte du paramètre d'entrée.

Maintenant, introduisons une erreur dans ce code en changeant `greeting` pour exclure `name` pour voir à quoi ressemble l'erreur de test par défaut :

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

Exécuter ce test produit ceci :

    exécution d'un test
    test tests::greeting_contains_name... FAILED

    échecs :

    ---- tests::greeting_contains_name sortie standard ----
    thread'main' a généré une erreur à 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher
    une trace de pile


    échecs :
        tests::greeting_contains_name

Ce résultat indique simplement que l'assertion a échoué et sur quelle ligne se trouve l'assertion. Un message d'erreur plus utile afficherait la valeur de la fonction `greeting`. Ajoutons un message d'erreur personnalisé composé d'une chaîne de formatage avec un emplacement remplacé par la valeur réelle que nous avons obtenue de la fonction `greeting` :

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

Maintenant, lorsque nous exécutons le test, nous obtiendrons un message d'erreur plus informatif :

    ---- tests::greeting_contains_name sortie standard ----
    thread'main' a généré une erreur à 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher
    une trace de pile

Nous pouvons voir la valeur que nous avons effectivement obtenue dans la sortie du test, ce qui nous aiderait à déboguer ce qui s'est passé au lieu de ce que nous nous attendions à ce qui se passe.
