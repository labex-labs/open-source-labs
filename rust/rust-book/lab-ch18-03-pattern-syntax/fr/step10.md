# Déconstruction de structs et de tuples

Nous pouvons mélanger, combiner et imbriquer des motifs de déconstruction de manière encore plus complexe. L'exemple suivant montre une déconstruction complexe où nous imbriquons des structs et des tuples à l'intérieur d'un tuple et décomposons toutes les valeurs primitives :

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

Ce code nous permet de séparer des types complexes en leurs parties constitutives afin que nous puissions utiliser séparément les valeurs qui nous intéressent.

La déconstruction avec des motifs est un moyen pratique d'utiliser des parties de valeurs, telles que les valeurs de chaque champ dans une struct, séparément les unes des autres.
