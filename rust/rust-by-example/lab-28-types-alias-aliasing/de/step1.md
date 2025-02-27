# Aliasing

Die `type`-Anweisung kann verwendet werden, um einem bestehenden Typ einen neuen Namen zu geben. Typen müssen `UpperCamelCase`-Namen haben, andernfalls wird der Compiler eine Warnung ausgeben. Ausnahme von dieser Regel sind die primitive Typen: `usize`, `f32`, etc.

```rust
// `NanoSecond`, `Inch` und `U64` sind neue Namen für `u64`.
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`.
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // Beachten Sie, dass Typaliase *keine* zusätzliche Typsicherheit bieten, weil
    // Aliase *keine* neuen Typen sind
    println!("{} Nanosekunden + {} Zoll = {} Einheit?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

Der Hauptzweck von Aliasen ist es, Boilerplate zu reduzieren; beispielsweise ist der `io::Result<T>`-Typ ein Alias für den `Result<T, io::Error>`-Typ.
