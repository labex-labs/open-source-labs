# Adding a Key and Value Only If a Key Isn't Present (Ajout d'une clé et d'une valeur seulement si la clé n'existe pas)

Il est courant de vérifier si une clé particulière existe déjà dans la table de hachage avec une valeur, puis de prendre les actions suivantes : si la clé existe déjà dans la table de hachage, la valeur existante doit rester telle quelle ; si la clé n'existe pas, l'insérer avec une valeur associée.

Les tables de hachage ont une API spéciale pour cela appelée `entry` qui prend en paramètre la clé que vous souhaitez vérifier. La valeur de retour de la méthode `entry` est une énumération appelée `Entry` qui représente une valeur qui peut exister ou non. Disons que nous voulons vérifier si la clé de l'équipe Jaune a une valeur associée. Si ce n'est pas le cas, nous voulons insérer la valeur `50`, et de même pour l'équipe Bleue. En utilisant l'API `entry`, le code ressemble à la liste 8 - 24.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);

scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);
```

Liste 8 - 24 : Utilisation de la méthode `entry` pour insérer seulement si la clé n'a pas déjà de valeur

La méthode `or_insert` sur `Entry` est définie pour retourner une référence mutable à la valeur pour la clé `Entry` correspondante si cette clé existe, et sinon, elle insère le paramètre comme nouvelle valeur pour cette clé et retourne une référence mutable à la nouvelle valeur. Cette technique est beaucoup plus propre que d'écrire la logique nous - mêmes et, en outre, fonctionne mieux avec le vérificateur d'emprunts.

L'exécution du code de la liste 8 - 24 affichera `{"Yellow": 50, "Blue": 10}`. Le premier appel à `entry` insérera la clé de l'équipe Jaune avec la valeur `50` car l'équipe Jaune n'a pas déjà de valeur. Le deuxième appel à `entry` ne changera pas la table de hachage car l'équipe Bleue a déjà la valeur `10`.
