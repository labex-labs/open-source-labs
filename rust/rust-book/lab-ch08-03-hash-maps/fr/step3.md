# Accessing Values in a Hash Map (Accès aux valeurs dans une table de hachage)

Nous pouvons extraire une valeur de la table de hachage en fournissant sa clé à la méthode `get`, comme indiqué dans la liste 8 - 21.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Liste 8 - 21 : Accès au score de l'équipe Bleue stocké dans la table de hachage

Ici, `score` aura la valeur associée à l'équipe Bleue, et le résultat sera `10`. La méthode `get` renvoie un `Option<&V>` ; s'il n'y a pas de valeur pour cette clé dans la table de hachage, `get` renverra `None`. Ce programme gère l'`Option` en appelant `copied` pour obtenir un `Option<i32>` plutôt qu'un `Option<&i32>`, puis `unwrap_or` pour définir `score` à zéro si `scores` n'a pas d'entrée pour la clé.

Nous pouvons itérer sur chaque paire clé - valeur dans une table de hachage de la même manière que nous le faisons avec les vecteurs, en utilisant une boucle `for` :

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

Ce code affichera chaque paire dans un ordre arbitraire :

```rust
Yellow: 50
Blue: 10
```
