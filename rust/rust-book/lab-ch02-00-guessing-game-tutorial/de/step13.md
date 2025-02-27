# Generieren einer Zufallszahl

Lassen Sie uns beginnen, `rand` zu verwenden, um eine Zahl zu generieren, die geraten werden soll. Der nächste Schritt ist es, `src/main.rs` zu aktualisieren, wie in Listing 2-3 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::io;
1 use rand::Rng;

fn main() {
    println!("Guess the number!");

  2 let secret_number = rand::thread_rng().gen_range(1..=100);

  3 println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
     .read_line(&mut guess)
     .expect("Failed to read line");

    println!("You guessed: {guess}");
}
```

Listing 2-3: Hinzufügen von Code, um eine Zufallszahl zu generieren

Zuerst fügen wir die Zeile `use rand::Rng;` hinzu \[1\]. Das `Rng`-Trait definiert Methoden, die Zufallszahlengeneratoren implementieren, und dieses Trait muss im Gültigkeitsbereich sein, damit wir diese Methoden verwenden können. Kapitel 10 wird Traits im Detail behandeln.

Als nächstes fügen wir zwei Zeilen in die Mitte hinzu. In der ersten Zeile \[2\] rufen wir die `rand::thread_rng`-Funktion auf, die uns den speziellen Zufallszahlengenerator gibt, den wir verwenden werden: einen, der lokal zum aktuellen Ausführungsthread ist und von dem Betriebssystem initialisiert wird. Dann rufen wir die `gen_range`-Methode auf dem Zufallszahlengenerator auf. Diese Methode wird vom `Rng`-Trait definiert, das wir mit der `use rand::Rng;`-Anweisung in den Gültigkeitsbereich gebracht haben. Die `gen_range`-Methode nimmt einen Bereichsausdruck als Argument und generiert eine Zufallszahl im Bereich. Der Art von Bereichsausdruck, den wir hier verwenden, hat die Form `start..=end` und ist sowohl für die untere als auch für die obere Grenze eingeschlossen, daher müssen wir `1..=100` angeben, um eine Zahl zwischen 1 und 100 zu erhalten.

> Hinweis: Sie werden nicht einfach wissen, welche Traits zu verwenden und welche Methoden und Funktionen aus einer Kiste aufzurufen sind, daher hat jede Kiste eine Dokumentation mit Anweisungen zur Verwendung. Ein weiterer praktischer Aspekt von Cargo ist, dass das Ausführen des Befehls `cargo doc --open` die lokal von allen Ihren Abhängigkeiten bereitgestellte Dokumentation erstellen und in Ihrem Browser öffnen wird. Wenn Sie beispielsweise an anderer Funktionalität in der `rand`-Kiste interessiert sind, führen Sie `cargo doc --open` aus und klicken Sie in der linken Seitenleiste auf `rand`.

Die zweite neue Zeile \[3\] druckt die Geheimzahl. Dies ist nützlich, wenn wir das Programm entwickeln und testen möchten, aber wir werden es in der endgültigen Version löschen. Es ist nicht viel von einem Spiel, wenn das Programm die Antwort sofort ausgibt, wenn es startet!

Versuchen Sie, das Programm ein paar Mal auszuführen:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

Sie sollten verschiedene Zufallszahlen erhalten, und alle sollten Zahlen zwischen 1 und 100 sein. Tolle Arbeit!
