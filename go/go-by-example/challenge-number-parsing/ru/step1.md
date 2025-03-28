# Парсинг чисел

Парсинг чисел из строк - это распространенная задача в многих программах. В этом испытании требуется использовать встроенный пакет `strconv` для парсинга различных типов чисел из строк.

## Требования

- Использовать пакет `strconv` для парсинга чисел из строк.
- Парсить вещественное число с использованием `ParseFloat`.
- Парсить целое число с использованием `ParseInt`.
- Парсить шестнадцатерично форматированное число с использованием `ParseInt`.
- Парсить неотрицательное целое число с использованием `ParseUint`.
- Парсить десятичное целое число с использованием `Atoi`.
- Обрабатывать ошибки, возвращаемые функциями парсинга.

## Пример

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: парсинг "wat": синтаксис неверен

# Далее мы рассмотрим другую распространенную задачу парсинга: URL-адреса.
```
