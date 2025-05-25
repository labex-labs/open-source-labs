# Congelamento

Quando os dados são ligados pelo mesmo nome de forma imutável, eles também são _congelados_. Dados _congelados_ não podem ser modificados até que a ligação imutável saia de âmbito:

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // Sombra por `_mutable_integer` imutável
        let _mutable_integer = _mutable_integer;

        // Erro! `_mutable_integer` está congelado neste âmbito
        _mutable_integer = 50;
        // FIXME ^ Comente esta linha

        // `_mutable_integer` sai de âmbito
    }

    // Ok! `_mutable_integer` não está congelado neste âmbito
    _mutable_integer = 3;
}
```
