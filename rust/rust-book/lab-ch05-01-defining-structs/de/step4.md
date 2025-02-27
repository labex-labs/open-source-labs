# Verwendung von Tuple Structs ohne benannte Felder, um verschiedene Typen zu erstellen

Rust unterstützt auch Structs, die ähnlich wie Tuples aussehen, sogenannte _Tuple Structs_. Tuple Structs haben die zusätzliche Bedeutung, die der Struct-Name bietet, aber haben keine Namen, die mit ihren Feldern assoziiert sind; stattdessen haben sie nur die Typen der Felder. Tuple Structs sind nützlich, wenn Sie dem gesamten Tuple einen Namen geben möchten und das Tuple einen anderen Typ als andere Tuples machen möchten, und wenn das Benennen jedes Felds wie in einem normalen Struct umständlich oder redundant wäre.

Um einen Tuple Struct zu definieren, beginnen Sie mit dem Schlüsselwort `struct` und dem Struct-Namen, gefolgt von den Typen im Tuple. Beispielsweise definieren und verwenden wir hier zwei Tuple Structs namens `Color` und `Point`:

Dateiname: `src/main.rs`

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Beachte, dass die `black`- und `origin`-Werte unterschiedliche Typen sind, weil sie Instanzen unterschiedlicher Tuple Structs sind. Jeder Struct, den Sie definieren, ist ein eigener Typ, auch wenn die Felder innerhalb des Structs möglicherweise die gleichen Typen haben. Beispielsweise kann eine Funktion, die einen Parameter vom Typ `Color` annimmt, keinen `Point` als Argument akzeptieren, auch wenn beide Typen aus drei `i32`-Werten bestehen. Andernfalls sind Tuple Struct-Instanzen ähnlich wie Tuples, in dem Sie sie in ihre einzelnen Teile zerlegen können, und Sie können ein `.` gefolgt von dem Index verwenden, um einen einzelnen Wert zuzugreifen.
