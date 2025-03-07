# Модуль tests и #[cfg(test)]

Аннотация #[cfg(test)] для модуля tests сообщает Rust компилировать и запускать тестовый код только при вызове cargo test, а не при вызове cargo build. Это экономит время компиляции, когда вы только хотите собрать библиотеку, и занимает меньше места в результирующем скомпилированном артефакте, так как тесты не включаются. Вы увидите, что поскольку интеграционные тесты располагаются в другой директории, они не нуждаются в аннотации #[cfg(test)]. Однако, поскольку юнит-тесты находятся в том же файле, что и код, вы будете использовать #[cfg(test)] для указания того, что они не должны быть включены в скомпилированный результат.

Помните, что когда мы создавали новый проект adder в первом разделе этой главы, Cargo сгенерировал для нас этот код:

Имя файла: src/lib.rs

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Этот код представляет собой автоматически сгенерированный модуль tests. Атрибут cfg расшифровывается как _конфигурация_ и сообщает Rust, что следующий элемент должен быть включен только при определенных настройках конфигурации. В данном случае настройкой конфигурации является test, которую Rust предоставляет для компиляции и запуска тестов. Используя атрибут cfg, Cargo компилирует наш тестовый код только в том случае, если мы явно запускаем тесты с помощью cargo test. Это включает в себя любые вспомогательные функции, которые могут быть в этом модуле, помимо функций, помеченных #[test].
