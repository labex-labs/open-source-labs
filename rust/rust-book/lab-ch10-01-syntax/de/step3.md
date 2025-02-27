# In Funktionsdefinitionen

Wenn wir eine Funktion definieren, die Generics verwendet, platzieren wir die Generics in der Signatur der Funktion, wo wir normalerweise die Datentypen der Parameter und des Rückgabewerts angeben würden. Dadurch wird unser Code flexibler und bietet unseren Funktionsaufrufern mehr Funktionalität, während gleichzeitig Code-Duplizierung vermieden wird.

Fortfahrend mit unserer `largest`-Funktion zeigt Listing 10-4 zwei Funktionen, die beide den größten Wert in einer Slice finden. Anschließend kombinieren wir diese zu einer einzigen Funktion, die Generics verwendet.

Dateiname: `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-4: Zwei Funktionen, die sich nur in ihren Namen und in den Typen in ihren Signaturen unterscheiden

Die `largest_i32`-Funktion ist die, die wir in Listing 10-3 extrahiert haben, die den größten `i32` in einer Slice findet. Die `largest_char`-Funktion findet den größten `char` in einer Slice. Die Funktionskörper haben denselben Code, also eliminieren wir die Duplikation, indem wir einen generischen Typparameter in einer einzigen Funktion einführen.

Um die Typen in einer neuen einzigen Funktion zu parametrisieren, müssen wir den Typparameter benennen, genauso wie wir es für die Wertparameter einer Funktion tun. Sie können jedes beliebige Bezeichner als Typparametername verwenden. Wir werden jedoch `T` verwenden, weil es nach Konvention in Rust üblich ist, Typparameternamen kurz zu wählen, oft nur einen Buchstaben, und Rusts Typennennkonvention ist CamelCase. Kurz für _Typ_, `T` ist die Standardauswahl der meisten Rust-Programmierer.

Wenn wir einen Parameter im Funktionskörper verwenden, müssen wir den Parameternamen in der Signatur deklarieren, damit der Compiler weiß, was dieser Name bedeutet. Ähnlich müssen wir den Typparameternamen in einer Funktionssignatur deklarieren, bevor wir ihn verwenden. Um die generische `largest`-Funktion zu definieren, platzieren wir die Typnamen-Deklarationen innerhalb von eckigen Klammern, `<>` zwischen dem Funktionsnamen und der Parameterliste, wie folgt:

```rust
fn largest<T>(list: &[T]) -> &T {
```

Wir lesen diese Definition wie folgt: Die Funktion `largest` ist generisch über einen bestimmten Typ `T`. Diese Funktion hat einen Parameter namens `list`, der eine Slice von Werten vom Typ `T` ist. Die `largest`-Funktion wird eine Referenz auf einen Wert vom gleichen Typ `T` zurückgeben.

Listing 10-5 zeigt die kombinierte `largest`-Funktionsdefinition, die den generischen Datentyp in ihrer Signatur verwendet. Die Liste zeigt auch, wie wir die Funktion mit einer Slice von `i32`-Werten oder `char`-Werten aufrufen können. Beachten Sie, dass dieser Code noch nicht kompilieren wird, aber wir werden ihn später in diesem Kapitel beheben.

Dateiname: `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Listing 10-5: Die `largest`-Funktion mit generischen Typparametern; dies kompiliert noch nicht

Wenn wir diesen Code gerade kompilieren, erhalten wir diesen Fehler:

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

Der Hilfetext erwähnt `std::cmp::PartialOrd`, was ein _Trait_ ist, und wir werden im nächsten Abschnitt über Traits sprechen. Für jetzt wissen Sie, dass dieser Fehler angibt, dass der Körper von `largest` nicht für alle möglichen Typen funktionieren wird, auf die `T` sein könnte. Da wir in der Funktion Werte vom Typ `T` vergleichen möchten, können wir nur Typen verwenden, deren Werte geordnet werden können. Um Vergleiche zu ermöglichen, hat die Standardbibliothek das `std::cmp::PartialOrd`-Trait, das Sie auf Typen implementieren können (siehe Anhang C für mehr Informationen zu diesem Trait). Indem wir der Vorschrift im Hilfetext folgen, beschränken wir die gültigen Typen für `T` auf nur diejenigen, die `PartialOrd` implementieren, und dieses Beispiel wird kompilieren, da die Standardbibliothek `PartialOrd` sowohl für `i32` als auch für `char` implementiert.
