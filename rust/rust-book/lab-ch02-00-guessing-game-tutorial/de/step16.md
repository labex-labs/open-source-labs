# Beenden nach einem richtigen Rat

Lassen Sie uns das Spiel programmieren, um es zu beenden, wenn der Benutzer gewinnt, indem wir eine `break`-Anweisung hinzufügen:

Dateiname: `src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

Das Hinzufügen der `break`-Zeile nach `You win!` lässt das Programm die Schleife verlassen, wenn der Benutzer die Geheimzahl richtig erraten hat. Das Verlassen der Schleife bedeutet auch, das das Programm beendet wird, da die Schleife der letzte Teil von `main` ist.
