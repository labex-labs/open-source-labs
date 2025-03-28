# Введение

В этом практическом занятии мы познакомимся с ключевым словом `while`, которое используется для создания цикла, который продолжает выполняться, пока заданное условие истинно. Чтобы проиллюстрировать его использование, мы напишем программу на Rust под названием FizzBuzz. Программа использует цикл `while` для перебора чисел от 1 до 100. Внутри цикла она проверяет, делится ли текущее число на 3 и 5 (то есть является кратным 15), и в таких случаях выводит "fizzbuzz". Если число делится только на 3, выводится "fizz", а если только на 5, выводится "buzz". Для всех остальных чисел просто выводится само число. Цикл продолжается, пока переменная-счетчик не достигнет 101, увеличивая ее после вывода каждого числа или метки.

> **Примечание:** Если практическое занятие не задает имя файла, вы можете использовать любое имя, которое хотите. Например, вы можете использовать `main.rs`, скомпилировать и запустить его с помощью `rustc main.rs &&./main`.
