# Bounds

tout comme les types génériques peuvent être bornés, les durées de vie (elles-mêmes génériques) utilisent également des bornes. Le caractère `:` a une signification légèrement différente ici, mais `+` est le même. Notez comment la lecture suivante se présente :

1.  `T: 'a` : _Toutes_ les références dans `T` doivent avoir une durée de vie supérieure à la durée de vie `'a`.
2.  `T: Trait + 'a` : Le type `T` doit implémenter le trait `Trait` et _toutes_ les références dans `T` doivent avoir une durée de vie supérieure à `'a`.

L'exemple ci-dessous montre la syntaxe ci-dessus en action utilisée après le mot clé `where` :

```rust
use std::fmt::Debug; // Trait à lier.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` contient une référence à un type générique `T` qui a
// une durée de vie inconnue `'a`. `T` est borné de sorte que toute
// *référence* dans `T` doit avoir une durée de vie supérieure à `'a`. De plus, la durée de vie
// de `Ref` ne peut pas dépasser `'a`.

// Une fonction générique qui imprime en utilisant le trait `Debug`.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t est {:?}", t);
}

// Ici, une référence à `T` est prise où `T` implémente
// `Debug` et toutes les *références* dans `T` ont une durée de vie supérieure à `'a`. En
// outre, `'a` doit avoir une durée de vie supérieure à la fonction.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t est {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```
