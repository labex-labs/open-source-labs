# Использование методов трейта Iterator вместо индексирования

Далее, мы исправим тело функции `Config::build`. Поскольку `args` реализует трейт `Iterator`, мы знаем, что можем вызвать метод `next` для него! Листинг 13-20 обновляет код из листинга 12-23 для использования метода `next`.

Имя файла: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Листинг 13-20: Изменение тела функции `Config::build` для использования методов итератора

Помните, что первое значение в возвращаемом значении `env::args` — это имя программы. Мы хотим игнорировать это и перейти к следующему значению, поэтому сначала мы вызываем `next` и ничего не делаем с возвращаемым значением. Затем мы вызываем `next`, чтобы получить значение, которое мы хотим поместить в поле `query` структуры `Config`. Если `next` возвращает `Some`, мы используем `match` для извлечения значения. Если оно возвращает `None`, это означает, что передано недостаточно аргументов, и мы выходим ранним, возвращая значение `Err`. Мы делаем то же самое для значения `filename`.
