# Code mit loop wiederholen

Das Schlüsselwort `loop` sagt Rust, einen Codeblock ewig wiederholt auszuführen oder bis Sie es explizit zum Stoppen auffordern.

Als Beispiel ändern Sie die Datei `src/main.rs` im Verzeichnis `loops` so, dass sie wie folgt aussieht:

Dateiname: `src/main.rs`

```rust
fn main() {
    loop {
        println!("again!");
    }
}
```

Wenn wir dieses Programm ausführen, werden wir `again!` kontinuierlich wiederholt ausgegeben, bis wir das Programm manuell beenden. Die meisten Terminals unterstützen die Tastenkombination ctrl-C, um ein in einer Dauerschleife hängen gebliebenes Programm abzubrechen. Probieren Sie es aus:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s
     Running `target/debug/loops`
again!
again!
again!
again!
^Cagain!
```

Das Symbol `^C` repräsentiert den Punkt, an dem Sie ctrl-C gedrückt haben. Je nachdem, wo der Code in der Schleife war, als er das Interrupt-Signal erhielt, können Sie `again!` nach dem `^C` oder nicht sehen.

Glücklicherweise bietet Rust auch eine Möglichkeit, eine Schleife mit Code zu verlassen. Sie können das Schlüsselwort `break` innerhalb der Schleife platzieren, um dem Programm anzuzeigen, wann es die Schleife beenden soll. Denken Sie daran, dass wir das in das Ratespiel in "Beenden nach einem richtigen Rat" getan haben, um das Programm zu beenden, wenn der Benutzer das richtige Ergebnis erraten hat.

Wir haben auch `continue` im Ratespiel verwendet, was in einer Schleife dem Programm sagt, den Rest des Codes in dieser Schleifeniteration zu überspringen und zur nächsten Iteration zu gehen.
