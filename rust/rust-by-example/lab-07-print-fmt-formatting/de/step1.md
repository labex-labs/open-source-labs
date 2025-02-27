# Formatierung

Wir haben gesehen, dass die Formatierung über einen _Formatstring_ angegeben wird:

- `format!("{}", foo)` -> `"3735928559"`
- `format!("0x{:X}", foo)` -> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -> `"0o33653337357"`

Die gleiche Variable (`foo`) kann je nach verwendetem _Argumenttyp_ unterschiedlich formatiert werden: `X` gegenüber `o` gegenüber _nicht spezifiziert_.

Diese Formatierungsfunktionalität wird über Traits implementiert, und es gibt für jeden Argumenttyp einen Trait. Der am häufigsten verwendete Formatierungs-Trait ist `Display`, der Fälle behandelt, in denen der Argumenttyp nicht spezifiziert ist: `{}` beispielsweise.

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Breitengrad
    lat: f32,
    // Längengrad
    lon: f32,
}

impl Display for City {
    // `f` ist ein Puffer, und diese Methode muss die formattierte Zeichenkette darin schreiben.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` ist wie `format!`, aber es schreibt die formattierte Zeichenkette
        // in einen Puffer (das erste Argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Wechseln Sie dies zu {}, nachdem Sie eine Implementierung
        // für fmt::Display hinzugefügt haben.
        println!("{:?}", color);
    }
}
```

Sie können eine vollständige Liste der Formatierungs-Traits und ihrer Argumenttypen in der `std::fmt`-Dokumentation ansehen.

## Aktivität

Fügen Sie eine Implementierung des `fmt::Display`-Traits für die obige `Color`-Strukt hinzu, sodass die Ausgabe wie folgt aussieht:

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

Drei Tipps, falls Sie in Schwierigkeiten geraten:

- Die Formel zur Berechnung einer Farbe im RGB-Farbraum lautet: `RGB = (R*65536)+(G*256)+B, (wenn R ROT, G GRÜN und B BLAU ist)`. Weitere Informationen finden Sie unter RGB-Farformat & Berechnung.
- Sie können jede Farbe möglicherweise mehrmals auflisten.
- Sie können mit Nullen auf eine Breite von 2 auffüllen mit `:0>2`.
