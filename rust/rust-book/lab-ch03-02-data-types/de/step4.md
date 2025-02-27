# Gleitkommazahlen

Rust hat auch zwei primitive Datentypen für _Gleitkommazahlen_, das sind Zahlen mit Dezimalpunkt. Rusts Gleitkommazahlen sind `f32` und `f64`, die jeweils 32 Bit und 64 Bit groß sind. Der Standardtyp ist `f64`, da es auf modernen CPUs ungefähr die gleiche Geschwindigkeit wie `f32` hat, aber höhere Genauigkeit aufweist. Alle Gleitkommazahlen sind vorzeichenbehaftet.

Erstellen Sie ein neues Projekt namens `data-types`:

```bash
cargo new data-types
cd data-types
```

Hier ist ein Beispiel, das Gleitkommazahlen in Aktion zeigt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
}
```

Gleitkommazahlen werden gemäß der IEEE-754-Norm dargestellt. Der Typ `f32` ist ein einfache Genauigkeit Float, und `f64` hat doppelter Genauigkeit.
