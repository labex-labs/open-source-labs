# Typanonymität

Closures fangen Variablen aus umgebenden Gültigkeitsbereichen präzise ein. Hat das irgendwelche Auswirkungen? Sicherlich. Betrachten Sie, wie die Verwendung eines Closures als Funktionsparameter \[Generics\] erfordert, was notwendig ist, aufgrund ihrer Definition:

```rust
// `F` muss generisch sein.
fn apply<F>(f: F) where
    F: FnOnce() {
    f();
}
```

Wenn ein Closure definiert wird, erstellt der Compiler implizit eine neue anonyme Struktur, um die eingefangenen Variablen darin zu speichern, und implementiert gleichzeitig die Funktionalität über einen der `Traits`: `Fn`, `FnMut` oder `FnOnce` für diesen unbekannten Typ. Dieser Typ wird der Variablen zugewiesen, die bis zum Aufruf gespeichert wird.

Da dieser neue Typ vom unbekannten Typ ist, erfordert jede Verwendung in einer Funktion Generics. Allerdings wäre ein unbeschränkter Typparameter `<T>` immer noch mehrdeutig und nicht erlaubt. Daher reicht die Begrenzung durch einen der `Traits`: `Fn`, `FnMut` oder `FnOnce` (den es implementiert), um seinen Typ anzugeben.

```rust
// `F` muss `Fn` implementieren für ein Closure, das keine
// Eingaben annimmt und nichts zurückgibt - genau das, was
// für `print` erforderlich ist.
fn apply<F>(f: F) where
    F: Fn() {
    f();
}

fn main() {
    let x = 7;

    // Fange `x` in einen anonymen Typ ein und implementiere
    // `Fn` für ihn. Speichere es in `print`.
    let print = || println!("{}", x);

    apply(print);
}
```
