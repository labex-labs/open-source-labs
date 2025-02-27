# match Arms

Comme discuté au chapitre 6, nous utilisons des motifs dans les bras des expressions `match`. Formellement, les expressions `match` sont définies par le mot-clé `match`, une valeur à comparer, et un ou plusieurs bras de correspondance qui consistent en un motif et une expression à exécuter si la valeur correspond au motif de ce bras, comme ceci :

    match VALEUR {
        MOTIF => EXPRESSION,
        MOTIF => EXPRESSION,
        MOTIF => EXPRESSION,
    }

Par exemple, voici l'expression `match` de la liste 6-5 qui compare une valeur `Option<i32>` dans la variable `x` :

    match x {
        None => None,
        Some(i) => Some(i + 1),
    }

Les motifs dans cette expression `match` sont `None` et `Some(i)` à gauche de chaque flèche.

Une exigence pour les expressions `match` est qu'elles doivent être _exhaustives_ au sens où toutes les possibilités pour la valeur dans l'expression `match` doivent être prises en compte. Une manière de s'assurer d'avoir couvert toutes les possibilités est d'avoir un motif générique pour le dernier bras : par exemple, un nom de variable correspondant à n'importe quelle valeur ne peut jamais échouer et couvre donc tous les cas restants.

Le motif particulier `_` correspond à tout, mais il ne se lie jamais à une variable, il est donc souvent utilisé dans le dernier bras de correspondance. Le motif `_` peut être utile lorsque vous voulez ignorer toute valeur non spécifiée, par exemple. Nous aborderons le motif `_` en détail dans "Ignoring Values in a Pattern".
