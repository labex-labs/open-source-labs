# Splitting Code into a Library Crate

На данный момент наша программа `minigrep` выглядит неплохо! Теперь мы разделим файл `src/main.rs` и поместим часть кода в файл `src/lib.rs`. Таким образом, мы сможем протестировать код и уменьшить количество ответственностей в файле `src/main.rs`.

Переместим весь код, который не находится в функции `main` из `src/main.rs` в `src/lib.rs`:

- Определение функции `run`
- Соответствующие инструкции `use`
- Определение `Config`
- Определение функции `Config::build`

Содержимое `src/lib.rs` должно иметь сигнатуры, показанные в Listing 12-13 (мы опустили тела функций для краткости). Обратите внимание, что это не скомпилируется, пока мы не изменим `src/main.rs` в Listing 12-14.

Filename: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

Listing 12-13: Moving `Config` and `run` into `src/lib.rs`

Мы широко использовали ключевое слово `pub`: для `Config`, для его полей и метода `build`, а также для функции `run`. Теперь у нас есть библиотечный крейт с публичным API, которое мы можем протестировать!

Теперь нам нужно подключить код, который мы переместили в `src/lib.rs`, в область видимости бинарного крейта в `src/main.rs`, как показано в Listing 12-14.

Filename: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

Listing 12-14: Using the `minigrep` library crate in `src/main.rs`

Мы добавили строку `use minigrep::Config`, чтобы подключить тип `Config` из библиотечного крейта в область видимости бинарного крейта, и мы добавили префикс с именем нашего крейта к функции `run`. Теперь вся функциональность должна быть связана и работать должным образом. Запустите программу с помощью `cargo run` и убедитесь, что все работает правильно.

Фу! Это было много работы, но мы подготовили себя к успеху в будущем. Теперь обработка ошибок стала намного проще, и мы сделали код более модульным. Почти все наша работа будет выполняться в `src/lib.rs` с этого момента.

Давайте воспользуемся этой новой модульностью и выполним что-то, что было бы сложно сделать с старым кодом, но легко с новым: напишем некоторые тесты!
