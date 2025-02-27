# let-Anweisungen

Vor diesem Kapitel hatten wir nur explizit über das Verwenden von Mustern mit `match` und `if let` diskutiert, aber tatsächlich haben wir Mustern auch an anderen Stellen verwendet, einschließlich in `let`-Anweisungen. Beispielsweise betrachten Sie diese einfache Variablenzuweisung mit `let`:

```rust
let x = 5;
```

Jedes Mal, wenn Sie eine `let`-Anweisung wie diese verwendet haben, haben Sie Mustern verwendet, obwohl Sie das vielleicht nicht bemerkt haben! Formeller sieht eine `let`-Anweisung so aus:

```rust
let MUSTER = AUSDRUCK;
```

In Anweisungen wie `let x = 5;` mit einem Variablennamen in der MUSTER-Slot ist der Variablennamen nur eine besonders einfache Form eines Musters. Rust vergleicht den Ausdruck mit dem Muster und weist allen gefundenen Namen zu. Also bedeutet in dem Beispiel `let x = 5;`, dass `x` ein Muster ist, das bedeutet: "Binde das, was hier übereinstimmt, an die Variable `x`." Da der Name `x` das gesamte Muster ist, bedeutet dieses Muster effektiv: "Binde alles an die Variable `x`, was auch immer der Wert ist."

Um den musterabgleichenden Aspekt von `let` deutlicher zu sehen, betrachten Sie Listing 18-4, das ein Muster mit `let` verwendet, um ein Tupel aufzulösen.

```rust
let (x, y, z) = (1, 2, 3);
```

Listing 18-4: Verwenden eines Musters, um ein Tupel aufzulösen und gleichzeitig drei Variablen zu erstellen

Hier vergleichen wir ein Tupel mit einem Muster. Rust vergleicht den Wert `(1, 2, 3)` mit dem Muster `(x, y, z)` und erkennt, dass der Wert mit dem Muster übereinstimmt, in dem er sieht, dass die Anzahl der Elemente in beiden gleich ist. Daher bindet Rust `1` an `x`, `2` an `y` und `3` an `z`. Man kann sich dieses Tupelmuster als das Verschachteln von drei einzelnen Variablenmustern darin vorstellen.

Wenn die Anzahl der Elemente im Muster nicht mit der Anzahl der Elemente im Tupel übereinstimmt, stimmt der gesamte Typ nicht überein und wir erhalten einen Compilerfehler. Beispielsweise zeigt Listing 18-5 einen Versuch, ein Tupel mit drei Elementen in zwei Variablen aufzulösen, was nicht funktioniert.

```rust
let (x, y) = (1, 2, 3);
```

Listing 18-5: Falsches Konstruieren eines Musters, dessen Variablen nicht mit der Anzahl der Elemente im Tupel übereinstimmen

Beim Versuch, diesen Code zu kompilieren, tritt dieser Typfehler auf:

```bash
error[E0308]: mismatched types
 --> src/main.rs:2:9
  |
2 |     let (x, y) = (1, 2, 3);
  |         ^^^^^^   --------- this expression has type `({integer}, {integer},
{integer})`
  |         |
  |         expected a tuple with 3 elements, found one with 2 elements
  |
  = note: expected tuple `({integer}, {integer}, {integer})`
             found tuple `(_, _)`
```

Um den Fehler zu beheben, können wir einen oder mehrere der Werte im Tupel mit `_` oder `..` ignorieren, wie Sie in "Ignoring Values in a Pattern" sehen werden. Wenn das Problem darin besteht, dass wir zu viele Variablen im Muster haben, ist die Lösung, die Typen so zu passen, dass wir Variablen entfernen, sodass die Anzahl der Variablen der Anzahl der Elemente im Tupel entspricht.
