# Введение

В этом лабораторном задании мы исследуем использование альтернативных/настраиваемых типов ключей в `HashMap` языка Rust, которые могут включать типы, реализующие трейты `Eq` и `Hash`, такие как `bool`, `int`, `uint`, `String` и `&str`. Кроме того, мы можем реализовать эти трейты для пользовательских типов, используя атрибут `#[derive(PartialEq, Eq, Hash)]`, что позволяет использовать их в качестве ключей в `HashMap`.

> **Примечание:** Если в лабораторном задании не указано имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью команды `rustc main.rs &&./main`.
