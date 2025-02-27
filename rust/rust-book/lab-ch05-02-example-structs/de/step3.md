# Refactoring mit Structs: Hinzufügen von mehr Bedeutung

Wir verwenden Structs, um Bedeutung hinzuzufügen, indem wir die Daten benennen. Wir können das Tupel, das wir verwenden, in einen Struct umwandeln, der einen Namen für das Ganze sowie Namen für die Teile hat, wie in Listing 5-10 gezeigt.

Dateiname: `src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "Die Fläche des Rechtecks beträgt {} Quadratpixel.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

Listing 5-10: Definition eines `Rectangle`-Structs

Hier haben wir einen Struct definiert und ihn `Rectangle` genannt \[1\]. Innerhalb der geschweiften Klammern haben wir die Felder als `width` und `height` definiert, beide von Typ `u32` \[2\]. Dann haben wir in `main` eine bestimmte Instanz von `Rectangle` erstellt, die eine Breite von `30` und eine Höhe von `50` hat \[3\].

Unsere `area`-Funktion ist jetzt mit einem Parameter definiert, den wir `rectangle` genannt haben, dessen Typ eine unveränderliche Referenz auf eine Struct-`Rectangle`-Instanz ist \[4\]. Wie in Kapitel 4 erwähnt, möchten wir die Struct referenzieren, anstatt die Eigentumsgewalt zu übernehmen. Auf diese Weise behält `main` seine Eigentumsgewalt und kann weiterhin `rect1` verwenden, was der Grund ist, warum wir das `&` in der Funktionssignatur und beim Funktionsaufruf verwenden.

Die `area`-Funktion greift auf die `width`- und `height`-Felder der `Rectangle`-Instanz zu \[5\] (beachten Sie, dass das Zugreifen auf Felder einer referenzierten Struct-Instanz die Feldwerte nicht bewegt, weshalb Sie oft Referenzen auf Structs sehen). Unsere Funktionssignatur für `area` sagt jetzt genau, was wir meinen: Berechnen Sie die Fläche von `Rectangle`, indem Sie seine `width`- und `height`-Felder verwenden. Dies vermittelt, dass Breite und Höhe miteinander zusammenhängen, und es gibt beschreibende Namen für die Werte anstelle von den Tupelindexwerten `0` und `1`. Dies ist ein Gewinn für die Klarheit.
