# Konstanten

Rust hat zwei verschiedene Arten von Konstanten, die in jedem Bereich, einschließlich des globalen Bereichs, deklariert werden können. Beide erfordern eine explizite Typangabe:

- `const`: Ein unveränderbarer Wert (der übliche Fall).
- `static`: Eine möglicherweise `mut`able Variable mit `'static` Lebensdauer. Die statische Lebensdauer wird inferiert und muss nicht angegeben werden. Das Lesen oder Ändern einer mutablen statischen Variable ist `unsafe`.

```rust
// Globale Variablen werden außerhalb aller anderen Bereiche deklariert.
static LANGUAGE: &str = "Rust";
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Konstante in einer Funktion verwenden
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Konstante im Hauptthread verwenden
    println!("Dies ist {}", LANGUAGE);
    println!("Der Schwellenwert ist {}", THRESHOLD);
    println!("{} ist {}", n, if is_big(n) { "groß" } else { "klein" });

    // Fehler! Eine `const` kann nicht geändert werden.
    THRESHOLD = 5;
    // FIXME ^ Kommentieren Sie diese Zeile aus
}
```
