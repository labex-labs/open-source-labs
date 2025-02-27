# Das Entfernen von eingefangenen Werten aus Closures und die Fn-Traits

Sobald ein Closure eine Referenz eingefangen hat oder die Eigentumsgewalt an einen Wert aus der Umgebung übernommen hat, in der das Closure definiert ist (was somit beeinflusst, was, wenn überhaupt etwas, in das Closure _eingezogen_ wird), definiert der Code im Körper des Closures, was mit den Referenzen oder Werten passiert, wenn das Closure später ausgewertet wird (was somit beeinflusst, was, wenn überhaupt etwas, aus dem Closure _entfernt_ wird).

Ein Closure-Körper kann eines der folgenden tun: einen eingefangenen Wert aus dem Closure entfernen, den eingefangenen Wert mutieren, weder den Wert entfernen noch mutieren oder überhaupt nichts aus der Umgebung einfangen.

Die Art, wie ein Closure Werte aus der Umgebung einfängt und behandelt, beeinflusst, welche Traits das Closure implementiert, und Traits sind die Art, wie Funktionen und Structs angeben können, welche Arten von Closures sie verwenden können. Closures werden automatisch einen, zwei oder alle drei dieser `Fn`-Traits in additiver Weise implementieren, je nachdem, wie der Closure-Körper die Werte behandelt:

- `FnOnce` gilt für Closures, die einmal aufgerufen werden können. Alle Closures implementieren mindestens diesen Trait, weil alle Closures aufgerufen werden können. Ein Closure, das eingefangene Werte aus seinem Körper entfernt, wird nur `FnOnce` implementieren und keine der anderen `Fn`-Traits, da es nur einmal aufgerufen werden kann.
- `FnMut` gilt für Closures, die eingefangene Werte nicht aus ihrem Körper entfernen, aber die eingefangenen Werte mutieren können. Diese Closures können mehr als einmal aufgerufen werden.
- `Fn` gilt für Closures, die eingefangene Werte nicht aus ihrem Körper entfernen und die eingefangenen Werte nicht mutieren, sowie für Closures, die nichts aus ihrer Umgebung einfangen. Diese Closures können mehr als einmal ohne die Umgebung zu mutieren aufgerufen werden, was wichtig ist, z.B. bei der gleichzeitigen mehrfachen Ausführung eines Closures.

Schauen wir uns die Definition der `unwrap_or_else`-Methode auf `Option<T>` an, die wir in Listing 13-1 verwendet haben:

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

Denken Sie daran, dass `T` der generische Typ ist, der den Typ des Werts in der `Some`-Variante einer `Option` repräsentiert. Dieser Typ `T` ist auch der Rückgabetyp der `unwrap_or_else`-Funktion: Code, der `unwrap_or_else` auf einer `Option<String>` aufruft, bekommt beispielsweise einen `String`.

Als nächstes bemerken Sie, dass die `unwrap_or_else`-Funktion den zusätzlichen generischen Typparameter `F` hat. Der `F`-Typ ist der Typ des Parameters namens `f`, der das Closure ist, das wir bei der Aufruf von `unwrap_or_else` angeben.

Die Trait-Bedingung, die auf dem generischen Typ `F` angegeben ist, lautet `FnOnce() -> T`, was bedeutet, dass `F` einmal aufgerufen werden muss, keine Argumente entgegennehmen darf und einen `T` zurückgeben muss. Die Verwendung von `FnOnce` in der Trait-Bedingung drückt die Einschränkung aus, dass `unwrap_or_else` `f` höchstens einmal aufrufen wird. Im Körper von `unwrap_or_else` können wir sehen, dass wenn die `Option` `Some` ist, `f` nicht aufgerufen wird. Wenn die `Option` `None` ist, wird `f` einmal aufgerufen. Da alle Closures `FnOnce` implementieren, akzeptiert `unwrap_or_else` die größte Anzahl von Closures und ist so flexibel wie möglich.

> Hinweis: Funktionen können auch alle drei der `Fn`-Traits implementieren. Wenn das, was wir tun möchten, nicht erfordert, einen Wert aus der Umgebung einzufangen, können wir den Namen einer Funktion statt eines Closures verwenden, wenn wir etwas benötigen, das einen der `Fn`-Traits implementiert. Beispielsweise könnten wir auf einem `Option<Vec<T>>`-Wert `unwrap_or_else(Vec::new)` aufrufen, um einen neuen, leeren Vektor zu erhalten, wenn der Wert `None` ist.

Lassen Sie uns jetzt die Standardbibliotheksmethode `sort_by_key` betrachten, die auf Slices definiert ist, um zu sehen, wie das von `unwrap_or_else` unterschiedlich ist und warum `sort_by_key` für die Trait-Bedingung `FnMut` statt `FnOnce` verwendet. Das Closure erhält ein Argument in Form einer Referenz auf das aktuelle Element im betrachteten Slice und gibt einen Wert vom Typ `K` zurück, der geordnet werden kann. Diese Funktion ist nützlich, wenn Sie einen Slice nach einem bestimmten Attribut jedes Elements sortieren möchten. In Listing 13-7 haben wir eine Liste von `Rectangle`-Instanzen und verwenden `sort_by_key`, um sie nach ihrem `width`-Attribut von niedrig nach hoch zu ordnen.

Dateiname: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Listing 13-7: Verwenden von `sort_by_key`, um Rechtecke nach der Breite zu ordnen

Dieser Code gibt aus:

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

Der Grund, warum `sort_by_key` so definiert ist, dass es ein `FnMut`-Closure annimmt, ist, dass es das Closure mehr als einmal aufruft: einmal für jedes Element im Slice. Das Closure `|r| r.width` fängt, mutiert oder entfernt nichts aus seiner Umgebung, sodass es die Trait-Bedingungen erfüllt.

Im Gegensatz dazu zeigt Listing 13-8 ein Beispiel für ein Closure, das nur den `FnOnce`-Trait implementiert, weil es einen Wert aus der Umgebung entfernt. Der Compiler lässt uns dieses Closure nicht mit `sort_by_key` verwenden.

Dateiname: `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

Listing 13-8: Versuch, ein `FnOnce`-Closure mit `sort_by_key` zu verwenden

Dies ist eine absichtlich komplizierte und umständliche Weise (die nicht funktioniert), um zu versuchen, die Anzahl der Aufrufe von `sort_by_key` zu zählen, wenn `list` sortiert wird. Dieser Code versucht, diese Zählung durch das Hinzufügen von `value` - einem `String` aus der Umgebung des Closures - in den `sort_operations`-Vektor durchzuführen. Das Closure fängt `value` ein und entfernt dann `value` aus dem Closure, indem es die Eigentumsgewalt von `value` an den `sort_operations`-Vektor übergibt. Dieses Closure kann einmal aufgerufen werden; das Versuchen, es eine zweite Zeit aufzurufen, würde nicht funktionieren, weil `value` nicht mehr in der Umgebung wäre, um erneut in `sort_operations` eingefügt zu werden! Daher implementiert dieses Closure nur `FnOnce`. Wenn wir diesen Code versuchen, zu kompilieren, erhalten wir diesen Fehler, dass `value` nicht aus dem Closure entfernt werden kann, weil das Closure `FnMut` implementieren muss:

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

Der Fehler verweist auf die Zeile im Closure-Körper, in der `value` aus der Umgebung entfernt wird. Um das zu beheben, müssen wir den Closure-Körper ändern, sodass er keine Werte aus der Umgebung entfernt. Ein Zähler in der Umgebung zu halten und seinen Wert im Closure-Körper zu erhöhen, ist eine einfacherere Weise, um die Anzahl der Aufrufe von `sort_by_key` zu zählen. Das Closure in Listing 13-9 funktioniert mit `sort_by_key`, weil es nur eine veränderliche Referenz auf den `num_sort_operations`-Zähler fängt und daher mehr als einmal aufgerufen werden kann.

Dateiname: `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

Listing 13-9: Das Verwenden eines `FnMut`-Closures mit `sort_by_key` ist erlaubt.

Die `Fn`-Traits sind wichtig, wenn Sie Funktionen oder Typen definieren oder verwenden, die Closures nutzen. Im nächsten Abschnitt werden wir Iteratoren diskutieren. Viele Iterator-Methoden nehmen Closure-Argumente an, also halten Sie diese Closure-Details im Kopf, wenn wir fortfahren!
