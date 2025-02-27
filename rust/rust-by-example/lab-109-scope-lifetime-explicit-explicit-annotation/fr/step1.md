# Annotation explicite

Le vérificateur d'emprunts utilise des annotations de durée de vie explicites pour déterminer combien de temps les références doivent être valides. Dans les cas où les durées de vie ne sont pas supprimées, Rust nécessite des annotations explicites pour déterminer quelle doit être la durée de vie d'une référence. La syntaxe pour annoter explicitement une durée de vie utilise un caractère apostrophe comme suit :

```rust
foo<'a>
// `foo` a un paramètre de durée de vie `'a`
```

De manière similaire aux closures, l'utilisation de durées de vie nécessite des types génériques. De plus, cette syntaxe de durée de vie indique que la durée de vie de `foo` ne peut pas excéder celle de `'a`. L'annotation explicite d'un type a la forme `&'a T` où `'a` a déjà été introduit.

Dans les cas avec plusieurs durées de vie, la syntaxe est similaire :

```rust
foo<'a, 'b>
// `foo` a des paramètres de durée de vie `'a` et `'b`
```

Dans ce cas, la durée de vie de `foo` ne peut pas excéder celle de `'a` _ou_ `'b`.

Voyez l'exemple suivant pour l'utilisation d'une annotation de durée de vie explicite :

```rust
// `print_refs` prend deux références à `i32` qui ont des
// durées de vie différentes `'a` et `'b`. Ces deux durées de vie doivent toutes les deux
// être au moins aussi longue que la fonction `print_refs`.
fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x is {} and y is {}", x, y);
}

// Une fonction qui prend aucun argument, mais a un paramètre de durée de vie `'a`.
fn failed_borrow<'a>() {
    let _x = 12;

    // ERREUR : `_x` n'existe pas assez longtemps
    let y: &'a i32 = &_x;
    // Tenter d'utiliser la durée de vie `'a` comme une annotation de type explicite
    // à l'intérieur de la fonction échouera car la durée de vie de `&_x` est plus courte
    // que celle de `y`. Une courte durée de vie ne peut pas être convertie en une plus longue.
}

fn main() {
    // Crée des variables à emprunter ci-dessous.
    let (four, nine) = (4, 9);

    // Les emprunts (`&`) des deux variables sont passés à la fonction.
    print_refs(&four, &nine);
    // Tout input qui est emprunté doit exister plus longtemps que l'emprunteur.
    // En d'autres termes, la durée de vie de `four` et `nine` doit
    // être plus longue que celle de `print_refs`.

    failed_borrow();
    // `failed_borrow` ne contient aucune référence pour forcer `'a` à être
    // plus longue que la durée de vie de la fonction, mais `'a` est plus longue.
    // Parce que la durée de vie n'est jamais contrainte, elle est par défaut `'static`.
}
```
