# Введение

В этом лабе мы узнали о форматировании в Rust и о том, как использовать макрос `format!` для форматирования переменных. Мы увидели, что форматирование задается с использованием строки формата, и для форматирования одной и той же переменной могут использоваться разные типы аргументов по-разному. Самый распространенный трейт форматирования - `Display`, который обрабатывает случаи, когда тип аргумента не указан. Мы увидели пример реализации трейта `Display` для структуры `City`, где мы отформатировали значения широты и долготы. Мы также увидели пример структуры `Color` и получили задание реализовать для нее трейт `Display`, чтобы отобразить значения RGB и их шестнадцатеричное представление.

> **Примечание:** Если в лабе не указано имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
