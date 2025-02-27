# Congelación

Cuando los datos se enlazan por el mismo nombre de manera inmutable, también se _congelan_. Los datos _congelados_ no pueden ser modificados hasta que el enlace inmutable sale del ámbito:

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // Sombreado por `_mutable_integer` inmutable
        let _mutable_integer = _mutable_integer;

        // Error! `_mutable_integer` está congelado en este ámbito
        _mutable_integer = 50;
        // FIXME ^ Comenta esta línea

        // `_mutable_integer` sale del ámbito
    }

    // Ok! `_mutable_integer` no está congelado en este ámbito
    _mutable_integer = 3;
}
```
