# Extracting the Argument Parser

Мы извлечем функциональность для разбора аргументов в функцию, которую вызовет `main`, чтобы подготовиться к перемещению логики разбора аргументов командной строки в `src/lib.rs`. Listing 12-5 показывает новый старт `main`, который вызывает новую функцию `parse_config`, которую мы определим в `src/main.rs` на данный момент.

Filename: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

Listing 12-5: Extracting a `parse_config` function from `main`

Мы по-прежнему собираем аргументы командной строки в вектор, но вместо того, чтобы назначить значение аргумента с индексом 1 переменной `query` и значение аргумента с индексом 2 переменной `file_path` внутри функции `main`, мы передаем целый вектор в функцию `parse_config`. Функция `parse_config` затем содержит логику, которая определяет, какой аргумент должен быть присвоен какой переменной, и передает значения обратно в `main`. Мы по-прежнему создаем переменные `query` и `file_path` в `main`, но `main` больше не имеет ответственности за определение соответствия между аргументами командной строки и переменными.

Эта переработка может показаться излишней для нашей маленькой программы, но мы рефакторим по маленьким, инкрементальным шагам. После внесения этих изменений запустите программу снова, чтобы проверить, работает ли разбор аргументов по-прежнему. Хорошо проверять свой прогресс часто, чтобы помочь определить причину проблем, когда они возникают.
