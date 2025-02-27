# Заморозка

Когда данные связываются одним и тем же именем неизменяемым образом, они также _замораживаются_. _Замороженные_ данные нельзя изменить, пока неизменяемая привязка не выйдет из области видимости:

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // Shadowing by immutable `_mutable_integer`
        let _mutable_integer = _mutable_integer;

        // Ошибка! `_mutable_integer` заморожено в этой области видимости
        _mutable_integer = 50;
        // FIXME ^ Comment out this line

        // `_mutable_integer` выходит из области видимости
    }

    // Ок! `_mutable_integer` не заморожено в этой области видимости
    _mutable_integer = 3;
}
```
