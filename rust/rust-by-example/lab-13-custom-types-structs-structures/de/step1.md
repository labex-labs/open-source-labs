# Strukturen

Es gibt drei Arten von Strukturen („structs“), die mit dem Schlüsselwort `struct` erstellt werden können:

- Tupelstrukturen, die im Grunde genommen benannte Tupel sind.
- Die klassischen C-Strukturen
- Einheitsstrukturen, die keine Felder haben und für Generika nützlich sind.

```rust
// Ein Attribut, um Warnungen für nicht genutzten Code zu unterdrücken.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// Eine Einheitsstruktur
struct Unit;

// Eine Tupelstruktur
struct Pair(i32, f32);

// Eine Struktur mit zwei Feldern
struct Point {
    x: f32,
    y: f32,
}

// Strukturen können als Felder einer anderen Struktur wiederverwendet werden
struct Rectangle {
    // Ein Rechteck kann durch die Position der oberen linken und unteren rechten
    // Ecken im Raum angegeben werden.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // Struktur mit Kurzschreibweise für die Feldinitialisierung erstellen
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Debug-Struktur ausgeben
    println!("{:?}", peter);

    // Ein `Point` instanziieren
    let point: Point = Point { x: 10.3, y: 0.4 };

    // Auf die Felder des Punktes zugreifen
    println!("Punktkoordinaten: ({}, {})", point.x, point.y);

    // Einen neuen Punkt erstellen, indem die Strukturaktualisierungssyntax verwendet wird,
    // um die Felder unseres anderen Punktes zu verwenden
    let bottom_right = Point { x: 5.2,..point };

    // `bottom_right.y` wird dasselbe wie `point.y` sein, da wir dieses Feld
    // von `point` verwendet haben
    println!("zweiter Punkt: ({}, {})", bottom_right.x, bottom_right.y);

    // Den Punkt mit einer `let`-Bindung zerstrukturieren
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // Die Strukturinstantiierung ist auch ein Ausdruck
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Eine Einheitsstruktur instanziieren
    let _unit = Unit;

    // Eine Tupelstruktur instanziieren
    let pair = Pair(1, 0.1);

    // Auf die Felder einer Tupelstruktur zugreifen
    println!("pair enthält {:?} und {:?}", pair.0, pair.1);

    // Eine Tupelstruktur zerstrukturieren
    let Pair(integer, decimal) = pair;

    println!("pair enthält {:?} und {:?}", integer, decimal);
}
```

## Aktivität

1. Fügen Sie eine Funktion `rect_area` hinzu, die die Fläche eines `Rectangle` berechnet (versuchen Sie, geschachtelte Zerstückelung zu verwenden).
2. Fügen Sie eine Funktion `square` hinzu, die einen `Point` und einen `f32` als Argumente nimmt und ein `Rectangle` zurückgibt, dessen obere linke Ecke an diesem Punkt liegt und dessen Breite und Höhe entsprechend dem `f32` sind.
