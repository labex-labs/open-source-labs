# Zwangsumwandlung

Eine längere Lebensdauer kann in eine kürzere umgewandelt werden, sodass sie innerhalb eines Bereichs funktioniert, in dem sie normalerweise nicht funktionieren würde. Dies erfolgt in Form der von Rust-Compiler inferierten Zwangsumwandlung und auch in Form der Angabe eines Lebensdauerunterschieds:

```rust
// Hier schließt Rust eine so kurze wie möglich Lebensdauer ab.
// Die beiden Referenzen werden dann in diese Lebensdauer umgewandelt.
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>` bedeutet, dass die Lebensdauer `'a` mindestens so lang wie `'b` ist.
// Hier nehmen wir eine `&'a i32` entgegen und geben als Ergebnis einer Zwangsumwandlung eine `&'b i32` zurück.
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // Längere Lebensdauer

    {
        let second = 3; // Kürzere Lebensdauer

        println!("Das Produkt ist {}", multiply(&first, &second));
        println!("{} ist das erste", choose_first(&first, &second));
    };
}
```
