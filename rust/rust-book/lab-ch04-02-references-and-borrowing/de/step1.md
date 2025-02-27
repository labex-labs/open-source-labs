# References and Borrowing

Das Problem mit dem Tupel-Code in Listing 4-5 besteht darin, dass wir die `String` an die aufrufende Funktion zurückgeben müssen, damit wir die `String` auch nach dem Aufruf von `calculate_length` noch verwenden können, da die `String` in `calculate_length` bewegt wurde. Stattdessen können wir eine Referenz auf den `String`-Wert bereitstellen. Eine _Referenz_ ist wie ein Zeiger, insofern es eine Adresse ist, die wir folgen können, um auf die an dieser Adresse gespeicherten Daten zuzugreifen; diese Daten werden von einer anderen Variable besessen. Im Gegensatz zu einem Zeiger ist garantiert, dass eine Referenz während ihrer Lebensdauer auf einen gültigen Wert eines bestimmten Typs zeigt.

Hier ist, wie Sie eine `calculate_length`-Funktion definieren und verwenden würden, die eine Referenz auf ein Objekt als Parameter hat, anstatt die Eigentumsgewalt über den Wert zu übernehmen:

Dateiname: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Zunächst bemerken Sie, dass der gesamte Tupel-Code in der Variablendeklaration und im Funktionsrückgabewert fehlt. Zweitens bemerken Sie, dass wir `&s1` an `calculate_length` übergeben und in seiner Definition `&String` statt `String` verwenden. Diese Ampersands stellen _Referenzen_ dar, und sie ermöglichen es Ihnen, auf einen Wert zu verweisen, ohne die Eigentumsgewalt darüber zu erwerben. Abbildung 4-5 veranschaulicht diesen Begriff.

Abbildung 4-5: Ein Diagramm von `&String s`, das auf `String s1` zeigt

> Hinweis: Das Gegenteil von der Referenzierung mit `&` ist die _Dereferenzierung_, die mit dem Dereferenzierungsoperator `*` erreicht wird. Wir werden einige Anwendungen des Dereferenzierungsoperators im Kapitel 8 sehen und die Details der Dereferenzierung im Kapitel 15 diskutieren.

Schauen wir uns den Funktionsaufruf hier genauer an:

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

Die Syntax `&s1` ermöglicht es uns, eine Referenz zu erstellen, die auf den Wert von `s1` _verweist_, aber ihn nicht besitzt. Da sie ihn nicht besitzt, wird der Wert, auf den sie zeigt, nicht gelöscht, wenn die Referenz nicht mehr verwendet wird.

Ebenso verwendet die Signatur der Funktion `&`, um anzuzeigen, dass der Typ des Parameters `s` eine Referenz ist. Fügen wir einige erklärende Anmerkungen hinzu:

```rust
fn calculate_length(s: &String) -> usize { // s ist eine Referenz auf eine String
    s.len()
} // Hier geht s außer Gültigkeitsbereich. Aber da es keine Eigentumsgewalt über das hat,
  // auf das es verweist, wird die String nicht gelöscht
```

Der Gültigkeitsbereich, in dem die Variable `s` gültig ist, ist der gleiche wie der eines beliebigen Funktionsparameters, aber der Wert, auf den die Referenz zeigt, wird nicht gelöscht, wenn `s` nicht mehr verwendet wird, weil `s` keine Eigentumsgewalt hat. Wenn Funktionen Referenzen als Parameter statt der tatsächlichen Werte haben, müssen wir die Werte nicht zurückgeben, um die Eigentumsgewalt zurückzugeben, weil wir nie die Eigentumsgewalt hatten.

Wir nennen die Aktion des Erstellens einer Referenz _Entleihen_. Wie im realen Leben können Sie etwas von jemandem entleihen, wenn er es besitzt. Wenn Sie fertig sind, müssen Sie es zurückgeben. Sie besitzen es nicht.

Was passiert also, wenn wir versuchen, etwas zu modifizieren, das wir entleihen? Versuchen Sie den Code in Listing 4-6. Vorabentschluß: Es funktioniert nicht!

Dateiname: `src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Listing 4-6: Versuch, einen entlehnten Wert zu modifizieren

Hier ist der Fehler:

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

Genau wie Variablen sind Referenzen standardmäßig unveränderlich. Wir dürfen etwas, auf das wir eine Referenz haben, nicht modifizieren.
