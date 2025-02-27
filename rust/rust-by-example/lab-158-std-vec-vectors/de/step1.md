# Vektoren

Vektoren sind vergrößerbare Arrays. Wie Slices ist ihre Größe zur Compile-Zeit unbekannt, aber sie können sich jederzeit erweitern oder verkleinern. Ein Vektor wird durch 3 Parameter dargestellt:

- Zeiger auf die Daten
- Länge
- Kapazität

Die Kapazität gibt an, wie viel Speicher für den Vektor reserviert ist. Der Vektor kann sich so lange erweitern, wie die Länge kleiner als die Kapazität ist. Wenn diese Schwelle überschritten werden muss, wird der Vektor mit einer größeren Kapazität neu zugewiesen.

```rust
fn main() {
    // Iteratoren können in Vektoren gesammelt werden
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Gesammelt (0..10) in: {:?}", collected_iterator);

    // Das `vec!`-Makro kann verwendet werden, um einen Vektor zu initialisieren
    let mut xs = vec![1i32, 2, 3];
    println!("Initialer Vektor: {:?}", xs);

    // Füge ein neues Element am Ende des Vektors hinzu
    println!("Füge 4 in den Vektor hinzu");
    xs.push(4);
    println!("Vektor: {:?}", xs);

    // Fehler! Unveränderliche Vektoren können nicht wachsen
    collected_iterator.push(0);
    // FIXME ^ Kommentiere diese Zeile aus

    // Die `len`-Methode liefert die Anzahl der aktuell im Vektor gespeicherten Elemente
    println!("Vektorlänge: {}", xs.len());

    // Der Zugriff erfolgt über eckige Klammern (der Zugriff beginnt bei 0)
    println!("Zweites Element: {}", xs[1]);

    // `pop` entfernt das letzte Element aus dem Vektor und gibt es zurück
    println!("Entferne letztes Element: {:?}", xs.pop());

    // Ein Zugriff außerhalb der Grenzen führt zu einem Absturz
    println!("Viertes Element: {}", xs[3]);
    // FIXME ^ Kommentiere diese Zeile aus

    // Über `Vector`s kann einfach iteriert werden
    println!("Inhalt von xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // Ein `Vector` kann auch iteriert werden, während die Iterationszahl
    // in einer separaten Variable (`i`) aufgelistet wird
    for (i, x) in xs.iter().enumerate() {
        println!("An Position {} haben wir den Wert {}", i, x);
    }

    // Dank `iter_mut` können auch veränderliche `Vector`s iteriert werden,
    // indem jeder Wert modifiziert werden kann
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Aktualisierter Vektor: {:?}", xs);
}
```

Weitere `Vec`-Methoden können im `std::vec`-Modul gefunden werden.
