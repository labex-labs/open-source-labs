# Фильтрация для запуска нескольких тестов

Мы можем указать часть имени теста, и все тесты, чье имя соответствует этому значению, будут запущены. Например, поскольку в именах двух наших тестов содержится `add`, мы можем запустить эти два теста, выполнив `cargo test add`:

```bash
$ cargo test add
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test tests::add_three_and_two... ok
test tests::add_two_and_two... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Эта команда запустила все тесты, в именах которых содержится `add`, и проигнорировала тест с именем `one_hundred`. Также обратите внимание, что модуль, в котором появляется тест, становится частью имени теста, поэтому мы можем запустить все тесты в модуле, выполнив фильтрацию по имени модуля.
