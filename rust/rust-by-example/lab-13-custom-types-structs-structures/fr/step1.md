# Structures

Il existe trois types de structures ("structs") qui peuvent être créées en utilisant le mot clé `struct` :

- Les structs tuple, qui sont, fondamentalement, des tuples nommés.
- Les structs C classiques
- Les structs unitaires, qui n'ont pas de champ, sont utiles pour les génériques.

```rust
// Un attribut pour masquer les avertissements pour le code inutilisé.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// Une struct unitaire
struct Unit;

// Une struct tuple
struct Pair(i32, f32);

// Une struct avec deux champs
struct Point {
    x: f32,
    y: f32,
}

// Les structs peuvent être réutilisés comme champs d'un autre struct
struct Rectangle {
    // Un rectangle peut être spécifié par l'emplacement des coins supérieur gauche et inférieur droit
    // dans l'espace.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // Créer une struct avec la notation raccourcie d'initialisation de champ
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Afficher la struct en mode debug
    println!("{:?}", peter);

    // Instancier un `Point`
    let point: Point = Point { x: 10.3, y: 0.4 };

    // Accéder aux champs du point
    println!("coordonnées du point : ({}, {})", point.x, point.y);

    // Créer un nouveau point en utilisant la syntaxe de mise à jour de struct pour utiliser les champs de notre
    // autre point
    let bottom_right = Point { x: 5.2,..point };

    // `bottom_right.y` sera le même que `point.y` car nous avons utilisé ce champ
    // de `point`
    println!("second point : ({}, {})", bottom_right.x, bottom_right.y);

    // Déstructurer le point en utilisant une liaison `let`
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // L'instanciation de struct est également une expression
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Instancier une struct unitaire
    let _unit = Unit;

    // Instancier une struct tuple
    let pair = Pair(1, 0.1);

    // Accéder aux champs d'une struct tuple
    println!("pair contient {:?} et {:?}", pair.0, pair.1);

    // Déstructurer une struct tuple
    let Pair(integer, decimal) = pair;

    println!("pair contient {:?} et {:?}", integer, decimal);
}
```

## Activité

1. Ajouter une fonction `rect_area` qui calcule l'aire d'un `Rectangle` (essayez d'utiliser la déstructuration imbriquée).
2. Ajouter une fonction `square` qui prend un `Point` et un `f32` en arguments, et renvoie un `Rectangle` dont le coin supérieur gauche est sur le point, et une largeur et une hauteur correspondant au `f32`.
