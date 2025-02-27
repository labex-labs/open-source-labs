# `impl Trait`

`impl Trait` kann an zwei Stellen verwendet werden:

1.  als Argumenttyp
2.  als Rückgabetyp

## Als Argumenttyp

Wenn Ihre Funktion über einen Trait generisch ist, aber Sie sich nicht um den spezifischen Typ kümmern, können Sie die Funktionsdeklaration mit `impl Trait` als Typ des Arguments vereinfachen.

Betrachten Sie beispielsweise folgenden Code:

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Für jede Zeile in der Quelle
            line.map(|line| {
                // Wenn die Zeile erfolgreich gelesen wurde, verarbeiten Sie sie, andernfalls geben Sie den Fehler zurück
                line.split(',') // Teilen Sie die Zeile anhand von Kommas auf
                 .map(|entry| String::from(entry.trim())) // Entfernen Sie führende und abschließende Leerzeichen
                 .collect() // Sammeln Sie alle Zeichenketten in einer Zeile in einen Vec<String>
            })
        })
     .collect() // Sammeln Sie alle Zeilen in einen Vec<Vec<String>>
}
```

`parse_csv_document` ist generisch und kann daher jeden Typ akzeptieren, der `BufRead` implementiert, wie z. B. `BufReader<File>` oder `[u8]`, aber es ist nicht wichtig, welchen Typ `R` hat, und `R` wird nur verwendet, um den Typ von `src` zu deklarieren. Daher kann die Funktion auch wie folgt geschrieben werden:

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Für jede Zeile in der Quelle
            line.map(|line| {
                // Wenn die Zeile erfolgreich gelesen wurde, verarbeiten Sie sie, andernfalls geben Sie den Fehler zurück
                line.split(',') // Teilen Sie die Zeile anhand von Kommas auf
                 .map(|entry| String::from(entry.trim())) // Entfernen Sie führende und abschließende Leerzeichen
                 .collect() // Sammeln Sie alle Zeichenketten in einer Zeile in einen Vec<String>
            })
        })
     .collect() // Sammeln Sie alle Zeilen in einen Vec<Vec<String>>
}
```

Beachten Sie, dass das Verwenden von `impl Trait` als Argumenttyp bedeutet, dass Sie nicht explizit angeben können, welche Form der Funktion Sie verwenden. D. h., `parse_csv_document::<std::io::Empty>(std::io::empty())` funktioniert nicht mit dem zweiten Beispiel.

## Als Rückgabetyp

Wenn Ihre Funktion einen Typ zurückgibt, der `MyTrait` implementiert, können Sie seinen Rückgabetyp als `-> impl MyTrait` schreiben. Dies kann die Typensignatur erheblich vereinfachen!

```rust
use std::iter;
use std::vec::IntoIter;

// Diese Funktion kombiniert zwei `Vec<i32>` und gibt einen Iterator darüber zurück.
// Schauen Sie sich an, wie kompliziert sein Rückgabetyp ist!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// Dies ist die genaue gleiche Funktion, aber ihr Rückgabetyp verwendet `impl Trait`.
// Schauen Sie sich an, wie viel einfacher es ist!
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("all done");
}
```

Wichtiger noch, einige Rust-Typen können nicht geschrieben werden. Beispielsweise hat jede Closure ihren eigenen namenlosen konkreten Typ. Bevor die `impl Trait`-Syntax existierte, mussten Sie auf dem Heap allokieren, um eine Closure zurückzugeben. Aber jetzt können Sie es statisch machen, wie folgt:

```rust
// Gibt eine Funktion zurück, die `y` zu ihrem Eingang addiert
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

Sie können auch `impl Trait` verwenden, um einen Iterator zurückzugeben, der `map` oder `filter`-Closures verwendet! Dies macht das Verwenden von `map` und `filter` einfacher. Da Closure-Typen keine Namen haben, können Sie keinen expliziten Rückgabetyp schreiben, wenn Ihre Funktion Iteratoren mit Closures zurückgibt. Aber mit `impl Trait` können Sie dies leicht tun:

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
