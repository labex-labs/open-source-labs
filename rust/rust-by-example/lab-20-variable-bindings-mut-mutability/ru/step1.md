# Мутабельность

По умолчанию переменные неизменяемы, но это можно изменить с помощью модификатора `mut`.

```rust
fn main() {
    let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // Error! Cannot assign a new value to an immutable variable
    _immutable_binding += 1;
}
```

Компилятор выдаст подробный диагностический отчет об ошибках связанных с мутабельностью.
