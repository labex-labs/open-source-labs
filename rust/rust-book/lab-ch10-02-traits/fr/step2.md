# Définir un Trait

Le comportement d'un type est constitué des méthodes que l'on peut appeler sur ce type. Différents types partagent le même comportement si l'on peut appeler les mêmes méthodes sur tous ces types. Les définitions de traits sont un moyen de regrouper les signatures de méthodes pour définir un ensemble de comportements nécessaires pour accomplir un certain but.

Par exemple, disons que nous avons plusieurs structs qui contiennent différents types et quantités de texte : un struct `NewsArticle` qui contient un article de presse enregistré à un emplacement particulier et un `Tweet` qui peut avoir au plus 280 caractères, ainsi que des métadonnées indiquant s'il s'agit d'un nouveau tweet, d'un retweet ou d'une réponse à un autre tweet.

Nous voulons créer une bibliothèque de crate d'agrégateur de médias appelée `aggregator` qui peut afficher des résumés de données qui pourraient être stockées dans une instance de `NewsArticle` ou `Tweet`. Pour ce faire, nous avons besoin d'un résumé de chaque type, et nous demanderons ce résumé en appelant une méthode `summarize` sur une instance. La liste 10-12 montre la définition d'un trait public `Summary` qui exprime ce comportement.

Nom du fichier : `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

Liste 10-12 : Un trait `Summary` qui consiste en le comportement fourni par une méthode `summarize`

Ici, nous déclarons un trait en utilisant le mot clé `trait`, puis le nom du trait, qui est `Summary` dans ce cas. Nous déclarons également le trait comme `pub` afin que les crates dépendantes de cette crate puissent également utiliser ce trait, comme nous le verrons dans quelques exemples. Dans les accolades, nous déclarons les signatures de méthodes qui décrivent les comportements des types qui implémentent ce trait, qui est `fn summarize(&self) -> String` dans ce cas.

Après la signature de la méthode, au lieu de fournir une implémentation entre accolades, nous utilisons un point-virgule. Chaque type implémentant ce trait doit fournir son propre comportement personnalisé pour le corps de la méthode. Le compilateur imposera que tout type ayant le trait `Summary` aura la méthode `summarize` définie exactement avec cette signature.

Un trait peut avoir plusieurs méthodes dans son corps : les signatures de méthodes sont listées une par ligne, et chaque ligne se termine par un point-virgule.
