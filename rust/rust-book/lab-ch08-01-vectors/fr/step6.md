# Using an Enum to Store Multiple Types

Les vecteurs ne peuvent stocker que des valeurs du même type. Cela peut être gênant ; il existe certainement des cas d'utilisation où il est nécessaire de stocker une liste d'éléments de différents types. Heureusement, les variantes d'un enum sont définies sous le même type d'enum, donc lorsque nous avons besoin d'un type pour représenter des éléments de différents types, nous pouvons définir et utiliser un enum!

Par exemple, disons que nous voulons extraire des valeurs d'une ligne d'un tableur dans laquelle certaines des colonnes de la ligne contiennent des entiers, des nombres à virgule flottante et des chaînes de caractères. Nous pouvons définir un enum dont les variantes contiendront les différents types de valeurs, et toutes les variantes d'enum seront considérées comme le même type : celui de l'enum. Ensuite, nous pouvons créer un vecteur pour stocker cet enum et donc, finalement, stocker différents types. Nous l'avons démontré dans la Liste 8-9.

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

Liste 8-9: Définition d'un `enum` pour stocker des valeurs de différents types dans un seul vecteur

Rust doit savoir quels types seront dans le vecteur à la compilation afin de savoir exactement combien de mémoire sur le tas sera nécessaire pour stocker chaque élément. Nous devons également être explicites sur les types autorisés dans ce vecteur. Si Rust autorisait un vecteur à stocker n'importe quel type, il y aurait une chance qu'un ou plusieurs des types entraînent des erreurs avec les opérations effectuées sur les éléments du vecteur. Utiliser un enum plus une expression `match` signifie que Rust assurera au moment de la compilation que chaque cas possible est traité, comme discuté au Chapitre 6.

Si vous ne connaissez pas l'ensemble exhaustif des types que votre programme recevra à l'exécution pour les stocker dans un vecteur, la technique d'enum ne fonctionnera pas. Au lieu de cela, vous pouvez utiliser un objet trait, que nous aborderons au Chapitre 17.

Maintenant que nous avons discuté de certaines des façons les plus courantes d'utiliser les vecteurs, assurez-vous de consulter la documentation de l'API pour toutes les nombreuses méthodes utiles définies sur `Vec<T>` par la bibliothèque standard. Par exemple, en plus de `push`, une méthode `pop` supprime et renvoie le dernier élément.
