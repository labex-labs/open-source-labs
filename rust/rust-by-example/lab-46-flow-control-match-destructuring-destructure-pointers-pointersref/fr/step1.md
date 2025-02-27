# pointers/ref

Pour les pointeurs, il est important de distinguer la déstructuration et la déréférencement car ce sont des concepts différents qui sont utilisés différemment des langages tels que C/C++.

- La déréférencement utilise `*`
- La déstructuration utilise `&`, `ref` et `ref mut`

```rust
fn main() {
    // Affectez une référence de type `i32`. Le `&` signifie qu'il
    // y a une référence qui est assignée.
    let reference = &4;

    match reference {
        // Si `reference` est comparé avec le motif `&val`, cela donne
        // une comparaison du type :
        // `&i32`
        // `&val`
        // ^ Nous voyons que si les `&` de correspondance sont supprimés,
        // alors l'`i32` devrait être assigné à `val`.
        &val => println!("Got a value via destructuring: {:?}", val),
    }

    // Pour éviter le `&`, vous déréférez avant de comparer.
    match *reference {
        val => println!("Got a value via dereferencing: {:?}", val),
    }

    // Et si vous ne commencez pas avec une référence? `reference` était
    // un `&` car le côté droit était déjà une référence. Ceci n'est
    // pas une référence car le côté droit n'en est pas un.
    let _not_a_reference = 3;

    // Rust fournit `ref` pour exactement cet usage. Il modifie
    // l'affectation de manière à créer une référence pour l'élément ;
    // cette référence est assignée.
    let ref _is_a_reference = 3;

    // En conséquence, en définissant 2 valeurs sans référence, des
    // références peuvent être obtenues via `ref` et `ref mut`.
    let value = 5;
    let mut mut_value = 6;

    // Utilisez le mot clé `ref` pour créer une référence.
    match value {
        ref r => println!("Got a reference to a value: {:?}", r),
    }

    // Utilisez `ref mut` de la même manière.
    match mut_value {
        ref mut m => {
            // Nous avons une référence. Nous devons la déréférencer
            // avant de pouvoir y ajouter quoi que ce soit.
            *m += 10;
            println!("We added 10. `mut_value`: {:?}", m);
        },
    }
}
```
