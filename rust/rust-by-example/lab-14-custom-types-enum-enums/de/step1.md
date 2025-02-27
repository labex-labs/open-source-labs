# Enums

Das Schlüsselwort `enum` ermöglicht die Erstellung eines Typs, der eine von mehreren verschiedenen Varianten sein kann. Jede Variante, die als `struct` gültig ist, ist auch in einem `enum` gültig.

```rust
// Erstellen Sie ein `enum`, um einen Webeverlauf zu klassifizieren. Beachten Sie, wie sowohl
// Namen als auch Typinformationen zusammen die Variante bestimmen:
// `PageLoad!= PageUnload` und `KeyPress(char)!= Paste(String)`.
// Jede ist unterschiedlich und unabhängig.
enum WebEvent {
    // Eine `enum`-Variante kann entweder `unit-ähnlich` sein,
    PageLoad,
    PageUnload,
    // wie Tupelstrukturen,
    KeyPress(char),
    Paste(String),
    // oder c-ähnliche Strukturen.
    Click { x: i64, y: i64 },
}

// Eine Funktion, die ein `WebEvent`-Enum als Argument nimmt und
// nichts zurückgibt.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("Seite geladen"),
        WebEvent::PageUnload => println!("Seite entladen"),
        // Entpacken Sie `c` aus der `enum`-Variante.
        WebEvent::KeyPress(c) => println!("Gedrückt '{}'.", c),
        WebEvent::Paste(s) => println!("Eingefügt \"{}\".", s),
        // Entpacken Sie `Click` in `x` und `y`.
        WebEvent::Click { x, y } => {
            println!("Geklickt bei x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let gedrueckt = WebEvent::KeyPress('x');
    // `to_owned()` erstellt eine eigene `String` aus einem Stringslice.
    let eingefuegt  = WebEvent::Paste("mein Text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let laden    = WebEvent::PageLoad;
    let entladen  = WebEvent::PageUnload;

    inspect(gedrueckt);
    inspect( eingefuegt);
    inspect(click);
    inspect(laden);
    inspect(entladen);
}
```

## Typaliase

Wenn Sie einen Typalias verwenden, können Sie auf jede Enum-Variante über ihren Alias verweisen. Dies kann nützlich sein, wenn der Name des Enums zu lang oder zu generisch ist und Sie es umbenennen möchten.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// Erstellt einen Typalias
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // Wir können auf jede Variante über ihren Alias, nicht ihren langen und unbequemen
    // Namen verweisen.
    let x = Operations::Add;
}
```

Der häufigste Ort, an dem Sie dies sehen, ist in `impl`-Blöcken, die den `Self`-Alias verwenden.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

Um mehr über Enums und Typaliase zu lernen, können Sie den Stabilisierungsbericht lesen, der von dem Zeitpunkt stammt, an dem diese Funktion in Rust stabilisiert wurde.
