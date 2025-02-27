# Elision

Einige Lebenszeitmuster sind überwältigend häufig, sodass der Borrow-Checker Ihnen erlaubt, sie zu weglassen, um die Tipparbeit zu sparen und die Lesbarkeit zu verbessern. Dies wird als Elision bezeichnet. Elision existiert in Rust lediglich, weil diese Muster häufig sind.

Der folgende Code zeigt einige Beispiele für Elision. Für eine umfassendere Beschreibung von Elision siehe Lebenszeitelision im Buch.

```rust
// `elided_input` und `annotated_input` haben im Wesentlichen identische Signaturen,
// weil die Lebenszeit von `elided_input` vom Compiler inferiert wird:
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x);
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x);
}

// Ähnlich haben `elided_pass` und `annotated_pass` identische Signaturen,
// weil die Lebenszeit implizit zu `elided_pass` hinzugefügt wird:
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}
```
