# Schöne `use`-Pfade erstellen

In Listing 7-11 hast du dich vielleicht gefragt, warum wir `use crate::front_of_house::hosting` angegeben haben und dann in `eat_at_restaurant` `hosting::add_to_waitlist` aufgerufen haben, anstatt den `use`-Pfad bis zur `add_to_waitlist`-Funktion hinzuschreiben, um das gleiche Ergebnis zu erzielen, wie in Listing 7-13.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}
```

Listing 7-13: Die `add_to_waitlist`-Funktion mit `use` in den Gültigkeitsbereich bringen, was nicht idiomatisch ist

Obwohl sowohl Listing 7-11 als auch Listing 7-13 die gleiche Aufgabe erfüllen, ist Listing 7-11 die idiomatische Weise, eine Funktion mit `use` in den Gültigkeitsbereich zu bringen. Das Bringen des Elternmoduls der Funktion mit `use` in den Gültigkeitsbereich bedeutet, dass wir das Elternmodul angeben müssen, wenn wir die Funktion aufrufen. Das Angabe des Elternmoduls beim Funktionsaufruf macht klar, dass die Funktion nicht lokal definiert ist, während die Wiederholung des vollen Pfads gleichzeitig minimiert wird. Der Code in Listing 7-13 ist unklar, wo `add_to_waitlist` definiert ist.

Andererseits ist es idiomatisch, den vollen Pfad anzugeben, wenn man Structs, Enums und andere Elemente mit `use` einführt. Listing 7-14 zeigt die idiomatische Weise, die `HashMap`-Struktur der Standardbibliothek in den Gültigkeitsbereich eines Binärcrates zu bringen.

Dateiname: `src/main.rs`

```rust
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
```

Listing 7-14: `HashMap` auf idiomatische Weise in den Gültigkeitsbereich bringen

Es gibt keinen starken Grund hinter dieser Idiomatik: Es ist einfach die Konvention, die sich herausgebildet hat, und die Leute sind daran gewöhnt, Rust-Code so zu lesen und zu schreiben.

Die Ausnahme von dieser Idiomatik besteht darin, wenn wir zwei Elemente mit demselben Namen mit `use`-Statements in den Gültigkeitsbereich bringen, weil Rust das nicht erlaubt. Listing 7-15 zeigt, wie man zwei `Result`-Typen mit demselben Namen, aber unterschiedlichen Elternmodulen, in den Gültigkeitsbereich bringt und wie man auf sie verweist.

Dateiname: `src/lib.rs`

```rust
use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    --snip--
}

fn function2() -> io::Result<()> {
    --snip--
}
```

Listing 7-15: Zwei Typen mit demselben Namen in denselben Gültigkeitsbereich bringen erfordert die Verwendung ihrer Elternmodule.

Wie du siehst, unterscheidet die Verwendung der Elternmodule die beiden `Result`-Typen. Wenn wir stattdessen `use std::fmt::Result` und `use std::io::Result` angegeben hätten, würden wir zwei `Result`-Typen im selben Gültigkeitsbereich haben, und Rust würde nicht wissen, welchen wir meinen, wenn wir `Result` verwenden.
