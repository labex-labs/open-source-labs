# Eingabefunktionen

Da Closures als Argumente verwendet werden können, möchtest du vielleicht wissen, ob das auch für Funktionen gilt. Und tatsächlich kann man das sagen! Wenn du eine Funktion deklarierst, die ein Closure als Parameter nimmt, dann kann jede Funktion, die die Merkmalsbindung dieses Closures erfüllt, als Parameter übergeben werden.

```rust
// Definiere eine Funktion, die ein generisches `F`-Argument annimmt,
// das durch `Fn` begrenzt ist, und rufe es auf
fn call_me<F: Fn()>(f: F) {
    f();
}

// Definiere eine Umhüllungsfunktion, die die `Fn`-Begrenzung erfüllt
fn function() {
    println!("Ich bin eine Funktion!");
}

fn main() {
    // Definiere ein Closure, das die `Fn`-Begrenzung erfüllt
    let closure = || println!("Ich bin ein Closure!");

    call_me(closure);
    call_me(function);
}
```

Als zusätzliche Bemerkung bestimmen die `Fn`, `FnMut` und `FnOnce`-`Merkmale`, wie ein Closure Variablen aus dem umgebenden Bereich aufnimmt.
