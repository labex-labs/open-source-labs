# Strukturzerlegung von Structs

Listing 18-12 zeigt eine `Point`-Struktur mit zwei Feldern, `x` und `y`, die wir mit einem Muster in einer `let`-Anweisung aufteilen können.

Dateiname: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    assert_eq!(0, a);
    assert_eq!(7, b);
}
```

Listing 18-12: Strukturzerlegung der Felder einer Struktur in separate Variablen

Dieser Code erstellt die Variablen `a` und `b`, die den Werten der `x`- und `y`-Felder der `p`-Struktur entsprechen. Dieses Beispiel zeigt, dass die Namen der Variablen im Muster nicht mit den Feldnamen der Struktur übereinstimmen müssen. Es ist jedoch üblich, die Variablennamen den Feldnamen zu entsprechen, um es einfacher zu 记住，welche Variablen aus welchen Feldern stammen. Aufgrund dieser üblichen Verwendung und weil das Schreiben von `let Point { x: x, y: y } = p;` viel Duplizität enthält, hat Rust eine Abkürzung für Muster, die Strukturfelder abgleichen: Du musst nur den Namen des Strukturfelds auflisten, und die aus dem Muster erstellten Variablen werden die gleichen Namen haben. Listing 18-13 verhält sich genauso wie der Code in Listing 18-12, aber die im `let`-Muster erstellten Variablen sind `x` und `y` anstelle von `a` und `b`.

Dateiname: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x, y } = p;
    assert_eq!(0, x);
    assert_eq!(7, y);
}
```

Listing 18-13: Strukturzerlegung von Strukturfeldern mit der Strukturfeldabkürzung

Dieser Code erstellt die Variablen `x` und `y`, die den `x`- und `y`-Feldern der `p`-Variablen entsprechen. Das Ergebnis ist, dass die Variablen `x` und `y` die Werte aus der `p`-Struktur enthalten.

Wir können auch mit Literalwerten strukturieren, als Teil des Strukturmusters, anstatt Variablen für alle Felder zu erstellen. Dadurch können wir einige der Felder auf bestimmte Werte testen, während wir Variablen erstellen, um die anderen Felder aufzuteilen.

In Listing 18-14 haben wir einen `match`-Ausdruck, der `Point`-Werte in drei Fälle aufteilt: Punkte, die direkt auf der `x`-Achse liegen (was dann zutrifft, wenn `y = 0`), auf der `y`-Achse (`x = 0`) oder auf keiner Achse.

Dateiname: `src/main.rs`

```rust
fn main() {
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("Auf der x-Achse bei {x}"),
        Point { x: 0, y } => println!("Auf der y-Achse bei {y}"),
        Point { x, y } => {
            println!("Auf keiner Achse: ({x}, {y})");
        }
    }
}
```

Listing 18-14: Strukturzerlegung und Abgleich von Literalwerten in einem Muster

Der erste Arm wird jeden Punkt auf der `x`-Achse abgleichen, indem er angibt, dass das `y`-Feld übereinstimmt, wenn sein Wert mit dem Literal `0` übereinstimmt. Das Muster erstellt immer noch eine `x`-Variable, die wir im Code für diesen Arm verwenden können.

Ähnlich übereinstimmt der zweite Arm jeden Punkt auf der `y`-Achse, indem er angibt, dass das `x`-Feld übereinstimmt, wenn sein Wert `0` ist, und erstellt eine Variable `y` für den Wert des `y`-Felds. Der dritte Arm gibt keine Literale an, sodass er jeden anderen `Point` übereinstimmt und Variablen für beide `x`- und `y`-Felder erstellt.

In diesem Beispiel stimmt der Wert `p` mit dem zweiten Arm überein, weil `x` einen `0` enthält, sodass dieser Code `Auf der y-Achse bei 7` ausgeben wird.

Denke daran, dass ein `match`-Ausdruck aufhört, die Arme zu überprüfen, sobald er das erste übereinstimmende Muster gefunden hat. Daher würde dieser Code auch dann nur `Auf der x-Achse bei 0` ausgeben, wenn `Point { x: 0, y: 0}` auf der `x`-Achse und der `y`-Achse liegt.
