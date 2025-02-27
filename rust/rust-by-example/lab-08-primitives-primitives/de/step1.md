# Primitivdatentypen

Rust bietet Zugang zu einer Vielzahl von `Primitivdatentypen`. Ein Beispiel ist:

## Skalarwerte

- Vorzeichenbehaftete Ganzzahlen: `i8`, `i16`, `i32`, `i64`, `i128` und `isize` (Zeigergröße)
- Vorzeichenlose Ganzzahlen: `u8`, `u16`, `u32`, `u64`, `u128` und `usize` (Zeigergröße)
- Gleitkommazahlen: `f32`, `f64`
- `char` Unicode-Skalarwerte wie `'a'`, `'α'` und `'∞'` (jeweils 4 Bytes)
- `bool` entweder `true` oder `false`
- Der Einheitstyp `()`, dessen einzig möglicher Wert ein leeres Tupel ist: `()`

Trotz des Werts eines Einheitstyps ist es ein Tupel, wird er nicht als zusammengesetzter Typ betrachtet, da er keine mehreren Werte enthält.

## Zusammengesetzte Typen

- Arrays wie `[1, 2, 3]`
- Tupel wie `(1, true)`

Variablen können immer _typannotiert_ werden. Zahlen können zusätzlich über einen _Suffix_ oder _standardmäßig_ annotiert werden. Ganzzahlen haben standardmäßig den Typ `i32` und Gleitkommazahlen den Typ `f64`. Beachten Sie, dass Rust auch Typen aus dem Kontext ableiten kann.

```rust
fn main() {
    // Variablen können typannotiert werden.
    let logisch: bool = true;

    let eine_flaechenzahl: f64 = 1.0;  // Regelmäßige Annotation
    let eine_ganzzahl   = 5i32; // Suffix-Annotation

    // Oder ein Standardwert wird verwendet.
    let standard_flaechenzahl   = 3.0; // `f64`
    let standard_ganzzahl = 7;   // `i32`

    // Ein Typ kann auch aus dem Kontext abgeleitet werden.
    let mut abgeleiteter_typ = 12; // Typ i64 wird aus einer anderen Zeile abgeleitet.
    abgeleiteter_typ = 4294967296i64;

    // Der Wert einer mutablen Variablen kann geändert werden.
    let mut mutabel = 12; // Mutabler `i32`
    mutabel = 21;

    // Fehler! Der Typ einer Variablen kann nicht geändert werden.
    mutabel = true;

    // Variablen können mit Shadowing überschrieben werden.
    let mutabel = true;
}
```
