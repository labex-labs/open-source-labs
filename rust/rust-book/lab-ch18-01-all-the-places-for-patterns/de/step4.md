# while let bedingte Schleifen

Ähnlich aufgebaut wie `if let`, erlaubt die `while let` bedingte Schleife, dass eine `while`-Schleife solange läuft, wie ein Muster weiterhin übereinstimmt. In Listing 18-2 schreiben wir eine `while let`-Schleife, die einen Vektor als Stapel verwendet und die Werte im Vektor in umgekehrter Reihenfolge ausgibt, in der sie hinzugefügt wurden.

Dateiname: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listing 18-2: Verwenden einer `while let`-Schleife, um Werte auszugeben, solange `stack.pop()` `Some` zurückgibt

Dieses Beispiel gibt `3`, `2` und dann `1` aus. Die `pop`-Methode nimmt das letzte Element aus dem Vektor und gibt `Some(value)` zurück. Wenn der Vektor leer ist, gibt `pop` `None` zurück. Die `while`-Schleife führt den Code in ihrem Block solange aus, wie `pop` `Some` zurückgibt. Wenn `pop` `None` zurückgibt, stoppt die Schleife. Wir können `while let` verwenden, um jedes Element von unserem Stapel zu entfernen.
