# Congélation

Lorsque des données sont liées par le même nom de manière immuable, elles sont également _congelées_. Les données _congelées_ ne peuvent pas être modifiées tant que la liaison immuable est dans la portée :

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // Ombre par `_mutable_integer` immuable
        let _mutable_integer = _mutable_integer;

        // Erreur! `_mutable_integer` est congelé dans cette portée
        _mutable_integer = 50;
        // FIXME ^ Commenter cette ligne

        // `_mutable_integer` sort de portée
    }

    // Ok! `_mutable_integer` n'est pas congelé dans cette portée
    _mutable_integer = 3;
}
```
