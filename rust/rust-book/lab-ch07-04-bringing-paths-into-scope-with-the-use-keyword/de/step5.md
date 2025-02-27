# Externe Pakete verwenden

Im zweiten Kapitel haben wir ein Zahlenratespielprojekt programmiert, bei dem wir ein externes Paket namens `rand` verwendet haben, um Zufallszahlen zu erhalten. Um `rand` in unserem Projekt zu verwenden, haben wir diese Zeile in `Cargo.toml` hinzugefügt:

Dateiname: `Cargo.toml`

```tomltoml
rand = "0.8.5"
```

Das Hinzufügen von `rand` als Abhängigkeit in `Cargo.toml` veranlasst Cargo, das `rand`-Paket und alle Abhängigkeiten von *https://crates.io* herunterzuladen und `rand` unserem Projekt zur Verfügung zu stellen.

Dann, um die `rand`-Definitionen in den Gültigkeitsbereich unseres Pakets zu bringen, haben wir eine `use`-Zeile hinzugefügt, die mit dem Namen des Crates, `rand`, beginnt, und die Elemente aufgelistet, die wir in den Gültigkeitsbereich bringen wollten. Denken Sie daran, dass wir im Abschnitt "Generating a Random Number" das `Rng`-Trait in den Gültigkeitsbereich gebracht und die `rand::thread_rng`-Funktion aufgerufen haben:

```rust
use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=100);
}
```

Mitglieder der Rust-Community haben viele Pakete auf *https://crates.io* zur Verfügung gestellt, und das Einbinden eines beliebigen davon in Ihr Paket erfordert dieselben Schritte: Es wird in der `Cargo.toml`-Datei Ihres Pakets aufgelistet und `use` verwendet, um Elemente aus ihren Crates in den Gültigkeitsbereich zu bringen.

Beachten Sie, dass die Standardbibliothek `std` ebenfalls ein Crate ist, das extern zu unserem Paket ist. Da die Standardbibliothek mit der Rust-Sprache ausgeliefert wird, müssen wir `Cargo.toml` nicht ändern, um `std` einzuschließen. Aber wir müssen sie mit `use` referenzieren, um Elemente von dort in den Gültigkeitsbereich unseres Pakets zu bringen. Beispielsweise würden wir für `HashMap` diese Zeile verwenden:

```rust
use std::collections::HashMap;
```

Dies ist ein absoluter Pfad, der mit `std` beginnt, dem Namen des Crates der Standardbibliothek.
