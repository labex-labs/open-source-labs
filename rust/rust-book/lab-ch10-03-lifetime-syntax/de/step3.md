# The Borrow Checker

Der Rust-Compiler hat einen _Borrow-Checker_, der die Bereiche vergleicht, um zu bestimmen, ob alle Entleihen gültig sind. Listing 10-17 zeigt denselben Code wie Listing 10-16, aber mit Anmerkungen, die die Lebenszeiten der Variablen anzeigen.

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

Listing 10-17: Anmerkungen zu den Lebenszeiten von `r` und `x`, benannt `'a` und `'b` respective

Hier haben wir die Lebenszeit von `r` mit `'a` und die Lebenszeit von `x` mit `'b` annotiert. Wie Sie sehen können, ist der innere `'b`-Block viel kleiner als der äußere `'a`-Lebenszeit-Block. Zur Compile-Zeit vergleicht Rust die Größe der beiden Lebenszeiten und sieht, dass `r` eine Lebenszeit von `'a` hat, aber dass es auf Speicher mit einer Lebenszeit von `'b` verweist. Das Programm wird abgelehnt, weil `'b` kürzer als `'a` ist: Das Objekt der Referenz lebt nicht so lange wie die Referenz.

Listing 10-18 behebt den Code, sodass er keinen verhängenden Verweis hat und ohne Fehler kompiliert.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Listing 10-18: Eine gültige Referenz, weil die Daten eine längere Lebenszeit als die Referenz haben

Hier hat `x` die Lebenszeit `'b`, die in diesem Fall größer als `'a` ist. Dies bedeutet, dass `r` `x` referenzieren kann, weil Rust weiß, dass die Referenz in `r` immer gültig sein wird, solange `x` gültig ist.

Jetzt, da Sie wissen, wo die Lebenszeiten von Referenzen sind und wie Rust Lebenszeiten analysiert, um sicherzustellen, dass Referenzen immer gültig sind, werden wir die generischen Lebenszeiten von Parametern und Rückgabewerten im Kontext von Funktionen untersuchen.
