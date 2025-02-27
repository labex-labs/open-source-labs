# Refactoring mit Tupeln

Listing 5-9 zeigt eine andere Version unseres Programms, das Tupel verwendet.

Dateiname: `src/main.rs`

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "Die Fläche des Rechtecks beträgt {} Quadratpixel.",
      1 area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
  2 dimensions.0 * dimensions.1
}
```

Listing 5-9: Angabe der Breite und Höhe des Rechtecks mit einem Tupel

Auf eine Weise ist dieses Programm besser. Tupel erlauben es uns, etwas Struktur hinzuzufügen, und wir übergeben jetzt nur einen Argument \[1\]. Aber auf eine andere Weise ist diese Version weniger klar: Tupel benennen ihre Elemente nicht, sodass wir in die Teile des Tupels indexieren müssen \[2\], was unsere Berechnung weniger offensichtlich macht.

Das Vertauschen von Breite und Höhe würde für die Flächenberechnung keine Rolle spielen, aber wenn wir das Rechteck auf dem Bildschirm zeichnen möchten, würde es eine Rolle spielen! Wir müssten dann im Kopf behalten, dass `width` der Tupelindex `0` ist und `height` der Tupelindex `1` ist. Es wäre noch schwieriger für jemanden anderen, das herauszufinden und sich zu merken, wenn er unseren Code verwenden würde. Da wir die Bedeutung unserer Daten in unserem Code nicht vermittelt haben, ist es jetzt einfacher, Fehler zu machen.
