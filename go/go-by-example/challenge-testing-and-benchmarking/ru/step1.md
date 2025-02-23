# Тестирование и бенчмаркирование

Задача, которую необходимо решить в этом испытании, - это протестировать и провести бенчмарк простой реализации функции нахождения минимального целого числа под названием `IntMin`.

## Требования

- Необходимо импортировать пакет `testing`.
- Функция `IntMin` должна принимать два целочисленных параметра и возвращать целое число.
- Функция `TestIntMinBasic` должна тестировать функцию `IntMin` для базовых значений входных данных.
- Функция `TestIntMinTableDriven` должна тестировать функцию `IntMin` в табличном стиле.
- Функция `BenchmarkIntMin` должна провести бенчмарк функции `IntMin`.

## Пример

```sh
# Запустить все тесты в текущем проекте в подробном режиме.
$ go test -v
== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
PASS
ok  	examples/testing-and-benchmarking	0.023s

# Запустить все бенчмарки в текущем проекте. Все тесты
# выполняются перед бенчмарками. Флаг `bench` фильтрует
# имена функций бенчмарков по регулярному выражению.
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
