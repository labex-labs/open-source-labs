# waitgroups

Проблема, которую необходимо решить в этом испытании, заключается в том, чтобы запустить несколько горутин и увеличить счетчик WaitGroup для каждой из них. Затем нам нужно дождаться завершения всех запущенных горутин.

## Требования

- Основные знания Golang.
- Понимание параллелизма в Golang.
- Знание пакета `sync`.

## Пример

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# Порядок запуска и завершения воркеров
# может быть разным для каждой ин vocation.
```
