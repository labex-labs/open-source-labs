# Thinking in Terms of Lifetimes

La manière dont vous devez spécifier les paramètres de durée de vie dépend de ce que votre fonction fait. Par exemple, si nous changeons l'implémentation de la fonction `longest` pour toujours renvoyer le premier paramètre plutôt que la plus longue slice de chaîne de caractères, nous n'aurons pas besoin de spécifier une durée de vie pour le paramètre `y`. Le code suivant compilera :

Nom de fichier : `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &str) -> &'a str {
    x
}
```

Nous avons spécifié un paramètre de durée de vie `'a` pour le paramètre `x` et le type de retour, mais pas pour le paramètre `y`, car la durée de vie de `y` n'a aucune relation avec la durée de vie de `x` ou de la valeur de retour.

Lorsque l'on renvoie une référence à partir d'une fonction, le paramètre de durée de vie pour le type de retour doit correspondre au paramètre de durée de vie d'un des paramètres. Si la référence renvoyée ne Fait PAS référence à l'un des paramètres, elle doit faire référence à une valeur créée à l'intérieur de cette fonction. Cependant, ce serait une référence fausse car la valeur sortira de portée à la fin de la fonction. Considérez cette tentative d'implémentation de la fonction `longest` qui ne compilera pas :

Nom de fichier : `src/main.rs`

```rust
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

Ici, même si nous avons spécifié un paramètre de durée de vie `'a` pour le type de retour, cette implémentation ne compilera pas car la durée de vie de la valeur de retour n'est pas du tout liée à la durée de vie des paramètres. Voici le message d'erreur que nous obtenons :

```bash
error[E0515]: cannot return reference to local variable `result`
  --> src/main.rs:11:5
   |
11 |     result.as_str()
   |     ^^^^^^^^^^^^^^^ returns a reference to data owned by the
current function
```

Le problème est que `result` sort de portée et est nettoyé à la fin de la fonction `longest`. Nous essayons également de renvoyer une référence à `result` à partir de la fonction. Il n'y a aucun moyen pour nous de spécifier des paramètres de durée de vie qui changeraient la référence fausse, et Rust ne nous laissera pas créer une référence fausse. Dans ce cas, la meilleure solution serait de renvoyer un type de données propriétaire plutôt qu'une référence, de sorte que la fonction appelante soit alors responsable de la nettoyage de la valeur.

En fin de compte, la syntaxe de durée de vie est destinée à connecter les durées de vie de divers paramètres et de valeurs de retour de fonctions. Une fois qu'elles sont connectées, Rust dispose d'informations suffisantes pour autoriser des opérations sécurisées en mémoire et interdire les opérations qui créeraient des pointeurs faussement rattachés ou qui enfreindraient autrement la sécurité mémoire.
