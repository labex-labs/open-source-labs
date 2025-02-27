# Tuples

Tuples können in einer `match` wie folgt zerlegt werden:

```rust
fn main() {
    let triple = (0, -2, 3);
    // TODO ^ Versuche verschiedene Werte für `triple`

    println!("Erzähl mir etwas über {:?}", triple);
    // Match kann verwendet werden, um ein Tuple zu zerlegen
    match triple {
        // Zerlege das zweite und dritte Element
        (0, y, z) => println!("Das erste ist `0`, `y` ist {:?} und `z` ist {:?}", y, z),
        (1,..)  => println!("Das erste ist `1` und der Rest ist unerheblich"),
        (.., 2)  => println!("Das letzte ist `2` und der Rest ist unerheblich"),
        (3,.., 4)  => println!("Das erste ist `3`, das letzte ist `4` und der Rest ist unerheblich"),
        // `..` kann verwendet werden, um den Rest des Tuples zu ignorieren
        _      => println!("Es spielt keine Rolle, was sie sind"),
        // `_` bedeutet, dass der Wert nicht an eine Variable gebunden wird
    }
}
```
