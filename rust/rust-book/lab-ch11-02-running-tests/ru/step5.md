# Запуск отдельных тестов

Мы можем передать имя любой тестовой функции в `cargo test`, чтобы запустить только этот тест:

```bash
$ cargo test one_hundred
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.69s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test tests::one_hundred... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2
filtered out; finished in 0.00s
```

Запустился только тест с именем `one_hundred`; другие два теста не соответствовали этому имени. Вывод теста сообщает нам, что у нас были дополнительные тесты, которые не запустились, показывая `2 filtered out` в конце.

Мы не можем указать имена нескольких тестов таким образом; будет использовано только первое значение, переданное в `cargo test`. Но есть способ запустить несколько тестов.
