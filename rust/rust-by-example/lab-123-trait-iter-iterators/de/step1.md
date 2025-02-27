# Iteratoren

Das `Iterator`-Trait wird verwendet, um Iteratoren über Sammlungen wie Arrays zu implementieren.

Das Trait erfordert nur, dass eine Methode für das `next`-Element definiert wird, die entweder manuell in einem `impl`-Block definiert oder automatisch definiert werden kann (wie bei Arrays und Bereichen).

Als praktische Abkürzung für häufige Situationen verwandelt die `for`-Konstruktion einige Sammlungen in Iteratoren mit der `.into_iter()`-Methode.

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// Implementiere `Iterator` für `Fibonacci`.
// Das `Iterator`-Trait erfordert nur, dass eine Methode für das `next`-Element definiert wird.
impl Iterator for Fibonacci {
    // Wir können diesen Typ mit Self::Item referenzieren.
    type Item = u32;

    // Hier definieren wir die Sequenz mit `.curr` und `.next`.
    // Der Rückgabetyp ist `Option<T>`:
    //     * Wenn der `Iterator` beendet ist, wird `None` zurückgegeben.
    //     * Andernfalls wird der nächste Wert in `Some` verpackt und zurückgegeben.
    // Wir verwenden Self::Item im Rückgabetyp, so dass wir den Typ ändern können,
    // ohne die Funktionssignaturen aktualisieren zu müssen.
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // Da es kein Endpunkt für eine Fibonacci-Sequenz gibt, wird der `Iterator`
        // niemals `None` zurückgeben, und `Some` wird immer zurückgegeben.
        Some(current)
    }
}

// Gibt einen Fibonacci-Sequenzgenerator zurück.
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` ist ein `Iterator`, der 0, 1 und 2 generiert.
    let mut sequence = 0..3;

    println!("Vier aufeinanderfolgende `next`-Aufrufe auf 0..3");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` iteriert über einen `Iterator`, bis er `None` zurückgibt.
    // Jeder `Some`-Wert wird entpackt und an eine Variable gebunden (hier `i`).
    println!("Iteriere über 0..3 mit `for`");
    for i in 0..3 {
        println!("> {}", i);
    }

    // Die `take(n)`-Methode reduziert einen `Iterator` auf seine ersten `n` Elemente.
    println!("Die ersten vier Elemente der Fibonacci-Sequenz sind: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // Die `skip(n)`-Methode kürzt einen `Iterator` ab, indem sie seine ersten `n` Elemente weglässt.
    println!("Die nächsten vier Elemente der Fibonacci-Sequenz sind: ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // Die `iter`-Methode erzeugt einen `Iterator` über ein Array/Slice.
    println!("Iteriere das folgende Array {:?}", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
