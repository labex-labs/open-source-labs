# Тестирование

Как мы знаем, тестирование является неотъемлемой частью любого программного обеспечения! Rust имеет первоклассную поддержку для модульных и интеграционных тестов (см. [этот раздел](https://doc.rust-lang.org/book/ch11-00-testing.html) в TRPL).

Из разделов о тестировании, ссыланных выше, мы узнаем, как писать модульные и интеграционные тесты. Организационно мы можем размещать модульные тесты в модулях, которые они тестируют, а интеграционные тесты в собственной директории `tests/`:

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

Каждый файл в `tests` является отдельным [интеграционным тестом](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests), то есть тестом, предназначенным для тестирования вашей библиотеки, как будто она вызывается из зависимой коробки.

Раздел о Тестировании подробно описывает три различных стиля тестирования: модульные, документационные и интеграционные.

`cargo` естественно предоставляет простой способ запустить все ваши тесты!

```shell
$ cargo test
```

Вы должны увидеть вывод в таком виде:

```shell

```

Вы также можете запустить тесты, чье имя соответствует шаблону:

```shell
$ cargo test test_foo
```

```shell

```

Одна важная вещь: Cargo может запускать несколько тестов одновременно, поэтому убедитесь, что они не конфликтуют друг с другом.

Одним примером, когда параллелизм вызывает проблемы, является ситуация, когда два теста выводят данные в файл, как ниже:

```rust
#[cfg(test)]
mod tests {
    // Импортируем необходимые модули
    use std::fs::OpenOptions;
    use std::io::Write;

    // Этот тест записывает данные в файл
    #[test]
    fn test_file() {
        // Открывает файл ferris.txt или создает его, если он не существует.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // Печатает "Ferris" 5 раз.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }

    // Этот тест пытается записать данные в тот же файл
    #[test]
    fn test_file_also() {
        // Открывает файл ferris.txt или создает его, если он не существует.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // Печатает "Corro" 5 раз.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }
}
```

Хотя ожидаемый результат следующий:

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

В самом файле `ferris.txt` на самом деле находится следующее:

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
