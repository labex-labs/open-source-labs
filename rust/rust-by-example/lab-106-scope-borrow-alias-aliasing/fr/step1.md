# Aliasing

Les données peuvent être empruntées de manière immuable un nombre quelconque de fois, mais tant qu'elles sont empruntées de manière immuable, les données d'origine ne peuvent pas être empruntées de manière mutable. D'un autre côté, seul _un_ prêt mutable est autorisé à la fois. Les données d'origine ne peuvent être empruntées à nouveau que _après_ que la référence mutable ait été utilisée pour la dernière fois.

```rust
struct Point { x: i32, y: i32, z: i32 }

fn main() {
    let mut point = Point { x: 0, y: 0, z: 0 };

    let borrowed_point = &point;
    let another_borrow = &point;

    // Les données peuvent être accessibles via les références et le propriétaire original
    println!("Point a les coordonnées : ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Erreur! Impossible d'emprunter `point` en tant que mutable car il est actuellement
    // emprunté en tant qu'immutable.
    // let mutable_borrow = &mut point;
    // TODO ^ Essayez de décommenter cette ligne

    // Les valeurs empruntées sont utilisées à nouveau ici
    println!("Point a les coordonnées : ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // Les références immuables ne sont plus utilisées pour le reste du code donc
    // il est possible de réemprunter avec une référence mutable.
    let mutable_borrow = &mut point;

    // Modifier les données via la référence mutable
    mutable_borrow.x = 5;
    mutable_borrow.y = 2;
    mutable_borrow.z = 1;

    // Erreur! Impossible d'emprunter `point` en tant qu'immutable car il est actuellement
    // emprunté en tant que mutable.
    // let y = &point.y;
    // TODO ^ Essayez de décommenter cette ligne

    // Erreur! Impossible d'afficher car `println!` prend une référence immutable.
    // println!("Point Z coordinate is {}", point.z);
    // TODO ^ Essayez de décommenter cette ligne

    // Ok! Les références mutables peuvent être passées en tant qu'immutables à `println!`
    println!("Point a les coordonnées : ({}, {}, {})",
                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);

    // La référence mutable n'est plus utilisée pour le reste du code donc il
    // est possible de réemprunter
    let new_borrowed_point = &point;
    println!("Point a maintenant les coordonnées : ({}, {}, {})",
             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);
}
```
