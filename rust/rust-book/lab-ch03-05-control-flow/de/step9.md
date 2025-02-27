# Bedingte Schleifen mit while

Ein Programm muss oft eine Bedingung innerhalb einer Schleife计算评估. Solange die Bedingung `true` ist, läuft die Schleife. Wenn die Bedingung nicht mehr `true` ist, ruft das Programm `break` auf und stoppt die Schleife. Es ist möglich, ein solches Verhalten mit einer Kombination aus `loop`, `if`, `else` und `break` zu implementieren; Sie können das jetzt in einem Programm versuchen, wenn Sie möchten. Dieses Muster ist jedoch so üblich, dass Rust eine integrierte Sprachkonstruktion dafür hat, die `while`-Schleife. In Listing 3-3 verwenden wir `while`, um das Programm drei Mal zu durchlaufen, jedes Mal herunter zu zählen, und dann, nachdem die Schleife beendet ist, eine Nachricht auszugeben und das Programm zu beenden.

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut number = 3;

    while number!= 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

Listing 3-3: Verwendung einer `while`-Schleife, um Code auszuführen, solange eine Bedingung `true` ist

Dieser Aufbau vermeidet eine Menge Verschachtelungen, die erforderlich wären, wenn Sie `loop`, `if`, `else` und `break` verwenden, und er ist klarer. Solange eine Bedingung `true` ist, läuft der Code; andernfalls bricht er die Schleife ab.
