# waitgroups

Le problème à résoudre dans ce défi est de lancer plusieurs goroutines et d'incrémenter le compteur du WaitGroup pour chacune d'entre elles. Ensuite, nous devons attendre que toutes les goroutines lancées se terminent.

## Exigences

- Connaissance de base de Golang.
- Compréhension de la concurrence en Golang.
- Familiarité avec le package `sync`.

## Exemple

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

# L'ordre dans lequel les workers démarrent et se terminent
# est susceptible d'être différent pour chaque invocation.
```
