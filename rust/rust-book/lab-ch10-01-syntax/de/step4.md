# In Strukturdefinitionen

Wir können auch Strukturen definieren, um einen generischen Typparameter in einem oder mehreren Feldern mit der `<>`-Syntax zu verwenden. Listing 10-6 definiert eine `Point<T>`-Struktur, um `x`- und `y`-Koordinatenwerte beliebigen Typs zu speichern.

Dateiname: `src/main.rs`

```rust
1 struct Point<T> {
  2 x: T,
  3 y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}
```

Listing 10-6: Eine `Point<T>`-Struktur, die `x`- und `y`-Werte vom Typ `T` speichert

Die Syntax für das Verwenden von Generics in Strukturdefinitionen ähnelt der in Funktionsdefinitionen verwendeten. Zunächst deklarieren wir den Namen des Typparameters innerhalb von eckigen Klammern direkt nach dem Namen der Struktur \[1\]. Anschließend verwenden wir den generischen Typ in der Strukturdefinition, wo wir sonst konkrete Datentypen angeben würden \[23\].

Beachten Sie, dass wir nur einen generischen Typ verwendet haben, um `Point<T>` zu definieren. Diese Definition besagt, dass die `Point<T>`-Struktur generisch über einen bestimmten Typ `T` ist und die Felder `x` und `y` _beide_ diesen gleichen Typ sind, unabhängig davon, welcher Typ das ist. Wenn wir eine Instanz von `Point<T>` erstellen, die Werte unterschiedlicher Typen hat, wie in Listing 10-7, wird unser Code nicht kompilieren.

Dateiname: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let wont_work = Point { x: 5, y: 4.0 };
}
```

Listing 10-7: Die Felder `x` und `y` müssen den gleichen Typ haben, da beide den gleichen generischen Datentyp `T` haben.

In diesem Beispiel, wenn wir den ganzzahligen Wert `5` für `x` zuweisen, informieren wir den Compiler, dass der generische Typ `T` für diese Instanz von `Point<T>` ein ganzzahliger Typ sein wird. Wenn wir dann `4.0` für `y` angeben, das wir als gleichen Typ wie `x` definiert haben, erhalten wir einen Typenfehler wie diesen:

```bash
error[E0308]: mismatched types
 --> src/main.rs:7:38
  |
7 |     let wont_work = Point { x: 5, y: 4.0 };
  |                                      ^^^ expected integer, found floating-
point number
```

Um eine `Point`-Struktur zu definieren, bei der `x` und `y` beide generisch sind, aber unterschiedliche Typen haben können, können wir mehrere generische Typparameter verwenden. Beispielsweise ändern wir in Listing 10-8 die Definition von `Point`, um generisch über die Typen `T` und `U` zu sein, wobei `x` vom Typ `T` und `y` vom Typ `U` ist.

Dateiname: `src/main.rs`

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

Listing 10-8: Eine `Point<T, U>`-Struktur, die über zwei Typen generisch ist, sodass `x` und `y` Werte unterschiedlicher Typen sein können

Jetzt sind alle gezeigten Instanzen von `Point` erlaubt! Sie können in einer Definition so viele generische Typparameter wie Sie möchten verwenden, aber das Verwenden von mehr als ein paar macht Ihren Code schwer lesbar. Wenn Sie feststellen, dass Sie in Ihrem Code viele generische Typen benötigen, kann dies darauf hinweisen, dass Ihr Code in kleinere Teile umstrukturiert werden muss.
