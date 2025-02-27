# Ermöglichen mehrerer Vermutungen mit Schleifen

Das `loop`-Schlüsselwort erstellt eine Endlosschleife. Wir werden eine Schleife hinzufügen, um den Benutzern mehr Chancen zu geben, die Zahl zu erraten:

Dateiname: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = guess
         .trim()
         .parse()
         .expect("Please type a number!");

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }
}
```

Wie Sie sehen können, haben wir alles ab dem Eingabeaufforderung für die Vermutung in eine Schleife verschoben. Stellen Sie sicher, dass Sie die Zeilen innerhalb der Schleife jeweils um weitere vier Leerzeichen einrücken und das Programm erneut ausführen. Das Programm wird jetzt für immer nach einer weiteren Vermutung fragen, was tatsächlich ein neues Problem aufwirft. Es scheint, dass der Benutzer nicht beenden kann!

Der Benutzer könnte immer den Programmablauf mit der Tastenkombination ctrl-C unterbrechen. Aber es gibt auch eine andere Möglichkeit, diesem unersättlichen Monster zu entkommen, wie in der `parse`-Diskussion in "Vergleichen der Vermutung mit der Geheimzahl" erwähnt: Wenn der Benutzer eine nicht-numerische Antwort eingibt, wird das Programm abstürzen. Wir können uns darauf verlassen, um dem Benutzer die Möglichkeit zu geben, das Spiel zu beenden, wie hier gezeigt:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
quit
thread'main' panicked at 'Please type a number!: ParseIntError
{ kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Beim Tippen von `quit` wird das Spiel beendet, aber wie Sie bemerken werden, wird dies auch bei der Eingabe jeder anderen nicht-numerischen Eingabe passieren. Dies ist zumindest suboptimal; wir möchten, dass das Spiel auch stoppt, wenn die richtige Zahl erraten wird.
