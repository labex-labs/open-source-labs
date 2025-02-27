# Lifetime Annotations in Function Signatures

Um Lebenszeitannotationen in Funktionssignaturen zu verwenden, müssen wir die generischen _Lebenszeit_-Parameter innerhalb von spitzen Klammern zwischen der Funktionsnamen und der Parameterliste deklarieren, genauso wie wir es mit generischen _Typ_-Parametern getan haben.

Wir möchten, dass die Signatur die folgende Einschränkung ausdrückt: Die zurückgegebene Referenz wird so lange gültig sein, wie beide Parameter gültig sind. Dies ist die Beziehung zwischen den Lebenszeiten der Parameter und dem Rückgabewert. Wir werden die Lebenszeit `'a` nennen und dann sie zu jeder Referenz hinzufügen, wie in Listing 10-21 gezeigt.

Dateiname: `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Listing 10-21: Die `longest`-Funktionsdefinition, die angibt, dass alle Referenzen in der Signatur die gleiche Lebenszeit `'a` haben

Dieser Code sollte kompilieren und das Ergebnis liefern, das wir erwarten, wenn wir ihn mit der `main`-Funktion in Listing 10-19 verwenden.

Die Funktionssignatur sagt jetzt Rust, dass für eine bestimmte Lebenszeit `'a` die Funktion zwei Parameter annimmt, von denen beide String-Slices sind, die mindestens so lange leben wie die Lebenszeit `'a`. Die Funktionssignatur sagt auch Rust, dass der String-Slice, der von der Funktion zurückgegeben wird, mindestens so lange leben wird wie die Lebenszeit `'a`. Im praktischen Einsatz bedeutet das, dass die Lebenszeit der von der `longest`-Funktion zurückgegebenen Referenz die gleiche ist wie die kleinere der Lebenszeiten der Werte, auf die die Funktionsargumente verweisen. Diese Beziehungen sind das, was wir möchten, dass Rust bei der Analyse dieses Codes verwendet.

Denken Sie daran, dass wir bei der Angabe der Lebenszeitparameter in dieser Funktionssignatur die Lebenszeiten von Werten, die übergeben oder zurückgegeben werden, nicht ändern. Stattdessen geben wir an, dass der Borrow-Checker alle Werte ablehnen soll, die diesen Einschränkungen nicht entsprechen. Beachten Sie, dass die `longest`-Funktion nicht genau wissen muss, wie lange `x` und `y` leben werden, sondern nur, dass ein bestimmter Bereich für `'a` eingesetzt werden kann, der dieser Signatur entspricht.

Wenn Lebenszeiten in Funktionen annotiert werden, gehen die Annotations in die Funktionssignatur, nicht in den Funktionskörper. Die Lebenszeitannotationen werden zum Teil des Vertrags der Funktion, ähnlich wie die Typen in der Signatur. Dass Funktionssignaturen den Lebenszeitvertrag enthalten, bedeutet, dass die Analyse, die der Rust-Compiler durchführt, einfacher sein kann. Wenn es ein Problem mit der Art, wie eine Funktion annotiert oder aufgerufen wird, können die Compilerfehler auf den Teil unseres Codes und die Einschränkungen genauer verweisen. Wenn der Rust-Compiler stattdessen mehr Schlussfolgerungen über das, was wir als Beziehung der Lebenszeiten beabsichtigen, ziehen würde, könnte der Compiler nur auf einen Gebrauch unseres Codes viele Schritte von der Ursache des Problems hinweisen.

Wenn wir konkrete Referenzen an `longest` übergeben, ist die konkrete Lebenszeit, die für `'a` eingesetzt wird, der Teil des Bereichs von `x`, der mit dem Bereich von `y` überlappt. Mit anderen Worten, die generische Lebenszeit `'a` erhält die konkrete Lebenszeit, die gleich der kleineren der Lebenszeiten von `x` und `y` ist. Da wir die zurückgegebene Referenz mit dem gleichen Lebenszeitparameter `'a` annotiert haben, wird die zurückgegebene Referenz auch für die Dauer der kleineren der Lebenszeiten von `x` und `y` gültig sein.

Schauen wir uns an, wie die Lebenszeitannotationen die `longest`-Funktion einschränken, indem wir Referenzen mit unterschiedlichen konkreten Lebenszeiten übergeben. Listing 10-22 ist ein einfaches Beispiel.

Dateiname: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

Listing 10-22: Verwendung der `longest`-Funktion mit Referenzen auf `String`-Werte, die unterschiedliche konkrete Lebenszeiten haben

In diesem Beispiel ist `string1` bis zum Ende des äußeren Bereichs gültig, `string2` ist bis zum Ende des inneren Bereichs gültig und `result` verweist auf etwas, das bis zum Ende des inneren Bereichs gültig ist. Führen Sie diesen Code aus, und Sie werden sehen, dass der Borrow-Checker zustimmt; er wird kompilieren und ausgeben `The longest string is long string is long`.

Als nächstes versuchen wir ein Beispiel, das zeigt, dass die Lebenszeit der Referenz in `result` die kleinere Lebenszeit der beiden Argumente sein muss. Wir verschieben die Deklaration der `result`-Variablen außerhalb des inneren Bereichs, lassen aber die Zuweisung des Werts an die `result`-Variable innerhalb des Bereichs mit `string2` stehen. Dann verschieben wir die `println!`, die `result` verwendet, außerhalb des inneren Bereichs, nachdem der innere Bereich beendet ist. Der Code in Listing 10-23 wird nicht kompilieren.

Dateiname: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

Listing 10-23: Versuch, `result` nach dem Auslaufen von `string2` zu verwenden

Wenn wir diesen Code versuchen, zu kompilieren, erhalten wir diesen Fehler:

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

Der Fehler zeigt, dass für `result` gültig zu sein für die `println!`-Anweisung, `string2` bis zum Ende des äußeren Bereichs gültig sein müsste. Rust weiß das, weil wir die Lebenszeiten der Funktionsparameter und Rückgabewerte mit dem gleichen Lebenszeitparameter `'a` annotiert haben.

Als Menschen können wir diesen Code betrachten und sehen, dass `string1` länger als `string2` ist und daher `result` eine Referenz auf `string1` enthalten wird. Da `string1` noch nicht außer Gültigkeitsbereich ist, wird eine Referenz auf `string1` auch für die `println!`-Anweisung gültig sein. Der Compiler kann jedoch nicht sehen, dass die Referenz in diesem Fall gültig ist. Wir haben Rust gesagt, dass die Lebenszeit der von der `longest`-Funktion zurückgegebenen Referenz die gleiche ist wie die kleinere der Lebenszeiten der übergebenen Referenzen. Daher verbietet der Borrow-Checker den Code in Listing 10-23 als möglicherweise eine ungültige Referenz.

Versuchen Sie, weitere Experimente zu entwerfen, die die Werte und Lebenszeiten der Referenzen variieren, die an die `longest`-Funktion übergeben werden, und wie die zurückgegebene Referenz verwendet wird. Machen Sie Hypothesen darüber, ob Ihre Experimente den Borrow-Checker bestehen werden, bevor Sie kompilieren; überprüfen Sie dann, ob Sie Recht haben!
