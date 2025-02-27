# Funktionen

Funktionen werden mit dem Schlüsselwort `fn` deklariert. Ihre Argumente werden wie Variablen mit Typangaben versehen, und wenn die Funktion einen Wert zurückgibt, muss der Rückgabetyp nach einer Pfeilrichtung `->` angegeben werden.

Der letzte Ausdruck in der Funktion wird als Rückgabewert verwendet. Alternativ kann der `return`-Befehl verwendet werden, um einen Wert früher aus der Funktion zurückzugeben, sogar aus innerhalb von Schleifen oder `if`-Anweisungen.

Schreiben wir FizzBuzz mit Funktionen um!

```rust
// Im Gegensatz zu C/C++ gibt es keine Einschränkung für die Reihenfolge der Funktionsdefinitionen
fn main() {
    // Wir können diese Funktion hier verwenden und sie später irgendwo definieren
    fizzbuzz_to(100);
}

// Funktion, die einen booleschen Wert zurückgibt
fn is_divisible_by(lhs: u32, rhs: u32) -> bool {
    // Sonderfall, frühzeitiger Rückgabewert
    if rhs == 0 {
        return false;
    }

    // Dies ist ein Ausdruck, das `return`-Schlüsselwort ist hier nicht erforderlich
    lhs % rhs == 0
}

// Funktionen, die "keinen" Wert zurückgeben, geben tatsächlich den Einheitstyp `()` zurück
fn fizzbuzz(n: u32) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

// Wenn eine Funktion `()` zurückgibt, kann der Rückgabetyp aus der
// Signatur weggelassen werden
fn fizzbuzz_to(n: u32) {
    for n in 1..=n {
        fizzbuzz(n);
    }
}
```
