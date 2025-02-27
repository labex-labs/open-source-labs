# Retourner des Types qui Implémentent des Traits

Nous pouvons également utiliser la syntaxe `impl Trait` dans la position de retour pour retourner une valeur d'un certain type qui implémente un trait, comme le montre ici :

```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}
```

En utilisant `impl Summary` pour le type de retour, nous spécifions que la fonction `returns_summarizable` retourne un certain type qui implémente le trait `Summary` sans nommer le type concret. Dans ce cas, `returns_summarizable` retourne un `Tweet`, mais le code appelant cette fonction n'a pas besoin de le savoir.

La capacité de spécifier un type de retour uniquement par le trait qu'il implémente est particulièrement utile dans le contexte des closures et des itérateurs, que nous aborderons au chapitre 13. Les closures et les itérateurs créent des types que seul le compilateur connaît ou des types très longs à spécifier. La syntaxe `impl Trait` vous permet de spécifier de manière concise qu'une fonction retourne un certain type qui implémente le trait `Iterator` sans avoir besoin d'écrire un type très long.

Cependant, vous ne pouvez utiliser `impl Trait` que si vous retournez un seul type. Par exemple, ce code qui retourne soit un `NewsArticle` soit un `Tweet` avec le type de retour spécifié comme `impl Summary` ne fonctionnerait pas :

```rust
fn returns_summarizable(switch: bool) -> impl Summary {
    if switch {
        NewsArticle {
            headline: String::from(
                "Penguins win the Stanley Cup Championship!",
            ),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                 hockey team in the NHL.",
            ),
        }
    } else {
        Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        }
    }
}
```

Retourner soit un `NewsArticle` soit un `Tweet` n'est pas autorisé en raison des restrictions sur la manière dont la syntaxe `impl Trait` est implémentée dans le compilateur. Nous aborderons la manière d'écrire une fonction avec ce comportement dans "Utilisation d'Objets de Trait qui Autorisent des Valeurs de Différents Types".
