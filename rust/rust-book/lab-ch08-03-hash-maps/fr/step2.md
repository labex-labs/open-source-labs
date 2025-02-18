# Creating a New Hash Map (Création d'une nouvelle table de hachage)

Une façon de créer une table de hachage vide consiste à utiliser `new` et à ajouter des éléments avec `insert`. Dans la liste 8 - 20, nous suivons le score de deux équipes dont les noms sont _Blue_ et _Yellow_. L'équipe Bleue commence avec 10 points, et l'équipe Jaune commence avec 50 points.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

Liste 8 - 20 : Création d'une nouvelle table de hachage et insertion de quelques clés et valeurs

Notez que nous devons d'abord `utiliser` (use) le `HashMap` de la partie collections de la bibliothèque standard. Parmi nos trois collections courantes, celle - ci est la moins souvent utilisée, donc elle n'est pas incluse dans les fonctionnalités automatiquement importées dans la portée par le préambule. Les tables de hachage ont également moins de support de la part de la bibliothèque standard ; il n'y a pas de macro intégrée pour les construire, par exemple.

Tout comme les vecteurs, les tables de hachage stockent leurs données sur le tas. Cette `HashMap` a des clés de type `String` et des valeurs de type `i32`. Comme les vecteurs, les tables de hachage sont homogènes : toutes les clés doivent avoir le même type, et toutes les valeurs doivent avoir le même type.
