# Strukturzerlegung von Enums

Wir haben in diesem Buch Enums strukturiert (z.B. Listing 6-5), aber wir haben bisher noch nicht explizit diskutiert, dass das Muster zur Strukturzerlegung eines Enums der Art entspricht, wie die darin gespeicherten Daten definiert sind. Als Beispiel verwenden wir in Listing 18-15 das `Message`-Enum aus Listing 6-2 und schreiben einen `match` mit Mustern, die jedes innere Element strukturieren werden.

Dateiname: `src/main.rs`

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
  1 let msg = Message::ChangeColor(0, 160, 255);

    match msg {
      2 Message::Quit => {
            println!(
                "Der Quit-Variante gibt es keine Daten, die strukturiert werden könnten."
            );
        }
      3 Message::Move { x, y } => {
            println!(
                "Bewegung in x-Richtung {x}, in y-Richtung {y}"
            );
        }
      4 Message::Write(text) => {
            println!("Textnachricht: {text}");
        }
      5 Message::ChangeColor(r, g, b) => println!(
            "Farbe ändern zu rot {r}, grün {g} und blau {b}"
        ),
    }
}
```

Listing 18-15: Strukturzerlegung von Enum-Varianten, die verschiedene Arten von Werten enthalten

Dieser Code wird `Farbe ändern zu rot 0, grün 160 und blau 255` ausgeben. Versuche, den Wert von `msg` \[1\] zu ändern, um den Code aus den anderen Armen auszuführen.

Für Enum-Varianten ohne Daten, wie `Message::Quit` \[2\], können wir den Wert nicht weiter strukturieren. Wir können nur auf den Literalwert `Message::Quit` abgleichen, und in diesem Muster sind keine Variablen enthalten.

Für struct-ähnliche Enum-Varianten, wie `Message::Move` \[3\], können wir ein Muster verwenden, das ähnlich dem Muster ist, das wir verwenden, um Structs abzugleichen. Nach dem Variantenamen setzen wir geschweifte Klammern und listen dann die Felder mit Variablen auf, sodass wir die Teile auseinandernehmen, um sie im Code für diesen Arm zu verwenden. Hier verwenden wir die Abkürzung wie in Listing 18-13.

Für tuple-ähnliche Enum-Varianten, wie `Message::Write`, die ein Tuple mit einem Element enthält \[4\], und `Message::ChangeColor`, die ein Tuple mit drei Elementen enthält \[5\], ist das Muster ähnlich dem Muster, das wir verwenden, um Tuples abzugleichen. Die Anzahl der Variablen im Muster muss der Anzahl der Elemente in der Variante entsprechen, auf die wir abgleichen.
