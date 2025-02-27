# Traits en tant que Paramètres

Maintenant que vous savez comment définir et implémenter des traits, nous pouvons explorer comment utiliser les traits pour définir des fonctions qui acceptent de nombreux types différents. Nous utiliserons le trait `Summary` que nous avons implémenté sur les types `NewsArticle` et `Tweet` dans la liste 10-13 pour définir une fonction `notify` qui appelle la méthode `summarize` sur son paramètre `item`, qui est d'un certain type qui implémente le trait `Summary`. Pour ce faire, nous utilisons la syntaxe `impl Trait`, comme ceci :

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

Au lieu d'un type concret pour le paramètre `item`, nous spécifions le mot clé `impl` et le nom du trait. Ce paramètre accepte tout type qui implémente le trait spécifié. Dans le corps de `notify`, nous pouvons appeler n'importe quelle méthode sur `item` qui vient du trait `Summary`, comme `summarize`. Nous pouvons appeler `notify` et passer n'importe quelle instance de `NewsArticle` ou `Tweet`. Le code qui appelle la fonction avec n'importe quel autre type, tel qu'une `String` ou un `i32`, ne compilera pas car ces types n'implémentent pas `Summary`.
