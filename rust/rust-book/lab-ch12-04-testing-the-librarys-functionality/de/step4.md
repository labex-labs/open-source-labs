# Iterieren über Zeilen mit der lines-Methode

Rust hat eine hilfreiche Methode, um Zeilenweise-Iteration von Strings zu behandeln, die zweckmäßigerweise `lines` heißt und wie in Listing 12-17 funktioniert. Beachten Sie, dass dies noch nicht kompilieren wird.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // do something with line
    }
}
```

Listing 12-17: Iterieren über jede Zeile in `contents`

Die `lines`-Methode gibt einen Iterator zurück. Wir werden uns im Kapitel 13 im Detail mit Iteratoren befassen, aber erinnern Sie sich daran, dass Sie diese Art des Verwenden eines Iterators in Listing 3-5 gesehen haben, wo wir eine `for`-Schleife mit einem Iterator verwendet haben, um einige Codezeilen auf jedes Element in einer Sammlung auszuführen.
