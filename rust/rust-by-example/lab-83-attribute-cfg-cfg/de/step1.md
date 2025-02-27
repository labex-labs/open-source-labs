# `cfg`

Konfigurationsbedingte Prüfungen sind über zwei verschiedene Operatoren möglich:

- das `cfg`-Attribut: `#[cfg(...)]` an Attributposition
- das `cfg!`-Makro: `cfg!(...)` in booleschen Ausdrücken

Während das erstere die bedingte Kompilierung ermöglicht, wird das letztere bedingt zu `true` oder `false`-Literalen ausgewertet, was Prüfungen zur Laufzeit ermöglicht. Beide verwenden die gleiche Argumentsyntax.

Im Gegensatz zu `#[cfg]` entfernt `cfg!` keinen Code und wertet nur zu `true` oder `false` aus. Beispielsweise müssen alle Blöcke in einem if/else-Ausdruck gültig sein, wenn `cfg!` für die Bedingung verwendet wird, unabhängig davon, was `cfg!` auswertet.

```rust
// Diese Funktion wird nur kompiliert, wenn das Zielbetriebssystem linux ist
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// Und diese Funktion wird nur kompiliert, wenn das Zielbetriebssystem *nicht* linux ist
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!");
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}
```
