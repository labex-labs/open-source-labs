# Updating a Value Based on the Old Value (Mise à jour d'une valeur en fonction de l'ancienne valeur)

Un autre cas d'utilisation courant des tables de hachage consiste à rechercher la valeur d'une clé, puis à la mettre à jour en fonction de l'ancienne valeur. Par exemple, la liste 8 - 25 montre un code qui compte combien de fois chaque mot apparaît dans un texte. Nous utilisons une table de hachage avec les mots comme clés et incrémentons la valeur pour suivre combien de fois nous avons vu ce mot. S'il s'agit de la première fois que nous voyons un mot, nous insérerons d'abord la valeur `0`.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Liste 8 - 25 : Comptage des occurrences de mots à l'aide d'une table de hachage qui stocke les mots et les compteurs

Ce code affichera `{"world": 2, "hello": 1, "wonderful": 1}`. Vous pourriez voir les mêmes paires clé - valeur affichées dans un ordre différent : rappelez - vous de "Accessing Values in a Hash Map" (Accès aux valeurs dans une table de hachage) que l'itération sur une table de hachage se fait dans un ordre arbitraire.

La méthode `split_whitespace` retourne un itérateur sur les sous - tranches, séparées par des espaces, de la valeur dans `text`. La méthode `or_insert` retourne une référence mutable (`&mut V`) à la valeur pour la clé spécifiée. Ici, nous stockons cette référence mutable dans la variable `count`, donc pour assigner une valeur à cette variable, nous devons d'abord déréférencer `count` en utilisant l'astérisque (`*`). La référence mutable sort de portée à la fin de la boucle `for`, donc tous ces changements sont sûrs et autorisés par les règles d'emprunt.
