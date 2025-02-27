# Neue Namen mit dem `as`-Schlüsselwort angeben

Es gibt eine weitere Lösung für das Problem, zwei Typen mit demselben Namen mit `use` in denselben Gültigkeitsbereich zu bringen: Nach dem Pfad können wir `as` und einen neuen lokalen Namen, oder _Alias_, für den Typ angeben. Listing 7-16 zeigt eine andere Möglichkeit, den Code aus Listing 7-15 zu schreiben, indem wir einen der beiden `Result`-Typen mit `as` umbenennen.

Dateiname: `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Listing 7-16: Ein Typ umbenennen, wenn er mit dem `as`-Schlüsselwort in den Gültigkeitsbereich gebracht wird

In der zweiten `use`-Anweisung haben wir für den `std::io::Result`-Typ den neuen Namen `IoResult` gewählt, der nicht mit dem `Result` aus `std::fmt` kollidieren wird, das wir ebenfalls in den Gültigkeitsbereich gebracht haben. Listing 7-15 und Listing 7-16 gelten als idiomatisch, also ist die Wahl Ihnen überlassen!
