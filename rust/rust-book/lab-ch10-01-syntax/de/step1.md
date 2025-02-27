# Entfernen von Duplikaten durch Extrahieren einer Funktion

Generics ermöglichen es uns, spezifische Typen durch einen Platzhalter zu ersetzen, der mehrere Typen repräsentiert, um Code-Duplizierung zu entfernen. Bevor wir uns der Generics-Syntax widmen, schauen wir uns zunächst an, wie wir Duplikate auf eine Weise entfernen, die keine generischen Typen involviert, indem wir eine Funktion extrahieren, die spezifische Werte durch einen Platzhalter ersetzt, der mehrere Werte repräsentiert. Anschließend wenden wir die gleiche Technik an, um eine generische Funktion zu extrahieren! Indem wir uns ansehen, wie man duplizierten Code erkennt, den man in eine Funktion extrahieren kann, werden wir beginnen, duplizierten Code zu erkennen, der generics verwenden kann.

Wir beginnen mit dem kurzen Programm in Listing 10-1, das die größte Zahl in einer Liste findet.

Dateiname: `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-1: Finden der größten Zahl in einer Liste von Zahlen

Wir speichern eine Liste von ganzen Zahlen in der Variable `number_list` \[1\] und legen eine Referenz auf die erste Zahl in der Liste in einer Variable namens `largest` fest \[2\]. Anschließend iterieren wir über alle Zahlen in der Liste \[3\], und wenn die aktuelle Zahl größer ist als die Zahl, die in `largest` gespeichert ist \[4\], ersetzen wir die Referenz in dieser Variable \[5\]. Wenn die aktuelle Zahl jedoch kleiner oder gleich der bisher größten Zahl ist, ändert sich die Variable nicht, und der Code geht zur nächsten Zahl in der Liste über. Nachdem alle Zahlen in der Liste betrachtet wurden, sollte `largest` auf die größte Zahl verweisen, was in diesem Fall 100 ist.

Wir haben nun die Aufgabe, die größte Zahl in zwei verschiedenen Listen von Zahlen zu finden. Um dies zu tun, können wir uns entscheiden, den Code in Listing 10-1 zu duplizieren und die gleiche Logik an zwei verschiedenen Stellen im Programm zu verwenden, wie in Listing 10-2 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Listing 10-2: Code, um die größte Zahl in _zwei_ Listen von Zahlen zu finden

Obwohl dieser Code funktioniert, ist das Duplizieren von Code langwierig und fehleranfällig. Wir müssen auch daran denken, den Code an mehreren Stellen zu aktualisieren, wenn wir ihn ändern möchten.

Um diese Duplikation zu eliminieren, werden wir eine Abstraktion erstellen, indem wir eine Funktion definieren, die auf jeder Liste von ganzen Zahlen operiert, die als Parameter übergeben wird. Diese Lösung macht unseren Code klarer und ermöglicht es uns, das Konzept des Findens der größten Zahl in einer Liste abstrakt auszudrücken.

In Listing 10-3 extrahieren wir den Code, der die größte Zahl findet, in eine Funktion namens `largest`. Anschließend rufen wir die Funktion auf, um die größte Zahl in den beiden Listen aus Listing 10-2 zu finden. Wir könnten auch die Funktion auf jeder anderen Liste von `i32`-Werten verwenden, die wir in Zukunft haben könnten.

Dateiname: `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
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

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

Listing 10-3: Abstrahierter Code, um die größte Zahl in zwei Listen zu finden

Die `largest`-Funktion hat einen Parameter namens `list`, der jede konkrete Slice von `i32`-Werten repräsentiert, die wir in die Funktion übergeben könnten. Folglich wird der Code, wenn wir die Funktion aufrufen, auf den spezifischen Werten ausgeführt, die wir übergeben.

Zusammenfassend betrachtet, hier sind die Schritte, die wir durchgeführt haben, um den Code von Listing 10-2 zu Listing 10-3 zu ändern:

1.  Identifizieren Sie duplizierten Code.
2.  Extrahieren Sie den duplizierten Code in den Funktionskörper und geben Sie die Eingaben und Rückgabewerte dieses Codes in der Funktionssignatur an.
3.  Aktualisieren Sie die beiden Instanzen des duplizierten Codes, um die Funktion stattdessen aufzurufen.

Als nächstes werden wir diese gleichen Schritte mit Generics verwenden, um die Code-Duplizierung zu reduzieren. Auf die gleiche Weise wie der Funktionskörper auf eine abstrakte `list` anstelle von spezifischen Werten operieren kann, ermöglichen Generics es Code, auf abstrakte Typen zu operieren.

Zum Beispiel hätten wir zwei Funktionen: eine, die das größte Element in einer Slice von `i32`-Werten findet, und eine, die das größte Element in einer Slice von `char`-Werten findet. Wie würden wir diese Duplikation eliminieren? Lassen Sie uns es herausfinden!
