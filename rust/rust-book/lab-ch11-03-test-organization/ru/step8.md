# Интеграционные тесты для бинарных крейтов

Если наша программа представляет собой бинарный крейт, который содержит только файл `src/main.rs` и не имеет файла `src/lib.rs`, мы не можем создавать интеграционные тесты в директории `tests` и подтянуть в область видимости с помощью инструкции `use` функции, определенные в файле `src/main.rs`. Только библиотечные крейты экспортируют функции, которые могут использоваться другими крейтами; бинарные крейты предназначены для самостоятельного запуска.

Это одна из причин, по которой Rust-проекты, которые предоставляют бинарный файл, имеют простой файл `src/main.rs`, который вызывает логику, хранящуюся в файле `src/lib.rs`. Используя такую структуру, интеграционные тесты могут проверить библиотечный крейт с использованием `use`, чтобы сделать доступной важную функциональность. Если важная функциональность работает, небольшой объем кода в файле `src/main.rs` также будет работать, и этот небольшой объем кода не требует тестирования.
