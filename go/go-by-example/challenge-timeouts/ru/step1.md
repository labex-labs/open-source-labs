# Таймауты

Когда программы подключаются к внешним ресурсам или нуждаются в ограничении времени выполнения, таймауты играют важную роль. Задача - реализовать таймауты в Go с использованием каналов и `select`.

## Требования

- Реализовать таймауты в Go с использованием каналов и `select`.
- Использовать буферизованный канал для предотвращения утечки горутин в случае, если канал никогда не читается.
- Использовать `time.After` для ожидания отправки значения после истечения таймаута.
- Использовать `select` для продолжения с первым получением, которое готово.

## Пример

```sh
# Запуск этой программы показывает, что первая операция
# завершается по таймауту, а вторая - успешно.
$ go run timeouts.go
timeout 1
result 2
```
