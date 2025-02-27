# Einen Tipp verarbeiten

Der erste Teil des Ratespielprogramms wird den Benutzer nach Eingaben fragen, diese verarbeiten und überprüfen, ob die Eingabe in der erwarteten Form vorliegt. Zunächst erlauben wir es dem Spieler, einen Tipp abzugeben. Geben Sie den Code in Listing 2-1 in `src/main.rs` ein.

Dateiname: `src/main.rs`

```rust
use std::io;

fn main() {
    println!("Rate die Zahl!");

    println!("Bitte geben Sie Ihren Tipp ein.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Fehler beim Lesen der Zeile");

    println!("Ihr Tipp war: {guess}");
}
```

Listing 2-1: Code, der einen Tipp vom Benutzer erhält und ihn ausgibt

Dieser Code enthält eine Menge Informationen, also gehen wir Zeile für Zeile durch ihn. Um Benutzer-Eingaben zu erhalten und das Ergebnis dann als Ausgabe auszugeben, müssen wir die `io`-Eingabe/Ausgabe-Bibliothek in den Gültigkeitsbereich bringen. Die `io`-Bibliothek stammt aus der Standardbibliothek, die als `std` bekannt ist:

```rust
use std::io;
```

Standardmäßig hat Rust eine Reihe von Elementen, die in der Standardbibliothek definiert sind und die in den Gültigkeitsbereich jedes Programms gebracht werden. Diese Menge wird als _Prelude_ bezeichnet, und Sie können alles darin unter *https://doc.rust-lang.org/std/prelude/index.html* sehen.

Wenn ein Typ, den Sie verwenden möchten, nicht im Prelude vorhanden ist, müssen Sie diesen Typ mit einem `use`-Statement explizit in den Gültigkeitsbereich bringen. Die Verwendung der `std::io`-Bibliothek bietet Ihnen eine Reihe nützlicher Funktionen, einschließlich der Möglichkeit, Benutzer-Eingaben zu akzeptieren.

Wie Sie im ersten Kapitel gesehen haben, ist die `main`-Funktion der Einstiegspunkt in das Programm:

```rust
fn main() {
```

Die `fn`-Syntax deklariert eine neue Funktion; die Klammern `()` geben an, dass keine Parameter vorhanden sind; und die geschweifte Klammer `{` startet den Funktionskörper.

Wie Sie auch im ersten Kapitel gelernt haben, ist `println!` eine Makro, das einen String auf dem Bildschirm ausgibt:

```rust
println!("Rate die Zahl!");

println!("Bitte geben Sie Ihren Tipp ein.");
```

Dieser Code gibt eine Aufforderung aus, die angibt, was das Spiel ist, und fordert die Benutzer-Eingabe an.
