# Введение

В этом лабе мы узнаем, как обойти ограничение прямого возврата трейтов в Rust, используя тип `Box<dyn Animal>`, который позволяет функциям возвращать ссылку на объект, выделенный в куче, реализующий трейт `Animal`.

> **Примечание:** Если в лабе не указано имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
