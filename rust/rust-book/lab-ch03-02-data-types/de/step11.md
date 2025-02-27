# Zugriff auf Array-Elemente

Ein Array ist ein einzelner Arbeitsspeicherbereich von bekannter, fester Größe, der auf dem Stapel zugewiesen werden kann. Sie können auf die Elemente eines Arrays über die Indizierung zugreifen, wie folgt:

Dateiname: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

In diesem Beispiel erhält die Variable mit dem Namen `first` den Wert `1`, da das der Wert an der Stelle `[0]` im Array ist. Die Variable mit dem Namen `second` erhält den Wert `2` aus dem Index `[1]` im Array.
