# Введение

В этом лабе мы будем изучать небезопасные операции в Rust, которые используются для обхода защит компилятора и обычно используются для разыменовывания сырых указателей, вызова небезопасных функций, доступа к или модификации статических изменяемых переменных и реализации небезопасных трейтов. Эти операции должны быть минимизированы в кодовой базе для обеспечения безопасности.

> **Примечание:** Если лаб не уточняет имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
