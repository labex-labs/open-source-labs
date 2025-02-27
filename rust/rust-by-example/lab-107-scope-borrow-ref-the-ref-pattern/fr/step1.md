# Le motif `ref`

Lors de la correspondance de motifs ou de la déconstruction via la liaison `let`, le mot clé `ref` peut être utilisé pour prendre des références aux champs d'un struct/tuple. L'exemple ci-dessous montre quelques cas où cela peut être utile :

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // Un emprunt `ref` du côté gauche d'une affectation est équivalent à
    // un emprunt `&` du côté droit.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 est égal à ref_c2 : {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` est également valide lors de la déconstruction d'un struct.
    let _copy_of_x = {
        // `ref_to_x` est une référence au champ `x` de `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Retourne une copie du champ `x` de `point`.
        *ref_to_x
    };

    // Une copie mutable de `point`
    let mut mutable_point = point;

    {
        // `ref` peut être combiné avec `mut` pour prendre des références mutables.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Modifie le champ `y` de `mutable_point` via une référence mutable.
        *mut_ref_to_y = 1;
    }

    println!("point est ({}, {})", point.x, point.y);
    println!("mutable_point est ({}, {})", mutable_point.x, mutable_point.y);

    // Un tuple mutable qui inclut un pointeur
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Découpe `mutable_tuple` pour changer la valeur de `last`.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple est {:?}", mutable_tuple);
}
```
