# Display

`fmt::Debug` sieht kaum kompakt und sauber aus, daher ist es oft vorteilhaft, das Ausgabeverhalten anzupassen. Dies wird durch die manuelle Implementierung von `fmt::Display` erreicht, das das `{}`-Ausgabemarkierungszeichen verwendet. Die Implementierung sieht so aus:

```rust
// Importiere (über `use`) das `fmt`-Modul, um es verfügbar zu machen.
use std::fmt;

// Definiere eine Struktur, für die `fmt::Display` implementiert werden soll. Dies ist
// eine Tuple-Struktur namens `Structure`, die eine `i32` enthält.
struct Structure(i32);

// Um das `{}`-Zeichen zu verwenden, muss das `fmt::Display`-Trait
// manuell für den Typ implementiert werden.
impl fmt::Display for Structure {
    // Dieses Trait erfordert `fmt` mit dieser genauen Signatur.
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Schreibe genau das erste Element in den bereitgestellten Ausgabestream: `f`. Gibt `fmt::Result` zurück, das angibt, ob die Operation erfolgreich war oder fehlgeschlagen ist. Beachte, dass `write!` eine Syntax verwendet, die sehr ähnlich zu `println!` ist.
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` kann möglicherweise sauberer aussehen als `fmt::Debug`, aber dies stellt ein Problem für die `std`-Bibliothek dar. Wie sollten ambiguöse Typen dargestellt werden? Beispielsweise, wenn die `std`-Bibliothek eine einheitliche Darstellung für alle `Vec<T>` implementierte, welche Darstellung sollte es sein? Würde es eine dieser beiden sein?

- `Vec<path>`: `/:/etc:/home/username:/bin` (getrennt durch `:`)
- `Vec<number>`: `1,2,3` (getrennt durch `,`)

Nein, denn es gibt keine ideale Darstellung für alle Typen und die `std`-Bibliothek macht keine Prätention, eine festzulegen. `fmt::Display` ist für `Vec<T>` oder für andere generische Container nicht implementiert. Für diese generischen Fälle muss daher `fmt::Debug` verwendet werden.

Dies ist jedoch kein Problem, da für jede neue _Container_-Struktur, die _nicht_ generisch ist, `fmt::Display` implementiert werden kann.

```rust
use std::fmt; // Importiere `fmt`

// Eine Struktur, die zwei Zahlen enthält. `Debug` wird abgeleitet, damit die Ergebnisse
// mit `Display` verglichen werden können.
#[derive(Debug)]
struct MinMax(i64, i64);

// Implementiere `Display` für `MinMax`.
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Verwende `self.number`, um auf jedes positionale Datenpunkt zu verweisen.
        write!(f, "({}, {})", self.0, self.1)
    }
}

// Definiere eine Struktur, bei der die Felder benannt werden können, um einen Vergleich zu ermöglichen.
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// Entsprechend implementiere `Display` für `Point2D`.
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Anpassen, sodass nur `x` und `y` angegeben werden.
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("Vergleiche Strukturen:");
    println!("Display: {}", minmax);
    println!("Debug: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("Der große Bereich ist {big} und der kleine ist {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("Vergleiche Punkte:");
    println!("Display: {}", point);
    println!("Debug: {:?}", point);

    // Fehler. Sowohl `Debug` als auch `Display` wurden implementiert, aber `{:b}`
    // erfordert die Implementierung von `fmt::Binary`. Dies wird nicht funktionieren.
    // println!("Wie sieht Point2D in binär aus: {:b}?", point);
}
```

Somit wurde `fmt::Display` implementiert, aber `fmt::Binary` nicht und kann daher nicht verwendet werden. `std::fmt` hat viele solche `Traits`, und jedes erfordert seine eigene Implementierung. Dies wird in `std::fmt` weiter ausgeführt.

## Aktivität

Nachdem du die Ausgabe des obigen Beispiels überprüft hast, verwende die `Point2D`-Struktur als Leitfaden, um der Beispiel eine `Complex`-Struktur hinzuzufügen. Wenn sie auf die gleiche Weise gedruckt wird, sollte die Ausgabe wie folgt sein:

```txt
Display: 3.3 + 7.2i
Debug: Complex { real: 3.3, imag: 7.2 }
```
