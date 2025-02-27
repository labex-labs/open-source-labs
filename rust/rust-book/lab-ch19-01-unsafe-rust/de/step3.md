# Ein rohen Zeiger dereferenzieren

Im Abschnitt "Schwebende Referenzen" haben wir erwähnt, dass der Compiler sicherstellt, dass Referenzen immer gültig sind. Unsafe Rust hat zwei neue Typen namens _rohe Zeiger_, die ähnlich zu Referenzen sind. Wie bei Referenzen können rohe Zeiger unveränderlich oder veränderlich sein und werden als `*const T` bzw. `*mut T` geschrieben. Das Sternchen ist kein Dereferenzierungsoperator; es ist Teil des Typnamens. Im Kontext von rohen Zeigern bedeutet _unveränderlich_, dass der Zeiger nach der Dereferenzierung nicht direkt zugewiesen werden kann.

Im Gegensatz zu Referenzen und Smart-Pointern erlauben rohe Zeiger:

- Die Entlassungsregeln zu ignorieren, indem sowohl unveränderliche als auch veränderliche Zeiger oder mehrere veränderliche Zeiger auf die gleiche Adresse verweisen
- Es ist nicht gewährleistet, dass sie auf gültigen Speicher verweisen
- Es ist erlaubt, dass sie NULL sind
- Es wird keine automatische Bereinigung implementiert

Indem du die Garantien von Rust nicht durchsetzen lässt, kannst du die garantierte Sicherheit aufgeben, um eine höhere Leistung oder die Möglichkeit zu erhalten, mit einer anderen Sprache oder Hardware zu interagieren, wo Rusts Garantien nicht gelten.

Listing 19-1 zeigt, wie man einen unveränderlichen und einen veränderlichen rohen Zeiger aus Referenzen erstellt.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;
```

Listing 19-1: Erstellen von rohen Zeigern aus Referenzen

Bemerkenswert ist, dass wir in diesem Code nicht das Schlüsselwort `unsafe` verwenden. Wir können rohe Zeiger in safe Code erstellen; wir können sie nur außerhalb eines unsafe Blocks nicht dereferenzieren, wie du bald sehen wirst.

Wir haben rohe Zeiger erstellt, indem wir `as` verwenden, um eine unveränderliche und eine veränderliche Referenz in ihre entsprechenden rohen Zeigertypen umzuwandeln. Da wir sie direkt aus Referenzen erstellt haben, die als gültig gewährleistet sind, wissen wir, dass diese speziellen rohen Zeiger gültig sind, aber wir können dies für jeden beliebigen rohen Zeiger nicht annehmen.

Um dies zu demonstrieren, werden wir im nächsten Schritt einen rohen Zeiger erstellen, dessen Gültigkeit uns nicht so sicher ist. Listing 19-2 zeigt, wie man einen rohen Zeiger auf eine beliebige Adresse im Speicher erstellt. Versuchen, beliebigen Speicher zu verwenden, ist undefiniert: Es könnte Daten an dieser Adresse geben oder es könnte auch keine geben, der Compiler könnte den Code optimieren, so dass es keinen Speicherzugriff gibt, oder das Programm könnte mit einem Segmentation-Fehler beenden. Normalerweise gibt es keinen guten Grund, Code wie diesen zu schreiben, aber es ist möglich.

```rust
let address = 0x012345usize;
let r = address as *const i32;
```

Listing 19-2: Erstellen eines rohen Zeigers auf eine beliebige Speicheradresse

Denken wir daran, dass wir rohe Zeiger in safe Code erstellen können, aber wir können rohe Zeiger nicht _dereferenzieren_ und die daraufzeigenden Daten lesen. In Listing 19-3 verwenden wir den Dereferenzierungsoperator `*` auf einen rohen Zeiger, der einen `unsafe` Block erfordert.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

Listing 19-3: Dereferenzieren von rohen Zeigern innerhalb eines `unsafe` Blocks

Das Erstellen eines Zeigers schadet nicht; erst wenn wir versuchen, auf den Wert zuzugreifen, auf den er zeigt, können wir mit einem ungültigen Wert zu tun haben.

Beachte auch, dass in Listings 19-1 und 19-3 wir `*const i32` und `*mut i32` rohe Zeiger erstellt haben, die beide auf die gleiche Speicheradresse zeigten, an der `num` gespeichert ist. Wenn wir stattdessen versuchen würden, eine unveränderliche und eine veränderliche Referenz auf `num` zu erstellen, wäre der Code nicht kompiliert, weil Rusts Besitzregeln nicht zulassen, dass eine veränderliche Referenz gleichzeitig mit irgendeiner unveränderlichen Referenz existiert. Mit rohen Zeigern können wir einen veränderlichen Zeiger und einen unveränderlichen Zeiger auf die gleiche Adresse erstellen und durch den veränderlichen Zeiger Daten ändern, was möglicherweise einen Datenkonflikt erzeugt. Vorsicht!

Mit all diesen Gefahren, warum würdest du überhaupt rohe Zeiger verwenden? Ein wichtiger Anwendungsfall ist die Schnittstelle mit C-Code, wie du im Abschnitt "Aufrufen einer unsicheren Funktion oder Methode" sehen wirst. Ein weiterer Fall ist die Erstellung sicherer Abstraktionen, die der Borrow-Checker nicht versteht. Wir werden unsichere Funktionen einführen und dann ein Beispiel einer sicheren Abstraktion betrachten, die unsafe Code verwendet.
