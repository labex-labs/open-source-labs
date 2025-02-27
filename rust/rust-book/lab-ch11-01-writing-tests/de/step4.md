# Das Testen auf Gleichheit mit den assert_eq!- und assert_ne!-Makros

Ein üblicher Weg, um die Funktionalität zu überprüfen, ist es, die Gleichheit zwischen dem Ergebnis des zu testenden Codes und dem Wert zu testen, den Sie erwarten, dass der Code zurückgibt. Sie könnten dies tun, indem Sie das `assert!`-Makro verwenden und ihm einen Ausdruck mit dem `==`-Operator übergeben. Allerdings ist dies ein so üblicher Test, dass die Standardbibliothek zwei Makros bereitstellt - `assert_eq!` und `assert_ne!` - um diesen Test komfortabler durchzuführen. Diese Makros vergleichen zwei Argumente auf Gleichheit oder Ungleichheit, respectively. Sie werden auch die beiden Werte ausgeben, wenn die Behauptung fehlschlägt, was es einfacher macht, zu sehen, _warum_ der Test fehlgeschlagen ist; umgekehrt zeigt das `assert!`-Makro nur an, dass es einen `false`-Wert für den `==`-Ausdruck erhalten hat, ohne die Werte auszugeben, die zu dem `false`-Wert geführt haben.

In Listing 11-7 schreiben wir eine Funktion namens `add_two`, die `2` zu ihrem Parameter addiert, und testen diese Funktion dann mit dem `assert_eq!`-Makro.

Dateiname: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Listing 11-7: Das Testen der Funktion `add_two` mit dem `assert_eq!`-Makro

Lassen Sie uns überprüfen, dass es besteht!

    running 1 test
    test tests::it_adds_two... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Wir übergeben `4` als Argument an `assert_eq!`, das gleich dem Ergebnis von `add_two(2)` ist. Die Zeile für diesen Test lautet `test tests::it_adds_two... ok`, und der Text `ok` zeigt an, dass unser Test bestanden wurde!

Lassen Sie uns einen Fehler in unserem Code einführen, um zu sehen, wie `assert_eq!` aussieht, wenn es fehlschlägt. Ändern Sie die Implementierung der `add_two`-Funktion, um stattdessen `3` hinzuzufügen:

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

Führen Sie die Tests erneut aus:

    running 1 test
    test tests::it_adds_two... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Unser Test hat den Fehler erkannt! Der Test `it_adds_two` ist fehlgeschlagen, und die Fehlermeldung sagt uns, dass die fehlgeschlagene Behauptung `assertion failed:`(left == right)\``[1] war und was die`left`[2] und`right`[3] Werte sind. Diese Meldung hilft uns, mit dem Debugging zu beginnen: das`left`-Argument war`4`, aber das`right`-Argument, wo wir`add_two(2)`hatten, war`5\`. Man kann sich vorstellen, dass dies besonders hilfreich wäre, wenn wir viele Tests ausführen.

Beachten Sie, dass in einigen Sprachen und Testframeworks die Parameter von Gleichheitsbehauptungsfunktionen `expected` und `actual` genannt werden und die Reihenfolge, in der wir die Argumente angeben, wichtig ist. In Rust werden sie jedoch `left` und `right` genannt, und die Reihenfolge, in der wir den Wert angeben, den wir erwarten, und den Wert, den der Code produziert, spielt keine Rolle. Wir könnten die Behauptung in diesem Test als `assert_eq!(add_two(2), 4)` schreiben, was zu derselben Fehlermeldung führen würde, die `assertion failed:`(left == right)\`\` anzeigt.

Das `assert_ne!`-Makro wird bestehen, wenn die beiden Werte, die wir ihm geben, nicht gleich sind, und fehlschlagen, wenn sie gleich sind. Dieses Makro ist am nützlichsten in Fällen, in denen wir uns nicht sicher sind, was ein Wert _werden wird_, aber wir wissen, was der Wert definitiv _nicht sein sollte_. Beispielsweise, wenn wir eine Funktion testen, die gewährleistet ist, ihren Input auf irgendeine Weise zu ändern, aber die Art, wie der Input geändert wird, von dem Tag der Woche abhängt, an dem wir unsere Tests ausführen, ist das Beste, was wir behaupten können, dass die Ausgabe der Funktion nicht gleich dem Input ist.

Im Hintergrund verwenden die `assert_eq!`- und `assert_ne!`-Makros die Operatoren `==` und `!=` respectively. Wenn die Behauptungen fehlschlagen, geben diese Makros ihre Argumente mit Debug-Formatierung aus, was bedeutet, dass die zu vergleichenden Werte das `PartialEq`- und `Debug`-Trait implementieren müssen. Alle primitiven Typen und die meisten der Standardbibliothekstypen implementieren diese Traits. Für Structs und Enums, die Sie selbst definieren, müssen Sie `PartialEq` implementieren, um die Gleichheit dieser Typen zu beweisen. Sie müssen auch `Debug` implementieren, um die Werte auszugeben, wenn die Behauptung fehlschlägt. Da beide Traits ableitbare Traits sind, wie in Listing 5-12 erwähnt, ist dies normalerweise so einfach wie das Hinzufügen der `#[derive(PartialEq, Debug)]`-Annotation zu Ihrer Struct- oder Enum-Definition. Siehe Anhang C für weitere Details über diese und andere ableitbare Traits.
