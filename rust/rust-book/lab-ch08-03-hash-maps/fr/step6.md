# Overwriting a Value (Écrasement d'une valeur)

Si nous insérons une clé et une valeur dans une table de hachage, puis que nous insérons la même clé avec une valeur différente, la valeur associée à cette clé sera remplacée. Bien que le code de la liste 8 - 23 appelle `insert` deux fois, la table de hachage ne contiendra qu'une seule paire clé - valeur car nous insérons la valeur pour la clé de l'équipe Bleue les deux fois.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

Liste 8 - 23 : Remplacement d'une valeur stockée avec une clé particulière

Ce code affichera `{"Blue": 25}`. La valeur originale de `10` a été écrasée.
