# Matching mit Option`<T>`

Im vorherigen Abschnitt wollten wir den inneren `T`-Wert aus dem `Some`-Fall herausholen, wenn wir `Option<T>` verwenden; wir können `Option<T>` auch mit `match` behandeln, wie wir es mit dem `Coin`-Enum gemacht haben! Anstatt Münzen zu vergleichen, werden wir die Varianten von `Option<T>` vergleichen, aber die Art, wie der `match`-Ausdruck funktioniert, bleibt dieselbe.

Angenommen, wir möchten eine Funktion schreiben, die ein `Option<i32>` annimmt und, wenn ein Wert darin vorhanden ist, 1 zum Wert hinzufügt. Wenn kein Wert darin vorhanden ist, sollte die Funktion den `None`-Wert zurückgeben und keine weiteren Operationen ausführen.

Diese Funktion ist dank `match` sehr einfach zu schreiben und wird wie in Listing 6-5 aussehen.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
      1 None => None,
      2 Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five); 3
let none = plus_one(None); 4
```

Listing 6-5: Eine Funktion, die einen `match`-Ausdruck auf einem `Option<i32>` verwendet

Betrachten wir die erste Ausführung von `plus_one` genauer. Wenn wir `plus_one(five)` aufrufen \[3\], hat die Variable `x` im Körper von `plus_one` den Wert `Some(5)`. Wir vergleichen das dann mit jedem `match`-Arm:

```rust
None => None,
```

Der Wert `Some(5)` stimmt nicht mit dem Muster `None` überein \[1\], also gehen wir zum nächsten Arm weiter:

```rust
Some(i) => Some(i + 1),
```

Stimmt `Some(5)` mit `Some(i)` überein \[2\]? Ja, stimmt! Wir haben die gleiche Variante. Die Variable `i` bindet sich an den in `Some` enthaltenen Wert, sodass `i` den Wert `5` annimmt. Der Code im `match`-Arm wird dann ausgeführt, sodass wir 1 zum Wert von `i` addieren und einen neuen `Some`-Wert mit unserem Gesamtwert `6` darin erzeugen.

Betrachten wir nun den zweiten Aufruf von `plus_one` in Listing 6-5, bei dem `x` `None` ist \[4\]. Wir betreten den `match` und vergleichen ihn mit dem ersten Arm \[1\].

Es stimmt überein! Es gibt keinen Wert, dem etwas hinzugefügt werden soll, also stoppt das Programm und gibt den `None`-Wert auf der rechten Seite von `=>` zurück. Da der erste Arm übereinstimmt, werden keine anderen Arme verglichen.

Das Zusammenführen von `match` und Enums ist in vielen Situationen nützlich. Sie werden dieses Muster in Rust-Code häufig sehen: `match` gegen ein Enum, binden Sie eine Variable an die darin enthaltenen Daten und führen Sie dann basierend darauf Code aus. Es ist zunächst ein bisschen tricky, aber wenn Sie sich daran gewöhnen, wünschen Sie sich es in allen Sprachen. Es ist immer ein Lieblingsfeature der Benutzer.
