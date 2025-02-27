# Box, pile et tas

Toutes les valeurs en Rust sont par défaut allouées sur la pile. Les valeurs peuvent être « emballées » (allouées sur le tas) en créant un `Box<T>`. Un emballage est un pointeur intelligent vers une valeur allouée sur le tas de type `T`. Lorsqu'un emballage sort de portée, son destructeur est appelé, l'objet interne est détruit et la mémoire sur le tas est libérée.

Les valeurs emballées peuvent être déréférencées à l'aide de l'opérateur `*` ; cela supprime une couche d'indirection.

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// Un Rectangle peut être spécifié par la position de ses coins supérieur gauche et inférieur droit
// dans l'espace
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // Alloue ce point sur le tas et renvoie un pointeur vers lui
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // (toutes les annotations de type sont superflues)
    // Variables allouées sur la pile
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // Rectangle alloué sur le tas
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // La sortie de fonctions peut être emballée
    let boxed_point: Box<Point> = Box::new(origin());

    // Double indirection
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point occupe {} octets sur la pile",
             mem::size_of_val(&point));
    println!("Rectangle occupe {} octets sur la pile",
             mem::size_of_val(&rectangle));

    // taille de l'emballage == taille du pointeur
    println!("Point emballé occupe {} octets sur la pile",
             mem::size_of_val(&boxed_point));
    println!("Rectangle emballé occupe {} octets sur la pile",
             mem::size_of_val(&boxed_rectangle));
    println!("Emballage dans un emballage occupe {} octets sur la pile",
             mem::size_of_val(&box_in_a_box));

    // Copie les données contenues dans `boxed_point` dans `unboxed_point`
    let unboxed_point: Point = *boxed_point;
    println!("Point non emballé occupe {} octets sur la pile",
             mem::size_of_val(&unboxed_point));
}
```
