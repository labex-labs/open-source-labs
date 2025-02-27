# Leistung von Code mit Generics

Sie könnten sich fragen, ob es einen Laufzeitaufwand gibt, wenn Sie generische Typparameter verwenden. Die gute Nachricht ist, dass das Verwenden von generischen Typen Ihren Programm nicht langsamer laufen lässt als es mit konkreten Typen wäre.

Rust erreicht dies, indem es die Monomorphisierung des Codes mit Generics zur Compile-Zeit durchführt. _Monomorphisierung_ ist der Prozess, bei dem generischer Code in spezifischen Code umgewandelt wird, indem die konkreten Typen eingefüllt werden, die bei der Kompilierung verwendet werden. In diesem Prozess macht der Compiler das Gegenteil der Schritte, die wir verwendet haben, um die generische Funktion in Listing 10-5 zu erstellen: Der Compiler betrachtet alle Stellen, an denen generischer Code aufgerufen wird, und generiert Code für die konkreten Typen, mit denen der generische Code aufgerufen wird.

Schauen wir uns an, wie dies funktioniert, indem wir das generische `Option<T>`-Enum der Standardbibliothek verwenden:

```rust
let integer = Some(5);
let float = Some(5.0);
```

Wenn Rust diesen Code kompiliert, führt es die Monomorphisierung durch. Während dieses Prozesses liest der Compiler die Werte, die in `Option<T>`-Instanzen verwendet wurden, und identifiziert zwei Arten von `Option<T>`: eine ist `i32` und die andere ist `f64`. Daher erweitert es die generische Definition von `Option<T>` in zwei Definitionen, die auf `i32` und `f64` spezialisiert sind, und ersetzt damit die generische Definition mit den spezifischen.

Die monomorphe Version des Codes sieht ähnlich wie folgend aus (der Compiler verwendet andere Namen als die hier verwendeten, um die Verdeutlichung zu erleichtern):

Dateiname: `src/main.rs`

```rust
enum Option_i32 {
    Some(i32),
    None,
}

enum Option_f64 {
    Some(f64),
    None,
}

fn main() {
    let integer = Option_i32::Some(5);
    let float = Option_f64::Some(5.0);
}
```

Das generische `Option<T>` wird durch die spezifischen Definitionen ersetzt, die der Compiler erstellt hat. Da Rust generischen Code in Code kompiliert, der den Typ in jeder Instanz angibt, haben wir keinen Laufzeitaufwand für das Verwenden von Generics. Wenn der Code läuft, verhält er sich genauso wie wenn wir jede Definition manuell dupliziert hätten. Der Prozess der Monomorphisierung macht Rusts Generics extrem effizient zur Laufzeit.
