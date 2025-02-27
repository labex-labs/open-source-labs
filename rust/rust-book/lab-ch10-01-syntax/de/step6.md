# In Methodendefinitionen

Wir können Methoden auf Strukturen und Enums implementieren (wie wir es im Kapitel 5 getan haben), und auch in ihren Definitionen generische Typen verwenden. Listing 10-9 zeigt die `Point<T>`-Struktur, die wir in Listing 10-6 definiert haben, mit einer Methode namens `x`, die auf ihr implementiert ist.

Dateiname: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}
```

Listing 10-9: Implementieren einer Methode namens `x` auf der `Point<T>`-Struktur, die eine Referenz auf das `x`-Feld vom Typ `T` zurückgibt

Hier haben wir eine Methode namens `x` auf `Point<T>` definiert, die eine Referenz auf die Daten im Feld `x` zurückgibt.

Beachten Sie, dass wir `T` direkt nach `impl` deklarieren müssen, damit wir `T` verwenden können, um anzugeben, dass wir Methoden auf dem Typ `Point<T>` implementieren. Indem wir `T` als generischen Typ nach `impl` deklarieren, kann Rust erkennen, dass der Typ in den eckigen Klammern in `Point` ein generischer Typ ist und kein konkreter Typ. Wir hätten für diesen generischen Parameter einen anderen Namen wählen können als den generischen Parameter, der in der Strukturdefinition deklariert wurde, aber es ist üblich, den gleichen Namen zu verwenden. Methoden, die innerhalb eines `impl` geschrieben werden, das den generischen Typ deklariert, werden für jede Instanz des Typs definiert, unabhängig davon, welchen konkreten Typ schließlich für den generischen Typ eingesetzt wird.

Wir können auch Einschränkungen für generische Typen angeben, wenn wir Methoden für den Typ definieren. Wir könnten beispielsweise Methoden nur auf `Point<f32>`-Instanzen implementieren, statt auf `Point<T>`-Instanzen mit beliebigem generischem Typ. In Listing 10-10 verwenden wir den konkreten Typ `f32`, was bedeutet, dass wir keine Typen nach `impl` deklarieren.

Dateiname: `src/main.rs`

```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

Listing 10-10: Ein `impl`-Block, der nur auf eine Struktur mit einem bestimmten konkreten Typ für den generischen Typparameter `T` anwendbar ist

Dieser Code bedeutet, dass der Typ `Point<f32>` eine `distance_from_origin`-Methode haben wird; andere Instanzen von `Point<T>`, bei denen `T` kein `f32`-Typ ist, werden diese Methode nicht haben. Die Methode misst, wie weit unser Punkt von dem Punkt bei den Koordinaten (0.0, 0.0) entfernt ist, und verwendet mathematische Operationen, die nur für Gleitkomma-Typen verfügbar sind.

Generische Typparameter in einer Strukturdefinition stimmen nicht immer mit denen überein, die Sie in der Methodensignatur derselben Struktur verwenden. Listing 10-11 verwendet die generischen Typen `X1` und `Y1` für die `Point`-Struktur und `X2` und `Y2` für die `mixup`-Methodensignatur, um das Beispiel verständlicher zu machen. Die Methode erstellt eine neue `Point`-Instanz mit dem `x`-Wert aus der `self`-`Point` (vom Typ `X1`) und dem `y`-Wert aus der übergebenen `Point` (vom Typ `Y2`).

Dateiname: `src/main.rs`

```rust
struct Point<X1, Y1> {
    x: X1,
    y: Y1,
}

1 impl<X1, Y1> Point<X1, Y1> {
  2 fn mixup<X2, Y2>(
        self,
        other: Point<X2, Y2>,
    ) -> Point<X1, Y2> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}

fn main() {
  3 let p1 = Point { x: 5, y: 10.4 };
  4 let p2 = Point { x: "Hello", y: 'c' };

  5 let p3 = p1.mixup(p2);

  6 println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```

Listing 10-11: Eine Methode, die generische Typen verwendet, die von ihrer Strukturdefinition verschieden sind

In `main` haben wir eine `Point` definiert, die für `x` einen `i32` hat (mit dem Wert `5`) und für `y` einen `f64` (mit dem Wert `10.4` \[3\]). Die Variable `p2` ist eine `Point`-Struktur, die für `x` einen String-Slice hat (mit dem Wert `"Hello"`) und für `y` ein `char` (mit dem Wert `c` \[4\]). Wenn wir `mixup` auf `p1` mit dem Argument `p2` aufrufen, erhalten wir `p3` \[5\], das für `x` einen `i32` haben wird, weil `x` von `p1` stammt. Die Variable `p3` wird für `y` ein `char` haben, weil `y` von `p2` stammt. Der `println!`-Makroaufruf \[6\] wird `p3.x = 5, p3.y = c` ausgeben.

Zweck dieses Beispiels ist es, eine Situation zu demonstrieren, in der einige generische Parameter mit `impl` deklariert werden und einige mit der Methodendefinition. Hier werden die generischen Parameter `X1` und `Y1` nach `impl` deklariert \[1\], weil sie mit der Strukturdefinition zusammenhängen. Die generischen Parameter `X2` und `Y2` werden nach `fn mixup` deklariert \[2\], weil sie nur für die Methode relevant sind.
