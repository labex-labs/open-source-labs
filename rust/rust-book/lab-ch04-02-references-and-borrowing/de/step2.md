# Mutable Referenzen

Wir können den Code aus Listing 4-6 beheben, um es uns zu ermöglichen, einen entlehnten Wert zu modifizieren, indem wir nur einige kleine Änderungen vornehmen, die stattdessen eine _mutable Referenz_ verwenden:

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

Zunächst ändern wir `s` zu `mut`. Dann erstellen wir eine mutable Referenz mit `&mut s`, wo wir die `change`-Funktion aufrufen, und aktualisieren die Funktionssignatur, um eine mutable Referenz mit `some_string: &mut String` zu akzeptieren. Dies macht deutlich, dass die `change`-Funktion den Wert mutieren wird, den sie entleiht.

Mutable Referenzen haben eine große Einschränkung: Wenn Sie eine mutable Referenz zu einem Wert haben, können Sie keine anderen Referenzen zu diesem Wert haben. Dieser Code, der versucht, zwei mutable Referenzen zu `s` zu erstellen, wird fehlschlagen:

Dateiname: `src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

Hier ist der Fehler:

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

Dieser Fehler sagt aus, dass dieser Code ungültig ist, weil wir `s` nicht mehr als einmal als mutable entleihen können. Die erste mutable Entleihe ist in `r1` und muss bis zu ihrer Verwendung in der `println!` bestehen, aber zwischen der Erstellung dieser mutable Referenz und ihrer Verwendung haben wir versucht, eine weitere mutable Referenz in `r2` zu erstellen, die das gleiche Daten wie `r1` entleiht.

Die Einschränkung, die es verhindert, dass gleichzeitig mehrere mutable Referenzen zu den gleichen Daten existieren, ermöglicht die Mutation, aber in einem sehr kontrollierten Verfahren. Dies ist etwas, mit dem sich neue Rustaceans schwer tun, weil in den meisten Sprachen Sie jederzeit mutieren können. Der Vorteil dieser Einschränkung ist, dass Rust Laufzeitfehler bei der Kompilierung verhindern kann. Ein _Datenkonflikt_ ähnelt einem Wettlaufbedingung und tritt auf, wenn diese drei Verhaltensweisen auftreten:

- Zwei oder mehr Zeiger greifen gleichzeitig auf die gleichen Daten zu.
- Mindestens ein Zeiger wird verwendet, um auf die Daten zu schreiben.
- Es gibt kein Mechanismus, um den Zugang zu den Daten zu synchronisieren.

Datenkonflikte verursachen undefiniertes Verhalten und können schwierig zu diagnostizieren und zu beheben sein, wenn Sie versuchen, sie zur Laufzeit aufzuspüren; Rust verhindert dieses Problem, indem es Code mit Datenkonflikten nicht kompilieren lässt!

Wie immer können wir geschweifte Klammern verwenden, um einen neuen Gültigkeitsbereich zu erstellen, was mehrere mutable Referenzen ermöglicht, nur keine _gleichzeitigen_:

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // r1 geht hier außer Gültigkeitsbereich, so dass wir eine neue Referenz problemlos erstellen können

let r2 = &mut s;
```

Rust durchsetzt eine ähnliche Regel für die Kombination von mutable und immutable Referenzen. Dieser Code führt zu einem Fehler:

```rust
let mut s = String::from("hello");

let r1 = &s; // kein Problem
let r2 = &s; // kein Problem
let r3 = &mut s; // GROßES PROBLEM

println!("{r1}, {r2}, and {r3}");
```

Hier ist der Fehler:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // GROßES PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

Puh! Wir können auch keine mutable Referenz haben, wenn wir eine immutable Referenz zu demselben Wert haben.

Anwender einer immutable Referenz erwarten nicht, dass der Wert plötzlich von ihnen wegändert wird! Allerdings sind mehrere immutable Referenzen erlaubt, weil niemand, der nur die Daten liest, die Möglichkeit hat, das Lesen anderer Personen zu beeinflussen.

Beachten Sie, dass der Gültigkeitsbereich einer Referenz ab dem Punkt beginnt, an dem sie eingeführt wird, und bis zum letzten Mal, an dem diese Referenz verwendet wird. Beispielsweise wird dieser Code kompilieren, weil der letzte Gebrauch der immutable Referenzen, die `println!`, vor der Einführung der mutable Referenz erfolgt:

```rust
let mut s = String::from("hello");

let r1 = &s; // kein Problem
let r2 = &s; // kein Problem
println!("{r1} and {r2}");
// Variablen r1 und r2 werden nach diesem Punkt nicht mehr verwendet

let r3 = &mut s; // kein Problem
println!("{r3}");
```

Die Gültigkeitsbereiche der immutable Referenzen `r1` und `r2` enden nach der `println!`, wo sie zuletzt verwendet werden, was vor der Erstellung der mutable Referenz `r3` erfolgt. Diese Gültigkeitsbereiche überlappen sich nicht, daher ist dieser Code erlaubt: Der Compiler kann erkennen, dass die Referenz vor dem Ende des Gültigkeitsbereichs nicht mehr verwendet wird.

Auch wenn die Entleiherrors manchmal frustrierend sein können, denken Sie daran, dass es der Rust-Compiler ist, der frühzeitig (bei der Kompilierung statt bei der Laufzeit) ein potenzielles Bug aufzeigt und Ihnen genau anzeigt, wo das Problem ist. Dann müssen Sie nicht ermitteln, warum Ihre Daten nicht so sind, wie Sie dachten.
