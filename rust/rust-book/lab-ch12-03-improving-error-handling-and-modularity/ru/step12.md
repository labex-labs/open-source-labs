# Handling Errors Returned from run in main

Мы проверим наличие ошибок и обработаем их с использованием техники, похожей на ту, которую мы использовали с `Config::build` в Listing 12-10, но с небольшой разницей:

Filename: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

Мы используем `if let` вместо `unwrap_or_else`, чтобы проверить, возвращает ли `run` значение `Err`, и вызвать `process::exit(1)`, если это так. Функция `run` не возвращает значение, которое мы бы хотели `unwrap` так, как `Config::build` возвращает экземпляр `Config`. Поскольку `run` возвращает `()`, когда все прошло успешно, нас интересует только обнаружение ошибки, поэтому нам не нужно использовать `unwrap_or_else`, чтобы вернуть развернутое значение, которое было бы только `()`.

Тела `if let` и функции `unwrap_or_else` в обоих случаях одинаковы: мы выводим ошибку и завершаем программу.
