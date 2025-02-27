# Numerische Operationen

Rust unterstützt die grundlegenden mathematischen Operationen, die man von allen Zahlentypen erwarten würde: Addition, Subtraktion, Multiplikation, Division und Rest. Die Ganzzahldivision wird nach Null abgeschnitten auf die nächste ganze Zahl. Der folgende Code zeigt, wie man jede numerische Operation in einer `let`-Anweisung verwendet:

Dateiname: `src/main.rs`

```rust
fn main() {
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // Resultiert in -1

    // remainder
    let remainder = 43 % 5;
}
```

Jeder Ausdruck in diesen Anweisungen verwendet einen mathematischen Operator und ausgewertet zu einem einzelnen Wert, der dann an eine Variable gebunden wird. Anhang B enthält eine Liste aller Operatoren, die Rust zur Verfügung stellt.
