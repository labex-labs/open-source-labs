# Ausdrücke

Ein Rust-Programm besteht (meistens) aus einer Reihe von Anweisungen:

```rust
fn main() {
    // Anweisung
    // Anweisung
    // Anweisung
}
```

Es gibt verschiedene Arten von Anweisungen in Rust. Zwei der häufigsten sind die Deklaration einer Variablebindung und das Verwenden eines `;` mit einem Ausdruck:

```rust
fn main() {
    // Variablebindung
    let x = 5;

    // Ausdruck;
    x;
    x + 1;
    15;
}
```

Blöcke sind ebenfalls Ausdrücke, sodass sie als Werte in Zuweisungen verwendet werden können. Der letzte Ausdruck im Block wird an den Ausdrucksort wie einer lokalen Variable zugewiesen. Wenn jedoch der letzte Ausdruck des Blocks mit einem Semikolon endet, ist der Rückgabewert `()`.

```rust
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Dieser Ausdruck wird an `y` zugewiesen
        x_cube + x_squared + x
    };

    let z = {
        // Das Semikolon unterdrückt diesen Ausdruck und `()` wird an `z` zugewiesen
        2 * x;
    };

    println!("x ist {:?}", x);
    println!("y ist {:?}", y);
    println!("z ist {:?}", z);
}
```
