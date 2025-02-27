# Der Slice-Typ

_Slices_ ermöglichen es Ihnen, auf eine zusammenhängende Sequenz von Elementen in einer Sammlung zu verweisen, anstatt auf die gesamte Sammlung. Ein Slice ist eine Art Referenz, sodass er keine Eigentumsgewalt hat.

Hier ist ein kleines Programmierungsproblem: Schreiben Sie eine Funktion, die einen String von Wörtern, getrennt durch Leerzeichen, annimmt und das erste Wort in diesem String zurückgibt. Wenn die Funktion keinen Leerzeichen im String findet, muss der gesamte String ein Wort sein, also sollte der gesamte String zurückgegeben werden.

Lassen Sie uns durchgehen, wie wir die Signatur dieser Funktion schreiben würden, ohne Slice zu verwenden, um das Problem zu verstehen, das Slice lösen wird:

```rust
fn first_word(s: &String) ->?
```

Die `first_word`-Funktion hat ein `&String` als Parameter. Wir möchten keine Eigentumsgewalt, also ist das in Ordnung. Aber was sollten wir zurückgeben? Wir haben eigentlich keine Möglichkeit, über einen _Teil_ eines Strings zu sprechen. Wir könnten jedoch den Index des Endes des Worts zurückgeben, der durch ein Leerzeichen angegeben wird. Probieren wir das, wie in Listing 4-7 gezeigt.

Dateiname: `src/main.rs`

```rust
fn first_word(s: &String) -> usize {
  1 let bytes = s.as_bytes();

    for (2 i, &item) in 3 bytes.iter().enumerate() {
      4 if item == b' ' {
            return i;
        }
    }

  5 s.len()
}
```

Listing 4-7: Die `first_word`-Funktion, die einen Byte-Indexwert in den `String`-Parameter zurückgibt

Da wir das `String` elementweise durchlaufen müssen und überprüfen müssen, ob ein Wert ein Leerzeichen ist, werden wir unseren `String` in ein Array von Bytes umwandeln, indem wir die `as_bytes`-Methode verwenden \[1\].

Als Nächstes erstellen wir einen Iterator über das Array von Bytes, indem wir die `iter`-Methode verwenden \[3\]. Wir werden Iteratoren im Kapitel 13 im Detail diskutieren. Im Moment wissen Sie nur, dass `iter` eine Methode ist, die jedes Element in einer Sammlung zurückgibt und dass `enumerate` das Ergebnis von `iter` umschließt und jedes Element als Teil eines Tuples zurückgibt. Das erste Element des von `enumerate` zurückgegebenen Tuples ist der Index, und das zweite Element ist eine Referenz auf das Element. Dies ist etwas bequemer als die Berechnung des Indexes selbst.

Da die `enumerate`-Methode ein Tuple zurückgibt, können wir Muster verwenden, um dieses Tuple zu zerlegen. Wir werden Muster im Kapitel 6 noch mehr diskutieren. In der `for`-Schleife geben wir ein Muster an, das `i` für den Index im Tuple und `&item` für das einzelne Byte im Tuple hat \[2\]. Da wir eine Referenz auf das Element von `.iter().enumerate()` erhalten, verwenden wir `&` im Muster.

Innerhalb der `for`-Schleife suchen wir das Byte, das den Leerzeichen darstellt, indem wir die Byte-Literal-Syntax verwenden \[4\]. Wenn wir ein Leerzeichen finden, geben wir die Position zurück. Andernfalls geben wir die Länge des Strings zurück, indem wir `s.len()` verwenden \[5\].

Wir haben jetzt eine Möglichkeit, den Index des Endes des ersten Worts im String zu ermitteln, aber es gibt ein Problem. Wir geben einen `usize` alleine zurück, aber es ist nur eine sinnvolle Zahl im Kontext des `&String`. Mit anderen Worten, da es ein separates Wert vom `String` ist, gibt es keine Garantie, dass es in Zukunft immer noch gültig sein wird. Betrachten Sie das Programm in Listing 4-8, das die `first_word`-Funktion aus Listing 4-7 verwendet.

    // src/main.rs
    fn main() {
        let mut s = String::from("hello world");

        let word = first_word(&s); // word wird den Wert 5 erhalten

        s.clear(); // dies leert den String, sodass er gleich "" ist

        // word hat hier immer noch den Wert 5, aber es gibt keinen mehr String,
        // mit dem wir den Wert 5 sinnvoll verwenden könnten. word ist jetzt völlig ungültig!
    }

Listing 4-8: Speichern des Ergebnisses von Aufrufen der `first_word`-Funktion und dann Ändern des `String`-Inhalts

Dieses Programm kompiliert ohne Fehler und würde auch dann so tun, wenn wir `word` nach dem Aufruf von `s.clear()` verwenden würden. Da `word` überhaupt nicht mit dem Zustand von `s` verbunden ist, enthält `word` immer noch den Wert `5`. Wir könnten diesen Wert `5` mit der Variable `s` verwenden, um das erste Wort zu extrahieren, aber dies wäre ein Bug, da der Inhalt von `s` sich seitdem geändert hat, als wir `5` in `word` gespeichert haben.

Es ist lästig und fehleranfällig, sich um den Index in `word` zu kümmern, der mit den Daten in `s` aus dem Sync gerät! Das Verwalten dieser Indizes ist noch brüchiger, wenn wir eine `second_word`-Funktion schreiben. Ihre Signatur müsste so aussehen:

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Jetzt verfolgen wir einen Anfangs- _und_ einen Endindex, und wir haben noch mehr Werte, die aus Daten in einem bestimmten Zustand berechnet wurden, aber überhaupt nicht an diesen Zustand gebunden sind. Wir haben drei unverbundene Variablen, die im Umlauf gehalten werden müssen, um in Sync zu bleiben.

Glücklicherweise hat Rust eine Lösung für dieses Problem: String-Slices.
