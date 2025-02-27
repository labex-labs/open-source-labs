# Methods That Produce Other Iterators

Les _adapters d'itérateur_ sont des méthodes définies sur le trait `Iterator` qui ne consomment pas l'itérateur. Au lieu de cela, elles produisent différents itérateurs en modifiant un aspect de l'itérateur original.

La Liste 13-14 montre un exemple d'appel de la méthode d'adaptateur d'itérateur `map`, qui prend une closure à appeler sur chaque élément au fur et à mesure que les éléments sont parcourus. La méthode `map` renvoie un nouvel itérateur qui produit les éléments modifiés. La closure ici crée un nouvel itérateur dans lequel chaque élément du vecteur sera incrémenté de 1.

Nom du fichier : `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

Liste 13-14: Appel de l'adaptateur d'itérateur `map` pour créer un nouvel itérateur

Cependant, ce code produit un avertissement :

    avertissement : `Map` non utilisé qui doit être utilisé
     --> src/main.rs:4:5
      |
    4 |     v1.iter().map(|x| x + 1);
      |     ^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = note : `#[warn(unused_must_use)]` activé par défaut
      = note : les itérateurs sont paresseux et ne font rien tant qu'ils ne sont pas consommés

Le code de la Liste 13-14 ne fait rien ; la closure que nous avons spécifiée n'est jamais appelée. L'avertissement nous rappelle pourquoi : les adapteurs d'itérateur sont paresseux, et nous devons consommer l'itérateur ici.

Pour corriger cet avertissement et consommer l'itérateur, nous utiliserons la méthode `collect`, que nous avons utilisée avec `env::args` dans la Liste 12-1. Cette méthode consomme l'itérateur et rassemble les valeurs résultantes dans un type de données de collection.

Dans la Liste 13-15, nous collectons dans un vecteur les résultats de l'itération sur l'itérateur renvoyé par l'appel à `map`. Ce vecteur finira par contenir chaque élément du vecteur original, incrémenté de 1.

Nom du fichier : `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

Liste 13-15: Appel de la méthode `map` pour créer un nouvel itérateur, puis appel de la méthode `collect` pour consommer le nouvel itérateur et créer un vecteur

Comme `map` prend une closure, nous pouvons spécifier n'importe quelle opération que nous voulons effectuer sur chaque élément. C'est un excellent exemple de la manière dont les closures vous permettent de personnaliser un certain comportement tout en réutilisant le comportement d'itération que le trait `Iterator` fournit.

Vous pouvez chaîner plusieurs appels à des adapteurs d'itérateur pour effectuer des actions complexes de manière lisible. Mais parce que tous les itérateurs sont paresseux, vous devez appeler l'une des méthodes d'adaptateur consommateur pour obtenir des résultats des appels à des adapteurs d'itérateur.
