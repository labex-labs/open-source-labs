# Die Option-Enumeration und ihre Vorteile gegenüber Null-Werten

In diesem Abschnitt befassen wir uns mit einer Fallstudie zu `Option`, einer weiteren Enumeration, die von der Standardbibliothek definiert wird. Der `Option`-Typ kodiert den sehr häufigen Fall, in dem ein Wert vorhanden sein kann oder nicht.

Beispielsweise erhalten Sie einen Wert, wenn Sie das erste Element in einer Liste mit mehreren Elementen anfordern. Wenn Sie das erste Element in einer leeren Liste anfordern, erhalten Sie nichts. Die Darstellung dieses Konzepts im Typensystem bedeutet, dass der Compiler überprüfen kann, ob Sie alle Fälle behandelt haben, die Sie behandeln sollten; diese Funktionalität kann Fehler verhindern, die in anderen Programmiersprachen extrem häufig auftreten.

Die Programmiersprachendesign wird oft in Bezug auf die enthaltenen Funktionen betrachtet, aber auch die ausgeschlossenen Funktionen sind wichtig. Rust hat nicht das Null-Feature, das viele andere Sprachen haben. _Null_ ist ein Wert, der bedeutet, dass kein Wert vorhanden ist. In Sprachen mit Null können Variablen immer in einem der beiden Zustände sein: Null oder nicht-null.

Im Jahr 2009 hielt Tony Hoare, der Erfinder von Null, in seiner Präsentation "Null References: The Billion Dollar Mistake" folgende Rede:

> Ich nenne es meinen Fehler im Milliardenbereich. Damals entwarf ich das erste umfassende Typsystem für Referenzen in einer objektorientierten Sprache. Mein Ziel war es, sicherzustellen, dass alle Verwendung von Referenzen absolut sicher ist, mit einer automatischen Prüfung durch den Compiler. Aber ich konnte der Versuchung nicht widerstehen, einen Null-Referenz hinzuzufügen, einfach weil sie so leicht zu implementieren war. Dies hat zu unzähligen Fehlern, Schwachstellen und Systemausfällen geführt, die wahrscheinlich in den letzten vierzig Jahren einen Schaden von Milliarden von Dollar verursacht haben. Das Problem mit Null-Werten ist, dass Sie einen Fehler von irgendwelcher Art erhalten, wenn Sie versuchen, einen Null-Wert als nicht-null-Wert zu verwenden. Da diese Null- oder nicht-null-Eigenschaft allgegenwärtig ist, ist es extrem leicht, diesen Fehler zu begehen.

Allerdings ist das Konzept, das Null ausdrücken möchte, immer noch nützlich: ein Null ist ein Wert, der derzeit aus irgendeinem Grund ungültig oder fehlt.

Das Problem liegt nicht wirklich mit dem Konzept, sondern mit der speziellen Implementierung. Daher hat Rust keine Nulls, hat aber eine Enumeration, die das Konzept eines vorhandenen oder fehlenden Werts kodieren kann. Diese Enumeration ist `Option<T>`, und sie wird von der Standardbibliothek wie folgt definiert:

```rust
enum Option<T> {
    None,
    Some(T),
}
```

Die `Option<T>`-Enumeration ist so nützlich, dass sie sogar im Präludium enthalten ist; Sie müssen sie nicht explizit in den Geltungsbereich bringen. Ihre Varianten sind auch im Präludium enthalten: Sie können `Some` und `None` direkt ohne das `Option::`-Präfix verwenden. Die `Option<T>`-Enumeration ist immer noch nur eine reguläre Enumeration, und `Some(T)` und `None` sind immer noch Varianten vom Typ `Option<T>`.

Die `<T>`-Syntax ist ein Feature von Rust, über das wir bisher noch nicht gesprochen haben. Es ist ein generischer Typparameter, und wir werden Generics im Kapitel 10 genauer behandeln. Für jetzt brauchen Sie nur zu wissen, dass `<T>` bedeutet, dass die `Some`-Variante der `Option`-Enumeration ein Datenstück beliebigen Typs enthalten kann, und dass jeder konkrete Typ, der anstelle von `T` verwendet wird, den gesamten `Option<T>`-Typ zu einem anderen Typ macht. Hier sind einige Beispiele für die Verwendung von `Option`-Werten, um Zahlentypen und Zeichenketten zu halten:

```rust
let some_number = Some(5);
let some_char = Some('e');

let absent_number: Option<i32> = None;
```

Der Typ von `some_number` ist `Option<i32>`. Der Typ von `some_char` ist `Option<char>`, was ein anderer Typ ist. Rust kann diese Typen ableiten, weil wir einen Wert innerhalb der `Some`-Variante angegeben haben. Für `absent_number` erfordert Rust, dass wir den gesamten `Option`-Typ angeben: Der Compiler kann den Typ nicht ableiten, den die entsprechende `Some`-Variante halten wird, indem er nur einen `None`-Wert betrachtet. Hier sagen wir Rust, dass wir meinen, dass `absent_number` vom Typ `Option<i32>` sein soll.

Wenn wir einen `Some`-Wert haben, wissen wir, dass ein Wert vorhanden ist und der Wert innerhalb der `Some` gehalten wird. Wenn wir einen `None`-Wert haben, bedeutet es in gewisser Weise dasselbe wie Null: wir haben keinen gültigen Wert. Also, warum ist es besser, `Option<T>` zu haben als Null?

Kurz gesagt, weil `Option<T>` und `T` (wobei `T` beliebigen Typs sein kann) unterschiedliche Typen sind, lässt der Compiler uns keinen `Option<T>`-Wert so verwenden, als wäre er definitiv ein gültiger Wert. Beispielsweise wird dieser Code nicht kompilieren, weil er versucht, einen `i8` zu einem `Option<i8>` hinzuzufügen:

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

let sum = x + y;
```

Wenn wir diesen Code ausführen, erhalten wir eine Fehlermeldung wie diese:

```bash
error[E0277]: cannot add `Option<i8>` to `i8`
 --> src/main.rs:5:17
  |
5 |     let sum = x + y;
  |                 ^ no implementation for `i8 + Option<i8>`
  |
  = help: the trait `Add<Option<i8>>` is not implemented for `i8`
```

Intensiv! In der Tat bedeutet diese Fehlermeldung, dass Rust nicht versteht, wie ein `i8` und ein `Option<i8>` addiert werden sollen, weil sie unterschiedliche Typen sind. Wenn wir in Rust einen Wert eines Typs wie `i8` haben, wird der Compiler sicherstellen, dass wir immer einen gültigen Wert haben. Wir können mit Zuversicht fortfahren, ohne vorher auf Null zu prüfen, bevor wir diesen Wert verwenden. Erst wenn wir einen `Option<i8>` (oder einen beliebigen anderen Werttyp, mit dem wir arbeiten) haben, müssen wir uns um die Möglichkeit kümmern, keinen Wert zu haben, und der Compiler wird sicherstellen, dass wir diesen Fall behandeln, bevor wir den Wert verwenden.

Mit anderen Worten, Sie müssen ein `Option<T>` in ein `T` umwandeln, bevor Sie mit ihm `T`-Operationen ausführen können. Im Allgemeinen hilft dies, einen der häufigsten Probleme mit Null zu erkennen: das Annehmen, dass etwas nicht null ist, wenn es tatsächlich null ist.

Das Risiko, ein nicht-null-Wert falsch zu unterstellen, zu eliminieren, hilft Ihnen, sich in Ihrem Code sicherer zu fühlen. Um einen Wert zu haben, der möglicherweise null ist, müssen Sie sich explizit dazu entscheiden, indem Sie den Typ dieses Werts `Option<T>` machen. Dann, wenn Sie diesen Wert verwenden, müssen Sie explizit den Fall behandeln, wenn der Wert null ist. Überall, wo ein Wert einen Typ hat, der kein `Option<T>` ist, können Sie _sicher_ annehmen, dass der Wert nicht null ist. Dies war eine bewusste Designentscheidung für Rust, um die Allgegenwärtigkeit von Null zu begrenzen und die Sicherheit von Rust-Code zu erhöhen.

Also, wie bekommen Sie den `T`-Wert aus einer `Some`-Variante, wenn Sie einen Wert vom Typ `Option<T>` haben, um diesen Wert verwenden zu können? Die `Option<T>`-Enumeration hat eine Vielzahl von Methoden, die in verschiedenen Situationen nützlich sind; Sie können sie in ihrer Dokumentation nachsehen. Das Vertrautmachen mit den Methoden auf `Option<T>` wird auf Ihrem Weg mit Rust extrem nützlich sein.

Im Allgemeinen müssen Sie Code haben, der jede Variante behandelt, um einen `Option<T>`-Wert zu verwenden. Sie möchten Code haben, der nur dann ausgeführt wird, wenn Sie einen `Some(T)`-Wert haben, und dieser Code darf den inneren `T` verwenden. Sie möchten anderen Code haben, der nur dann ausgeführt wird, wenn Sie einen `None`-Wert haben, und dieser Code hat keinen `T`-Wert zur Verfügung. Der `match`-Ausdruck ist ein Steuerflusskonstrukt, das genau dies tut, wenn er mit Enumerationen verwendet wird: er wird unterschiedlicher Code ausführen, je nachdem, welche Variante der Enumeration er hat, und dieser Code kann die Daten innerhalb des passenden Werts verwenden.
