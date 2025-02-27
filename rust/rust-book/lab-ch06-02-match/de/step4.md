# Matches sind erschöpfend

Es gibt noch einen anderen Aspekt von `match`, über den wir sprechen müssen: Die Muster der Arme müssen alle Möglichkeiten abdecken. Betrachten Sie diese Version unserer `plus_one`-Funktion, die einen Fehler hat und nicht kompilieren wird:

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

Wir haben den `None`-Fall nicht behandelt, sodass dieser Code einen Fehler verursachen wird. Zum Glück ist es ein Fehler, den Rust erkennen kann. Wenn wir diesen Code versuchen, zu kompilieren, erhalten wir diesen Fehler:

```bash
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |         match x {
  |               ^ pattern `None` not covered
  |
  note: `Option<i32>` defined here
      = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding
a match arm with a wildcard pattern or an explicit pattern as
shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |
```

Rust weiß, dass wir nicht jede mögliche Möglichkeit abgedeckt haben und sogar weiß, welches Muster wir vergessen haben! Matches in Rust sind _erschöpfend_: Wir müssen jede letzte Möglichkeit erschöpfen, damit der Code gültig ist. Vor allem im Fall von `Option<T>`, wenn Rust uns daran hindert, zu vergessen, den `None`-Fall explizit zu behandeln, schützt es uns davor, anzunehmen, dass wir einen Wert haben, wenn wir möglicherweise null haben, und macht somit den früher diskutierten Fehler in Milliardenhöhe unmöglich.
