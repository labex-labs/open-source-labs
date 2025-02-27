# Freezing

Wenn Daten unveränderlich mit dem gleichen Namen gebunden werden, werden sie auch _gefroren_. _Gefrorene_ Daten können nicht geändert werden, bis die unveränderliche Bindung außer Geltungsbereich geht:

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // Shadowing durch unveränderliche `_mutable_integer`
        let _mutable_integer = _mutable_integer;

        // Fehler! `_mutable_integer` ist in diesem Bereich gefroren
        _mutable_integer = 50;
        // FIXME ^ Kommentieren Sie diese Zeile aus

        // `_mutable_integer` geht außer Geltungsbereich
    }

    // Ok! `_mutable_integer` ist in diesem Bereich nicht gefroren
    _mutable_integer = 3;
}
```
