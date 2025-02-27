# Box, Stack und Heap

Alle Werte in Rust werden standardmäßig auf dem Stack zugewiesen. Werte können _geboxed_ (auf dem Heap zugewiesen) werden, indem ein `Box<T>` erstellt wird. Ein Box ist ein Smart-Pointer auf einen auf dem Heap zugewiesenen Wert vom Typ `T`. Wenn ein Box außer Reichweite gelangt, wird dessen Destruktor aufgerufen, das innere Objekt zerstört und der Speicher auf dem Heap freigegeben.

Geboxte Werte können mit dem `*`-Operator dereferenziert werden; dadurch wird eine Ebene der Indirektion entfernt.

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// Ein Rechteck kann durch die Position seiner oberen linken und unteren rechten
// Ecken im Raum angegeben werden
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // Weisen diesen Punkt auf dem Heap zu und gebe einen Zeiger darauf zurück
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // (alle Typangaben sind überflüssig)
    // Auf dem Stack zugewiesene Variablen
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // Auf dem Heap zugewiesenes Rechteck
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // Die Ausgabe von Funktionen kann geboxed werden
    let boxed_point: Box<Point> = Box::new(origin());

    // Doppelindirektion
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&point));
    println!("Rectangle nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&rectangle));

    // Box-Größe == Zeigergröße
    println!("Geboxter Punkt nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&boxed_point));
    println!("Geboxtes Rechteck nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&boxed_rectangle));
    println!("Geboxte Box nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&box_in_a_box));

    // Kopiere die in `boxed_point` enthaltenen Daten in `unboxed_point`
    let unboxed_point: Point = *boxed_point;
    println!("Entboxter Punkt nimmt auf dem Stack {} Bytes ein",
             mem::size_of_val(&unboxed_point));
}
```
