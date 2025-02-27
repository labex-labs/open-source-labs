# Implémenter un Trait sur un Type

Maintenant que nous avons défini les signatures souhaitées des méthodes du trait `Summary`, nous pouvons l'implementer sur les types de notre agrégateur de médias. La liste 10-13 montre une implémentation du trait `Summary` sur le struct `NewsArticle` qui utilise le titre, l'auteur et l'emplacement pour créer la valeur de retour de `summarize`. Pour le struct `Tweet`, nous définissons `summarize` comme le nom d'utilisateur suivi du texte complet du tweet, en supposant que le contenu du tweet est déjà limité à 280 caractères.

Nom du fichier : `src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

Liste 10-13 : Implémentation du trait `Summary` sur les types `NewsArticle` et `Tweet`

L'implémentation d'un trait sur un type est similaire à l'implémentation de méthodes régulières. La différence est que après `impl`, nous mettons le nom du trait que nous voulons implémenter, puis utilisons le mot clé `for`, et ensuite spécifions le nom du type pour lequel nous voulons implémenter le trait. Dans le bloc `impl`, nous mettons les signatures de méthodes définies par la définition du trait. Au lieu d'ajouter un point-virgule après chaque signature, nous utilisons des accolades et remplissons le corps de la méthode avec le comportement spécifique que nous voulons que les méthodes du trait aient pour le type particulier.

Maintenant que la bibliothèque a implémenté le trait `Summary` sur `NewsArticle` et `Tweet`, les utilisateurs de la crate peuvent appeler les méthodes du trait sur des instances de `NewsArticle` et `Tweet` de la même manière que nous appelons les méthodes régulières. La seule différence est que l'utilisateur doit également porter le trait dans le scope, ainsi que les types. Voici un exemple de la manière dont une crate binaire pourrait utiliser notre bibliothèque de crate `aggregator` :

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

Ce code affiche `1 new tweet: horse_ebooks: of course, as you probably already know, people`.

D'autres crates qui dépendent de la crate `aggregator` peuvent également porter le trait `Summary` dans le scope pour implémenter `Summary` sur leurs propres types. Une restriction à noter est que nous ne pouvons implémenter un trait sur un type que si le trait ou le type, ou les deux, sont locaux à notre crate. Par exemple, nous pouvons implémenter des traits de la bibliothèque standard comme `Display` sur un type personnalisé comme `Tweet` en tant que partie de la fonctionnalité de notre crate `aggregator` car le type `Tweet` est local à notre crate `aggregator`. Nous pouvons également implémenter `Summary` sur `Vec<T>` dans notre crate `aggregator` car le trait `Summary` est local à notre crate `aggregator`.

Mais nous ne pouvons pas implémenter des traits externes sur des types externes. Par exemple, nous ne pouvons pas implémenter le trait `Display` sur `Vec<T>` dans notre crate `aggregator` car `Display` et `Vec<T>` sont tous deux définis dans la bibliothèque standard et ne sont pas locaux à notre crate `aggregator`. Cette restriction est partie d'une propriété appelée _cohérence_, et plus précisément la _règle de l'orphelin_, ainsi nommée parce que le type parent n'est pas présent. Cette règle garantit que le code d'autres personnes ne peut pas casser votre code et vice versa. Sans cette règle, deux crates pourraient implémenter le même trait pour le même type, et Rust ne saurait laquelle des implémentations utiliser.
