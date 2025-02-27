# Несколько типов ошибок

Предыдущие примеры всегда были очень удобными; `Result` взаимодействуют с другими `Result`, а `Option` взаимодействуют с другими `Option`.

Иногда `Option` должен взаимодействовать с `Result`, или `Result<T, Error1>` должен взаимодействовать с `Result<T, Error2>`. В таких случаях мы хотим управлять нашими различными типами ошибок таким образом, чтобы они были комбинируемыми и легкими для взаимодействия.

В следующем коде два вызова `unwrap` генерируют разные типы ошибок. `Vec::first` возвращает `Option`, а `parse::<i32>` возвращает `Result<i32, ParseIntError>`:

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Генерирует ошибку 1
    2 * first.parse::<i32>().unwrap() // Генерирует ошибку 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(numbers));

    println!("The first doubled is {}", double_first(empty));
    // Ошибка 1: входящий вектор пуст

    println!("The first doubled is {}", double_first(strings));
    // Ошибка 2: элемент не может быть преобразован в число
}
```

В следующих разделах мы рассмотрим несколько стратегий для решения таких проблем.
