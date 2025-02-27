# Generic Type Parameters, Trait Bounds, and Lifetimes Together

Jetons un coup d'œil rapide à la syntaxe de spécification des paramètres de type générique, des contraintes de trait et des durées de vie dans une seule fonction!

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Il s'agit de la fonction `longest` de la Liste 10-21 qui renvoie la chaîne de caractères la plus longue parmi deux slices de chaîne. Mais maintenant, elle a un paramètre supplémentaire nommé `ann` du type générique `T`, qui peut être remplacé par n'importe quel type qui implémente le trait `Display` tel que spécifié dans la clause `where`. Ce paramètre supplémentaire sera affiché en utilisant `{}`, ce qui explique pourquoi la contrainte de trait `Display` est nécessaire. Étant donné que les durées de vie sont un type de paramètre générique, les déclarations du paramètre de durée de vie `'a` et du paramètre de type générique `T` se trouvent dans la même liste à l'intérieur des crochets angulaires après le nom de la fonction.
