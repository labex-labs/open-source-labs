# Der boolesche Typ

Wie in den meisten anderen Programmiersprachen hat ein boolescher Typ in Rust zwei mögliche Werte: `true` und `false`. Boole'sche Werte haben eine Größe von einem Byte. Der boolesche Typ in Rust wird mit `bool` angegeben. Beispiel:

Dateiname: `src/main.rs`

```rust
fn main() {
    let t = true;

    let f: bool = false; // mit expliziter Typangabe
}
```

Die Hauptweise, boolesche Werte zu verwenden, ist über bedingte Anweisungen wie z. B. einen `if`-Ausdruck. Wir werden im Abschnitt "Steuerfluss" erklären, wie `if`-Ausdrücke in Rust funktionieren.
