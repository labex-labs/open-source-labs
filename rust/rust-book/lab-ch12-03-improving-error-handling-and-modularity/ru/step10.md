# Extracting Logic from main

Теперь, когда мы закончили рефакторинг разбора конфигурации, давайте перейдем к логике программы. Как мы сказали в разделе "Separation of Concerns for Binary Projects", мы извлечем функцию под названием `run`, которая будет содержать всю текущую логику из функции `main`, которая не связана с настройкой конфигурации или обработкой ошибок. Когда мы закончим, `main` будет краткой и легко проверить наглядно, и мы сможем написать тесты для всей остальной логики.

Listing 12-11 показывает извлеченную функцию `run`. В данный момент мы делаем только небольшое, нарастающее улучшение - извлечение функции. Мы по-прежнему определяем функцию в `src/main.rs`.

Filename: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

Listing 12-11: Extracting a `run` function containing the rest of the program logic

Теперь функция `run` содержит всю оставшуюся логику из `main`, начиная от чтения файла. Функция `run` принимает экземпляр `Config` в качестве аргумента.
