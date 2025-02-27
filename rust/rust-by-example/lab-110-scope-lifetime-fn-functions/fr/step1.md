# Fonctions

En ignorant l'[élision], les signatures de fonctions avec des durées de vie ont quelques contraintes :

- toute référence _doit_ avoir une durée de vie annotée.
- toute référence retournée _doit_ avoir la même durée de vie qu'une entrée ou être `static`.

De plus, notez que la restitution de références sans entrée est interdite si elle entraînerait la restitution de références à des données invalides. L'exemple suivant montre quelques formes valides de fonctions avec des durées de vie :

```rust
// Une référence d'entrée avec la durée de vie `'a` qui doit exister
// au moins aussi longtemps que la fonction.
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x est {}", x);
}

// Les références mutables sont également possibles avec des durées de vie.
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// Plusieurs éléments avec différentes durées de vie. Dans ce cas, il
// serait correct que les deux aient la même durée de vie `'a`, mais
// dans des cas plus complexes, des durées de vie différentes peuvent être requises.
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x est {}, y est {}", x, y);
}

// Retourner des références qui ont été passées en paramètre est acceptable.
// Cependant, la durée de vie correcte doit être retournée.
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// Le code ci-dessus est invalide : `'a` doit exister plus longtemps que la fonction.
// Ici, `&String::from("foo")` créerait une `String`, suivie d'une
// référence. Ensuite, les données seraient supprimées lors de la sortie du scope, laissant
// une référence à des données invalides à retourner.

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```
