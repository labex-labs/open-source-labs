# Зависимости разработки

Иногда возникает необходимость иметь зависимости только для тестов (или примеров, или бенчмарков). Такие зависимости добавляются в `Cargo.toml` в разделе `[dev-dependencies]`. Эти зависимости не распространяются на другие пакеты, которые зависят от этого пакета.

Одним из таких примеров является [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html), который расширяет стандартные макросы `assert_eq!` и `assert_ne!`, чтобы предоставить цветной различия.\
Файл `Cargo.toml`:

```toml
# стандартные данные о пакете опущены
[dev-dependencies]
pretty_assertions = "1"
```

Файл `src/lib.rs`:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // пакет для использования только в тестах. Не может быть использован в не-тестовом коде.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```
