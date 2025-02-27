# Dropping a Vector Drops Its Elements

Comme tout autre `struct`, un vecteur est libéré lorsqu'il sort de portée, comme indiqué dans la Liste 8-10.

```rust
{
    let v = vec![1, 2, 3, 4];

    // faire des choses avec v
} // <- v sort de portée et est libéré ici
```

Liste 8-10: Montre où le vecteur et ses éléments sont supprimés

Lorsque le vecteur est supprimé, tous ses contenus sont également supprimés, ce qui signifie que les entiers qu'il contient seront nettoyés. Le vérificateur d'emprunt s'assure que toutes les références aux contenus d'un vecteur ne sont utilisées que tant que le vecteur lui-même est valide.

Passons à la prochaine collection de type : `String`!
