# Игнорирование некоторых тестов, если не требуется их запуск явно

Иногда некоторые конкретные тесты могут быть очень затратными по времени на выполнение, поэтому вы, возможно, захотите исключить их при большинстве запусков `cargo test`. Вместо того, чтобы перечислять в качестве аргументов все тесты, которые вы хотите запустить, вы можете вместо этого пометить затратные тесты с помощью атрибута `ignore`, чтобы исключить их, как показано ниже:

Имя файла: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // код, который занимает час на выполнение
}
```

После `#[test]` мы добавляем строку `#[ignore]` к тесту, который мы хотим исключить. Теперь, когда мы запускаем наши тесты, `it_works` запускается, а `expensive_test` нет:

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.60s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 2 tests
test expensive_test... ignored
test it_works... ok

test result: ok. 1 passed; 0 failed; 1 ignored; 0 measured; 0
filtered out; finished in 0.00s
```

Функция `expensive_test` перечислена как `ignored`. Если мы хотим запустить только игнорируемые тесты, мы можем использовать `cargo test -- --ignored`:

```bash
$ cargo test -- --ignored
    Finished test [unoptimized + debuginfo] target(s) in 0.61s
     Running unittests src/lib.rs (target/debug/deps/adder-
92948b65e88960b4)

running 1 test
test expensive_test... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1
filtered out; finished in 0.00s
```

Управляя тем, какие тесты запускаются, вы можете убедиться, что результаты `cargo test` будут возвращены быстро. Когда вы достигнете такой точки, где имеет смысл проверить результаты `ignored` тестов и у вас есть время ожидать результатов, вы можете вместо этого запустить `cargo test -- --ignored`. Если вы хотите запустить все тесты, независимо от того, игнорируются они или нет, вы можете запустить `cargo test -- --include-ignored`.
