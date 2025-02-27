# Implémentations Par Défaut

Parfois, il est utile d'avoir un comportement par défaut pour certaines ou toutes les méthodes d'un trait, plutôt que de demander des implémentations pour toutes les méthodes sur chaque type. Ensuite, lorsque nous implémentons le trait sur un type particulier, nous pouvons conserver ou remplacer le comportement par défaut de chaque méthode.

Dans la liste 10-14, nous spécifions une chaîne de caractères par défaut pour la méthode `summarize` du trait `Summary`, au lieu de seulement définir la signature de la méthode, comme nous l'avons fait dans la liste 10-12.

Nom du fichier : `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Lire la suite...)")
    }
}
```

Liste 10-14 : Définition d'un trait `Summary` avec une implémentation par défaut de la méthode `summarize`

Pour utiliser l'implémentation par défaut pour résumer des instances de `NewsArticle`, nous spécifions un bloc `impl` vide avec `impl Summary for NewsArticle {}`.

Même si nous ne définissons plus directement la méthode `summarize` sur `NewsArticle`, nous avons fourni une implémentation par défaut et spécifié que `NewsArticle` implémente le trait `Summary`. En conséquence, nous pouvons toujours appeler la méthode `summarize` sur une instance de `NewsArticle`, comme ceci :

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

Ce code affiche `New article available! (Lire la suite...)`.

Créer une implémentation par défaut ne nécessite pas que nous changions quoi que ce soit dans l'implémentation de `Summary` sur `Tweet` dans la liste 10-13. La raison en est que la syntaxe pour remplacer une implémentation par défaut est la même que la syntaxe pour implémenter une méthode de trait qui n'a pas d'implémentation par défaut.

Les implémentations par défaut peuvent appeler d'autres méthodes dans le même trait, même si ces autres méthodes n'ont pas d'implémentation par défaut. De cette manière, un trait peut fournir beaucoup de fonctionnalités utiles et ne demander aux implémentateurs de spécifier qu'une petite partie d'entre elles. Par exemple, nous pourrions définir le trait `Summary` pour avoir une méthode `summarize_author` dont l'implémentation est requise, puis définir une méthode `summarize` qui a une implémentation par défaut qui appelle la méthode `summarize_author` :

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Lire la suite de {}...)",
            self.summarize_author()
        )
    }
}
```

Pour utiliser cette version de `Summary`, nous n'avons besoin que de définir `summarize_author` lorsque nous implémentons le trait sur un type :

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

Après avoir défini `summarize_author`, nous pouvons appeler `summarize` sur des instances du struct `Tweet`, et l'implémentation par défaut de `summarize` appellera la définition de `summarize_author` que nous avons fournie. Parce que nous avons implémenté `summarize_author`, le trait `Summary` nous a donné le comportement de la méthode `summarize` sans que nous ayons besoin d'écrire plus de code. Voici à quoi cela ressemble :

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

Ce code affiche `1 new tweet: (Lire la suite de @horse_ebooks...)`.

Notez qu'il n'est pas possible d'appeler l'implémentation par défaut à partir d'une implémentation qui remplace la même méthode.
