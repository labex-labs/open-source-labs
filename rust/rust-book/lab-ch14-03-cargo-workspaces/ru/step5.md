# Добавление теста в рабочее пространство

Для следующего улучшения давайте добавим тест функции `add_one::add_one` внутри ящика `add_one`:

Имя файла: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Теперь запустите `cargo test` в верхнеуровневой директории `add`. Запуск `cargo test` в рабочем пространстве, структурированном так, как это одно, запустит тесты для всех ящиков в рабочем пространстве:

```bash
$ cargo test
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.27s
     Running unittests src/lib.rs (target/debug/deps/add_one-f0253159197f7841)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

     Running unittests src/main.rs (target/debug/deps/adder-49979ff40686fa8e)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

Первая часть вывода показывает, что тест `it_works` в ящике `add_one` прошел. Следующая часть показывает, что в ящике `adder` не было найдено ни одного теста, а затем последняя часть показывает, что в ящике `add_one` не было найдено ни одного документационного теста.

Мы также можем запускать тесты для одного конкретного ящика в рабочем пространстве из верхнеуровневой директории, используя флаг `-p` и указывая имя ящика, который мы хотим протестировать:

```bash
$ cargo test -p add_one
    Finished test [unoptimized + debuginfo] target(s) in 0.00s
     Running unittests src/lib.rs (target/debug/deps/add_one-b3235fea9a156f74)

running 1 test
test tests::it_works... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

   Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s
```

Этот вывод показывает, что `cargo test` запустил только тесты для ящика `add_one` и не запустил тесты для ящика `adder`.

Если вы публикуете ящики в рабочем пространстве на *https://crates.io*, каждый ящик в рабочем пространстве должен быть опубликован отдельно. Как и `cargo test`, мы можем опубликовать конкретный ящик в нашем рабочем пространстве, используя флаг `-p` и указывая имя ящика, который мы хотим опубликовать.

Для дополнительной практики добавьте ящик `add_two` в это рабочее пространство аналогичным образом, как и ящик `add_one`!

По мере роста вашего проекта рассмотрите использование рабочего пространства: оно предоставляет более понятные, более мелкие отдельные компоненты, чем один большой кусок кода. Кроме того, хранение ящиков в рабочем пространстве может облегчить координацию между ящиками, если они часто изменяются одновременно.
