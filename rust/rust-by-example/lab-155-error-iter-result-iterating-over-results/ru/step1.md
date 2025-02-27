# Итерация по `Result`

Операция `Iter::map` может завершиться с ошибкой, например:

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Рассмотрим стратегии для обработки этого.

## Игнорирование неудачных элементов с помощью `filter_map()`

`filter_map` вызывает функцию и фильтрует результаты, которые равны `None`.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Results: {:?}", numbers);
}
```

## Сбор неудачных элементов с помощью `map_err()` и `filter_map()`

`map_err` вызывает функцию с ошибкой, поэтому, добавив это к предыдущему решению с использованием `filter_map`, мы можем сохранить ошибки в отдельный вектор при итерации.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## Завершение всей операции с ошибкой с помощью `collect()`

`Result` реализует `FromIterator`, чтобы вектор результатов (`Vec<Result<T, E>>`) мог быть преобразован в результат с вектором (`Result<Vec<T>, E>`). Как только найдена ошибка `Result::Err`, итерация завершается.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Та же техника может быть использована с `Option`.

## Сбор всех валидных значений и ошибок с помощью `partition()`

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

При просмотре результатов вы заметите, что все еще обернуто в `Result`. Для этого требуется немного больше样板 кода.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```
