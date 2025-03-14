# Самая длинная подстрока с k различными символами

## Задача

Дана строка и целое число k. Найдите длину самой длинной подстроки, которая содержит не более k различных символов. Подстрока - это непрерывный блок символов. Например, в строке "abcabcdefgghiij" самая длинная подстрока с не более 3 различных символов - это "abcabc". Если есть несколько подстрок с одинаковой длиной, верните любую из них.

## Требования

Для решения этого испытания необходимо выполнить следующие требования:

- Входные данные могут быть недействительными, поэтому код должен优雅но обрабатывать недействительные входы.
- Строки состоят из ASCII-символов.
- Поиск чувствителен к регистру.
- Подстрока - это непрерывный блок символов.
- Результат должен быть целым числом.
- Код должен быть способен обрабатывать входные данные в рамках ограничений памяти.

## Примеры использования

Следующие примеры демонстрируют ожидаемое поведение кода:

- None -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
