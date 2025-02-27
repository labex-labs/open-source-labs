# String-Slices

Ein _String-Slice_ ist eine Referenz auf einen Teil eines `String`, und es sieht so aus:

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

Anstatt eine Referenz auf den gesamten `String` zu sein, ist `hello` eine Referenz auf einen Teil des `String`, wie im zusätzlichen `[0..5]`-Teil angegeben. Wir erstellen Slices, indem wir einen Bereich innerhalb von eckigen Klammern angeben, indem wir `[starting_index..ending_index]` angeben, wobei `starting_index` die erste Position im Slice ist und `ending_index` um eins größer als die letzte Position im Slice ist. Intern speichert die Slice-Datenstruktur die Startposition und die Länge des Slices, was entspricht `ending_index` minus `starting_index`. Also im Fall von `let world = &s[6..11];` wäre `world` ein Slice, der einen Zeiger auf das Byte an Index 6 von `s` mit einem Längenwert von `5` enthält.

Abbildung 4-6 zeigt dies in einem Diagramm.

Abbildung 4-6: String-Slice, der auf einen Teil eines `String` verweist

Mit Rusts `..`-Bereichssyntax können Sie, wenn Sie bei Index 0 beginnen möchten, den Wert vor den beiden Punkten weglassen. Mit anderen Worten, diese sind gleich:

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

Aus dem gleichen Grund können Sie, wenn Ihr Slice das letzte Byte des `String` enthält, die nachfolgende Zahl weglassen. Das bedeutet, dass diese gleich sind:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

Sie können auch beide Werte weglassen, um einen Slice des gesamten Strings zu nehmen. Also sind diese gleich:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> Hinweis: String-Slice-Bereichsindizes müssen an gültigen UTF-8-Zeichengrenzen auftreten. Wenn Sie versuchen, einen String-Slice mitten in einem Mehrbyte-Zeichen zu erstellen, wird Ihr Programm mit einem Fehler beendet. Im Rahmen der Einführung von String-Slices nehmen wir in diesem Abschnitt nur ASCII an; Eine umfassendere Diskussion der UTF-8-Bearbeitung finden Sie in "Speichern von UTF-8-kodiertem Text mit Strings".

Mit all dieser Information im Kopf lassen Sie uns `first_word` umschreiben, um einen Slice zurückzugeben. Der Typ, der "String-Slice" bedeutet, wird als `&str` geschrieben:

Dateiname: `src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Wir erhalten den Index für das Ende des Worts auf die gleiche Weise wie in Listing 4-7, indem wir nach dem ersten Vorkommen eines Leerzeichens suchen. Wenn wir ein Leerzeichen finden, geben wir einen String-Slice zurück, indem wir den Anfang des Strings und den Index des Leerzeichens als Start- und Endindizes verwenden.

Wenn wir jetzt `first_word` aufrufen, erhalten wir einen einzelnen Wert zurück, der an die zugrunde liegenden Daten gebunden ist. Der Wert besteht aus einer Referenz auf den Startpunkt des Slices und der Anzahl der Elemente im Slice.

Das Zurückgeben eines Slices würde auch für eine `second_word`-Funktion funktionieren:

```rust
fn second_word(s: &String) -> &str {
```

Wir haben jetzt eine einfache API, die viel schwerer zu verwechseln ist, weil der Compiler sicherstellt, dass die Referenzen in den `String` gültig bleiben. Denken Sie sich den Bug im Programm in Listing 4-8 noch einmal vor, als wir den Index zum Ende des ersten Worts erhalten haben, aber dann den String geleert haben, sodass unser Index ungültig war? Dieser Code war logisch falsch, zeigte aber keine unmittelbaren Fehler. Die Probleme würden später auftauchen, wenn wir weiterhin versuchten, den Index des ersten Worts mit einem geleerten String zu verwenden. Slices machen diesen Bug unmöglich und lassen uns viel früher wissen, dass wir ein Problem mit unserem Code haben. Das Verwenden der Slice-Version von `first_word` wird einen Kompilierfehler auslösen:

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // Fehler!

    println!("the first word is: {word}");
}
```

Hier ist der Kompilierfehler:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {word}");
   |                                   ---- immutable borrow later used here
```

Denken Sie sich die Leihregeln noch einmal vor, dass wir, wenn wir eine unveränderliche Referenz auf etwas haben, keine veränderliche Referenz auch noch nehmen können. Da `clear` den `String` kürzen muss, muss er eine veränderliche Referenz erhalten. Die `println!` nach dem Aufruf von `clear` verwendet die Referenz in `word`, sodass die unveränderliche Referenz zu diesem Zeitpunkt noch aktiv sein muss. Rust verbietet die veränderliche Referenz in `clear` und die unveränderliche Referenz in `word`, dass sie gleichzeitig existieren, und die Kompilierung scheitert. Nicht nur hat Rust unsere API einfacher zu verwenden gemacht, sondern es hat auch eine ganze Klasse von Fehlern zur Compile-Zeit eliminiert!
