# Tupel

Ein Tupel ist eine Sammlung von Werten unterschiedlicher Typen. Tupel werden mit runden Klammern `()` konstruiert, und jedes Tupel selbst ist ein Wert mit dem Typsignatur `(T1, T2,...)`, wobei `T1`, `T2` die Typen seiner Elemente sind. Funktionen können Tupel verwenden, um mehrere Werte zurückzugeben, da Tupel beliebig viele Werte aufnehmen können.

```rust
// Tupel können als Funktionsargumente und als Rückgabewerte verwendet werden.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` kann verwendet werden, um die Elemente eines Tupels an Variablen zu binden.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// Die folgende Struktur ist für die Aufgabe.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // Ein Tupel mit einer Reihe unterschiedlicher Typen.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Werte können aus dem Tupel mit der Tupel-Indexierung extrahiert werden.
    println!("Erstes Wert des langen Tupels: {}", long_tuple.0);
    println!("Zweites Wert des langen Tupels: {}", long_tuple.1);

    // Tupel können Elemente von anderen Tupeln sein.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tupel sind druckbar.
    println!("Tupel von Tupeln: {:?}", tuple_of_tuples);

    // Aber lange Tupel (mehr als 12 Elemente) können nicht gedruckt werden.
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Zu langes Tupel: {:?}", too_long_tuple);
    // TODO ^ Entkommentieren Sie die obigen 2 Zeilen, um den Compilerfehler zu sehen

    let pair = (1, true);
    println!("Das Paar ist {:?}", pair);

    println!("Das umgekehrte Paar ist {:?}", reverse(pair));

    // Um ein Tupel mit einem Element zu erstellen, ist das Komma erforderlich, um es
    // von einem Literal, das von Klammern umgeben ist, zu unterscheiden.
    println!("Tupel mit einem Element: {:?}", (5u32,));
    println!("Nur eine Ganzzahl: {:?}", (5u32));

    // Tupel können dekonstruiert werden, um Bindungen zu erstellen.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## Aufgabe

1.  _Wiederholung_: Fügen Sie das `fmt::Display`-Attribut zur `Matrix`-Struktur im obigen Beispiel hinzu, so dass wenn Sie von der Ausgabe im Debug-Format `{:?}` zur Ausgabe im Anzeigeformat `{}` wechseln, Sie die folgende Ausgabe erhalten:

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    Sie können sich an das Beispiel zur Ausgabe im Anzeigeformat erinnern.

2.  Fügen Sie eine `transpose`-Funktion hinzu, die die `reverse`-Funktion als Vorlage verwendet, die einen Matrix als Argument akzeptiert und eine Matrix zurückgibt, in der zwei Elemente getauscht wurden. Beispielsweise:

    ```rust
    println!("Matrix:\n{}", matrix);
    println!("Transponiert:\n{}", transpose(matrix));
    ```

    Dies führt zu der Ausgabe:

    ```plaintext
    Matrix:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transponiert:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
