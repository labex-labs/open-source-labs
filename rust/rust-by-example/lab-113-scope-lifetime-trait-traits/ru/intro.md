# Введение

В этом лабораторном задании мы исследуем аннотацию сроков жизни в методах трейтов, которая аналогична функциям. Также она включает в себя аннотацию сроков жизни в блоке `impl`. Приведенный код демонстрирует пример, в котором структура `Borrowed` имеет аннотацию срока жизни, и для нее реализуется трейт `Default` с использованием аннотированного срока жизни. Затем в главной функции создается экземпляр `Borrowed` с использованием метода `Default::default()`, демонстрируя использование сроков жизни в методах трейтов.

> **Примечание:** Если лабораторное задание не задает имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
