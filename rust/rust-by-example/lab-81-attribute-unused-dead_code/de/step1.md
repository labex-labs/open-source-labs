# `dead_code`

Der Compiler bietet eine `dead_code`-Warnung (Lint), die über unbenutzte Funktionen warnt. Ein _Attribut_ kann verwendet werden, um diese Warnung zu deaktivieren.

```rust
fn used_function() {}

// `#[allow(dead_code)]` ist ein Attribut, das die `dead_code`-Warnung deaktiviert
#[allow(dead_code)]
fn unused_function() {}

fn noisy_unused_function() {}
// FIXME ^ Füge ein Attribut hinzu, um die Warnung zu unterdrücken

fn main() {
    used_function();
}
```

Beachten Sie, dass Sie in realen Programmen ungenutzten Code (dead code) beseitigen sollten. In diesen Beispielen erlauben wir an einigen Stellen ungenutzten Code aufgrund der interaktiven Natur der Beispiele.
