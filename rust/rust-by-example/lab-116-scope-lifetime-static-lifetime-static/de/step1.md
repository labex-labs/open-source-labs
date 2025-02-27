# Statisch

Rust hat einige reservierte Lebensdauerbezeichnungen. Eine davon ist `'static`. Sie können es in zwei Situationen antrennen:

```rust
// Ein Verweis mit 'static Lebensdauer:
let s: &'static str = "hello world";

// 'static als Teil einer Trait-Bedingung:
fn generic<T>(x: T) where T: 'static {}
```

Beide sind verwandt, aber subtil unterschiedlich, und dies ist eine häufige Quelle der Verwirrung, wenn man Rust lernt. Hier sind einige Beispiele für jede Situation:

## Verweislebensdauer

Als Verweislebensdauer gibt `'static` an, dass die von dem Verweis bezeichneten Daten für die gesamte Lebensdauer des laufenden Programms existieren. Es kann jedoch immer noch auf eine kürzere Lebensdauer umgewandelt werden.

Es gibt zwei Möglichkeiten, eine Variable mit `'static` Lebensdauer zu erstellen, und beide werden im schreibgeschützten Speicher des Binärprogramms gespeichert:

- Erstellen Sie eine Konstante mit der `static`-Deklaration.
- Erstellen Sie einen `string`-Literal, der den Typ `&'static str` hat.

Siehe folgendes Beispiel für eine Darstellung jeder Methode:

```rust
// Erstellen Sie eine Konstante mit 'static Lebensdauer.
static NUM: i32 = 18;

// Gibt einen Verweis auf `NUM` zurück, wobei seine `'static`
// Lebensdauer auf die des Eingabearguments umgewandelt wird.
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // Erstellen Sie einen `string`-Literal und drucken Sie ihn:
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // Wenn `static_string` außerhalb des Gültigkeitsbereichs tritt, kann der Verweis
        // nicht mehr verwendet werden, aber die Daten verbleiben im Binärprogramm.
    }

    {
        // Erstellen Sie eine Ganzzahl, um sie für `coerce_static` zu verwenden:
        let lifetime_num = 9;

        // Wandeln Sie `NUM` in die Lebensdauer von `lifetime_num` um:
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} bleibt zugänglich!", NUM);
}
```

## Trait-Bedingung

Als Trait-Bedingung bedeutet es, dass der Typ keine nicht-statischen Verweise enthält. Beispielsweise kann der Empfänger das Objekt so lange behalten, wie er möchte, und es wird nie ungültig, bis er es ableitet.

Es ist wichtig zu verstehen, dass dies bedeutet, dass alle eigenen Daten immer eine `'static` Lebensdauerbedingung erfüllen, aber ein Verweis auf diese eigenen Daten erfüllt dies im Allgemeinen nicht:

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // i ist eine eigene Variable und enthält keine Verweise, daher ist es 'static:
    let i = 5;
    print_it(i);

    // Ups, &i hat nur die Lebensdauer, die durch den Gültigkeitsbereich von
    // main() definiert ist, daher ist es nicht 'static:
    print_it(&i);
}
```

Der Compiler wird Ihnen sagen:

```ignore
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed
```
