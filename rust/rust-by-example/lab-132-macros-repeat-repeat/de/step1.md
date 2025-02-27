# Wiederholung

Makros können in der Argumentliste `+` verwenden, um anzuzeigen, dass ein Argument mindestens einmal wiederholt werden kann, oder `*`, um anzuzeigen, dass das Argument null oder mehrmals wiederholt werden kann.

Im folgenden Beispiel wird das Matcher mit `$(...),+` umgeben, um eine oder mehrere Ausdrücke zu treffen, die durch Kommas getrennt sind. Beachten Sie auch, dass das Semikolon im letzten Fall optional ist.

```rust
// `find_min!` wird den kleinsten Wert von beliebig vielen Argumenten berechnen.
macro_rules! find_min {
    // Basisfall:
    ($x:expr) => ($x);
    // `$x` gefolgt von mindestens einem `$y,`
    ($x:expr, $($y:expr),+) => (
        // Rufen Sie `find_min!` auf dem Rest `$y` auf
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1));
    println!("{}", find_min!(1 + 2, 2));
    println!("{}", find_min!(5, 2 * 3, 4));
}
```
