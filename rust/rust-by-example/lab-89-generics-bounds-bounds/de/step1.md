# Bounds

Wenn Sie mit Generics arbeiten, müssen die Typparameter oft Traits als _Bounds_ verwenden, um festzulegen, welche Funktionalität ein Typ implementiert. Beispielsweise verwendet das folgende Beispiel das `Display`-Trait, um etwas auszugeben, und erfordert daher, dass `T` durch `Display` begrenzt ist; d.h. `T` _muss_ `Display` implementieren.

```rust
// Definiert eine Funktion `printer`, die einen generischen Typ `T` annimmt,
// der das `Display`-Trait implementieren muss.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

Das Begrenzen beschränkt das Generic auf Typen, die den Bounds entsprechen. D.h.:

```rust
struct S<T: Display>(T);

// Fehler! `Vec<T>` implementiert `Display` nicht. Diese
// Spezialisierung wird fehlschlagen.
let s = S(vec![1]);
```

Ein weiterer Effekt des Begrenzens ist, dass generische Instanzen die \[Methoden\] der im Bound angegebenen Traits aufrufen können. Beispielsweise:

```rust
// Ein Trait, das das Druckmarker `{:?}` implementiert.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// Der generische Typ `T` muss `Debug` implementieren. Unabhängig
// vom Typ wird dies korrekt funktionieren.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` muss `HasArea` implementieren. Jeder Typ, der den
// Bound erfüllt, kann die `area`-Funktion von `HasArea` aufrufen.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: Versuchen Sie, diese Zeilen zu aktivieren.
    // | Fehler: Implementiert weder `Debug` noch `HasArea`.
}
```

Als zusätzliche Bemerkung können `where`-Klauseln auch in einigen Fällen verwendet werden, um die Bounds ausdrücklicher anzuwenden.
