# Divergierende Funktionen

Divergierende Funktionen geben niemals zurück. Sie werden mit `!` markiert, was ein leerer Typ ist.

```rust
fn foo() ->! {
    panic!("Diese Funktion gibt nie zurück.");
}
```

Im Gegensatz zu allen anderen Typen kann dieser Typ nicht instanziiert werden, da die Menge aller möglichen Werte, die dieser Typ haben kann, leer ist. Beachten Sie, dass dies vom `()`-Typ unterschieden wird, der genau einen möglichen Wert hat.

Zum Beispiel gibt diese Funktion wie üblich zurück, obwohl kein Information in dem Rückgabewert enthalten ist.

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("Diese Funktion gibt zurück und Sie können diese Zeile sehen.");
}
```

Im Gegensatz zu dieser Funktion wird die Kontrolle niemals zurück an den Aufrufer gegeben.

```rust
#![feature(never_type)]

fn main() {
    let x:! = panic!("Diese Funktion gibt nie zurück.");
    println!("Sie werden diese Zeile nie sehen!");
}
```

Obwohl dies ein abstrakter Begriff erscheinen mag, ist er tatsächlich sehr nützlich und oft praktisch. Der Hauptvorteil dieses Typs ist, dass er in jeden anderen Typ umgewandelt werden kann und daher an Stellen verwendet werden kann, an denen ein bestimmter Typ erforderlich ist, beispielsweise in `match`-Zweigen. Dies ermöglicht es uns, Code wie diesen zu schreiben:

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // Beachten Sie, dass der Rückgabetyp dieses match-Ausdrucks u32 sein muss
            // aufgrund des Typs der "addition"-Variablen.
            let addition: u32 = match i%2 == 1 {
                // Die "i"-Variable ist vom Typ u32, was völlig in Ordnung ist.
                true => i,
                // Andererseits gibt der "continue"-Ausdruck kein u32 zurück,
                // aber es ist dennoch in Ordnung, da er niemals zurückkehrt und daher
                // die Typanforderungen des match-Ausdrucks nicht verletzt.
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Summe der ungeraden Zahlen bis 9 (ausschließlich): {}", sum_odd_numbers(9));
}
```

Es ist auch der Rückgabetyp von Funktionen, die für immer in einer Schleife verbleiben (z.B. `loop {}`), wie Netzwerkserver, oder Funktionen, die den Prozess beenden (z.B. `exit()`).
