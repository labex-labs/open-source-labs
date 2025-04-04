# Введение

В этом лабе мы узнаем, как использовать match guards в Rust для фильтрации ветвей на основе условий. Match guard добавляется после шаблона и представляется ключевым словом `if`, за которым следует условие. Условие guard позволяет нам дополнительно уточнить сопоставление шаблонов и выполнить дополнительные проверки перед выполнением соответствующей ветви match-выражения. Однако важно помнить, что компилятор не учитывает условия guard при проверке покрытия шаблонов, поэтому необходимо убедиться, что все шаблоны по-прежнему покрываются match-выражением.

> **Примечание:** Если в лабе не указано имя файла, вы можете использовать любое имя файла, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
