# Parameter

Wir können Funktionen definieren, die _Parameter_ haben, die spezielle Variablen sind, die Teil der Signatur einer Funktion sind. Wenn eine Funktion Parameter hat, kannst du ihr konkrete Werte für diese Parameter übergeben. Technisch gesehen werden die konkreten Werte als _Argumente_ bezeichnet, aber im alltäglichen Gespräch verwenden die Menschen die Wörter _Parameter_ und _Argument_ im Allgemeinen austauschbar für die Variablen in der Definition einer Funktion oder die konkreten Werte, die beim Aufruf einer Funktion übergeben werden.

In dieser Version von `another_function` fügen wir einen Parameter hinzu:

Dateiname: `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

Versuche, dieses Programm auszuführen; du solltest die folgende Ausgabe erhalten:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

Die Deklaration von `another_function` hat einen Parameter namens `x`. Der Typ von `x` wird als `i32` angegeben. Wenn wir `5` an `another_function` übergeben, setzt die `println!`-Makro `5` an die Stelle, an der die geschweiften Klammern, die `x` enthalten, im Formatstring waren.

In Funktionssignaturen _muss_ du den Typ jedes Parameters deklarieren. Dies ist eine bewusste Entscheidung in der Rust-Designphilosophie: Das Erfordern von Typangaben in Funktionsdefinitionen bedeutet, dass der Compiler fast nie benötigt, dass du sie an anderen Stellen im Code verwendest, um herauszufinden, welchen Typ du meinst. Der Compiler kann auch hilfreichere Fehlermeldungen geben, wenn er weiß, welche Typen die Funktion erwartet.

Wenn du mehrere Parameter definierst, trenne die Parameterdeklarationen mit Kommas, wie folgt:

Dateiname: `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

Dieses Beispiel erstellt eine Funktion namens `print_labeled_measurement` mit zwei Parametern. Der erste Parameter heißt `value` und ist vom Typ `i32`. Der zweite heißt `unit_label` und ist vom Typ `char`. Die Funktion druckt dann Text, der sowohl den `value` als auch das `unit_label` enthält.

Lass uns versuchen, diesen Code auszuführen. Ersetze das aktuelle Programm in der `src/main.rs`-Datei deines _functions_-Projekts durch das vorherige Beispiel und führe es mit `cargo run` aus:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

Da wir die Funktion mit `5` als Wert für `value` und `'h'` als Wert für `unit_label` aufgerufen haben, enthält die Programmausgabe diese Werte.
