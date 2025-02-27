# The Glob Operator

Si nous voulons amener _tous_ les éléments publics définis dans un chemin dans la portée, nous pouvons spécifier ce chemin suivi de l'opérateur `*` de type glob :

```rust
use std::collections::*;
```

Cette instruction `use` amène tous les éléments publics définis dans `std::collections` dans la portée actuelle. Faites attention lorsqu'on utilise l'opérateur glob! Le glob peut rendre plus difficile de savoir quels noms sont dans la portée et où un nom utilisé dans votre programme a été défini.

L'opérateur glob est souvent utilisé lors des tests pour amener tout ce qui est à tester dans le module `tests` ; nous en parlerons dans "Comment écrire des tests". L'opérateur glob est également parfois utilisé comme partie du motif de préambule : consultez la documentation de la bibliothèque standard pour en savoir plus sur ce motif.
