# Variablen und Daten, die mit Move interagieren

In Rust können mehrere Variablen auf die gleichen Daten auf verschiedene Weise zugreifen. Schauen wir uns ein Beispiel mit einem Integer in Listing 4-2 an.

```rust
let x = 5;
let y = x;
```

Listing 4-2: Zuweisen des ganzzahligen Werts von Variable `x` an `y`

Wir können wahrscheinlich raten, was hier passiert: "Binde den Wert `5` an `x`; kopiere dann den Wert in `x` und binde ihn an `y`." Wir haben jetzt zwei Variablen, `x` und `y`, und beide sind gleich `5`. Tatsächlich passiert genau das, weil Integer einfache Werte mit einer bekannten, festen Größe sind, und diese beiden `5`-Werte werden auf den Stapel gelegt.

Schauen wir uns jetzt die `String`-Version an:

```rust
let s1 = String::from("hello");
let s2 = s1;
```

Dies sieht sehr ähnlich aus, also könnten wir annehmen, dass es auf die gleiche Weise funktioniert: dass heißt, die zweite Zeile würde einen Kopie des Werts in `s1` erstellen und ihn an `s2` binden. Dies ist jedoch nicht ganz, was passiert.

Schauen Sie sich Abbildung 4-1 an, um zu sehen, was mit `String` im Hintergrund passiert. Ein `String` besteht aus drei Teilen, wie auf der linken Seite gezeigt: Ein Zeiger auf den Arbeitsspeicher, der den Inhalt des Strings enthält, eine Länge und eine Kapazität. Diese Datengruppe wird auf dem Stapel gespeichert. Rechts ist der Arbeitsspeicher auf dem Heap, der den Inhalt enthält.

Abbildung 4-1: Darstellung im Arbeitsspeicher eines `String`s, der den Wert `"hello"` an `s1` bindet

Die Länge ist die Anzahl der Bytes, die der Inhalt des `String`s derzeit verwendet. Die Kapazität ist die Gesamtanzahl der Bytes, die der `String` vom Arbeitsspeicherzuweisungsdienst erhalten hat. Der Unterschied zwischen Länge und Kapazität ist wichtig, aber in diesem Zusammenhang nicht relevant, also können wir die Kapazität vorerst ignorieren.

Wenn wir `s1` an `s2` zuweisen, wird die `String`-Daten kopiert, was bedeutet, dass wir den Zeiger, die Länge und die Kapazität, die auf dem Stapel sind, kopieren. Wir kopieren jedoch nicht die Daten auf dem Heap, auf die der Zeiger verweist. Mit anderen Worten, die Datenrepräsentation im Arbeitsspeicher sieht wie in Abbildung 4-2 aus.

Abbildung 4-2: Darstellung im Arbeitsspeicher der Variable `s2`, die eine Kopie des Zeigers, der Längen und der Kapazität von `s1` hat

Die Darstellung sieht _nicht_ wie in Abbildung 4-3 aus, was der Arbeitsspeicher so aussehen würde, wenn Rust auch die Heap-Daten kopierte. Wenn Rust dies tun würde, könnte die Operation `s2 = s1` in Bezug auf die Laufzeitleistung sehr aufwendig sein, wenn die Daten auf dem Heap groß wären.

Abbildung 4-3: Eine andere Möglichkeit, was `s2 = s1` tun könnte, wenn Rust auch die Heap-Daten kopierte

Früher haben wir gesagt, dass wenn eine Variable außerhalb ihres Gültigkeitsbereichs fällt, Rust automatisch die `drop`-Funktion aufruft und den Heap-Arbeitsspeicher für diese Variable bereinigt. Aber Abbildung 4-2 zeigt, dass beide Datenzeiger auf die gleiche Stelle zeigen. Dies ist ein Problem: wenn `s2` und `s1` außerhalb ihres Gültigkeitsbereichs fallen, werden beide versuchen, den gleichen Arbeitsspeicher freizugeben. Dies wird als _double free_ -Fehler bezeichnet und ist ein von den zuvor genannten Arbeitsspeichersicherheitsfehlern. Das Doppelte Freigeben von Arbeitsspeicher kann zu einer Arbeitsspeicherfehler führen, was möglicherweise zu Sicherheitslücken führen kann.

Um die Arbeitsspeichersicherheit zu gewährleisten, betrachtet Rust nach der Zeile `let s2 = s1;` `s1` als nicht mehr gültig. Daher muss Rust nichts freigeben, wenn `s1` außerhalb seines Gültigkeitsbereichs fällt. Schauen Sie sich an, was passiert, wenn Sie versuchen, `s1` nach der Erstellung von `s2` zu verwenden; es wird nicht funktionieren:

```rust
let s1 = String::from("hello");
let s2 = s1;

println!("{s1}, world!");
```

Sie erhalten einen Fehler wie diesen, weil Rust Sie daran hindert, auf die ungültige Referenz zuzugreifen:

```bash
error[E0382]: borrow of moved value: `s1`
 --> src/main.rs:5:28
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which
 does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |
5 |     println!("{s1}, world!");
  |                ^^ value borrowed here after move
```

Wenn Sie die Begriffe _shallow copy_ und _deep copy_ in anderen Sprachen gehört haben, klingt das Konzept des Kopierens des Zeigers, der Längen und der Kapazität ohne das Kopieren der Daten wahrscheinlich wie das Erstellen einer shallow copy. Aber weil Rust auch die erste Variable ungültig macht, wird es nicht als shallow copy bezeichnet, sondern als _move_. In diesem Beispiel würden wir sagen, dass `s1` in `s2` _verschoben_ wurde. Was tatsächlich passiert, ist in Abbildung 4-4 gezeigt.

Abbildung 4-4: Darstellung im Arbeitsspeicher nach der Ungültigkeit von `s1`

Das löst unser Problem! Mit nur `s2` gültig, wird es, wenn es außerhalb seines Gültigkeitsbereichs fällt, allein den Arbeitsspeicher freigeben, und wir sind fertig.

Zusätzlich gibt es eine Designentscheidung, die hier impliziert ist: Rust wird niemals automatisch "tiefe" Kopien Ihrer Daten erstellen. Daher kann angenommen werden, dass jede _automatische_ Kopie in Bezug auf die Laufzeitleistung kostengünstig ist.
