# Behandlung ungültiger Eingaben

Um das Verhalten des Spiels weiter zu verbessern, statt das Programm abzustürzen, wenn der Benutzer eine nicht-numerische Eingabe macht, lassen wir das Spiel ungültige Eingaben ignorieren, sodass der Benutzer weiterhin raten kann. Wir können das erreichen, indem wir die Zeile ändern, in der `guess` von einem `String` in einen `u32` umgewandelt wird, wie in Listing 2-5 gezeigt.

Dateiname: `src/main.rs`

```rust
--snip--

io::stdin()
 .read_line(&mut guess)
 .expect("Failed to read line");

let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};

println!("You guessed: {guess}");

--snip--
```

Listing 2-5: Ignorieren einer nicht-numerischen Vermutung und erneut nach einer Vermutung fragen, anstatt das Programm abzustürzen

Wir wechseln von einem `expect`-Aufruf zu einem `match`-Ausdruck, um von einem Absturz bei einem Fehler zu einem Umgang mit dem Fehler zu gelangen. Denken Sie daran, dass `parse` ein `Result`-Typ zurückgibt und `Result` eine Enumeration ist, die die Varianten `Ok` und `Err` hat. Wir verwenden hier einen `match`-Ausdruck, wie wir es auch bei dem `Ordering`-Ergebnis der `cmp`-Methode getan haben.

Wenn `parse` die Zeichenfolge erfolgreich in eine Zahl umwandeln kann, wird es einen `Ok`-Wert zurückgeben, der die resultierende Zahl enthält. Dieser `Ok`-Wert wird dem Muster des ersten Arms entsprechen, und der `match`-Ausdruck wird einfach den `num`-Wert zurückgeben, den `parse` erzeugt hat und in den `Ok`-Wert gesteckt hat. Diese Zahl wird genau dort landen, wo wir sie in der neuen `guess`-Variable haben wollen, die wir erstellen.

Wenn `parse` die Zeichenfolge _nicht_ in eine Zahl umwandeln kann, wird es einen `Err`-Wert zurückgeben, der weitere Informationen über den Fehler enthält. Der `Err`-Wert stimmt nicht mit dem `Ok(num)`-Muster im ersten `match`-Arm überein, stimmt aber mit dem `Err(_)`-Muster im zweiten Arm überein. Der Unterstrich, `_`, ist ein Platzhalterwert; in diesem Beispiel sagen wir, dass wir alle `Err`-Werte abfangen möchten, unabhängig davon, welche Informationen sie enthalten. Der Programm wird daher den Code des zweiten Arms ausführen, `continue`, was dem Programm sagt, zum nächsten Iterationsschritt der `loop` zu gehen und erneut nach einer Vermutung zu fragen. Effectiv ignoriert das Programm alle Fehler, die `parse` möglicherweise auftauchen kann!

Jetzt sollte alles im Programm wie erwartet funktionieren. Probieren wir es aus:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

Super! Mit einem kleinen letzten Anpassung werden wir das Raten-Spiel abschließen. Denken Sie daran, dass das Programm immer noch die Geheimzahl ausgibt. Das war für das Testen gut, aber es ruiniert das Spiel. Lassen Sie uns die `println!`, die die Geheimzahl ausgibt, löschen. Listing 2-6 zeigt den endgültigen Code.

Dateiname: `src/main.rs`

```rust
use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
         .read_line(&mut guess)
         .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
```

Listing 2-6: Vollständiger Code für das Raten-Spiel

An diesem Punkt haben Sie das Raten-Spiel erfolgreich gebaut. Herzlichen Glückwunsch!
