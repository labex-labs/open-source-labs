# Hash Maps and Ownership (Tables de hachage et propriété)

Pour les types qui implémentent le trait `Copy`, comme `i32`, les valeurs sont copiées dans la table de hachage. Pour les valeurs possédées comme `String`, les valeurs sont déplacées et la table de hachage deviendra le propriétaire de ces valeurs, comme démontré dans la liste 8 - 22.

```rust
use std::collections::HashMap;

let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(field_name, field_value);
// field_name and field_value are invalid at this point, try
// using them and see what compiler error you get!
```

Liste 8 - 22 : Montrant que les clés et les valeurs sont possédées par la table de hachage une fois qu'elles ont été insérées

Nous ne pouvons pas utiliser les variables `field_name` et `field_value` après qu'elles ont été déplacées dans la table de hachage lors de l'appel à `insert`.

Si nous insérons des références à des valeurs dans la table de hachage, les valeurs ne seront pas déplacées dans la table de hachage. Les valeurs auxquelles les références pointent doivent être valides au moins aussi longtemps que la table de hachage est valide. Nous parlerons plus de ces problèmes dans "Validating References with Lifetimes" (Validation des références avec des durées de vie).
