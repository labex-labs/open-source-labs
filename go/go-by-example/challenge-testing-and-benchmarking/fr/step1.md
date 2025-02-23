# Tests et tests de performance

Le problème à résoudre dans ce défi est de tester et de mesurer les performances d'une implémentation simple d'une fonction de minimum d'entier nommée `IntMin`.

## Exigences

- Le package `testing` doit être importé.
- La fonction `IntMin` doit prendre deux paramètres d'entier et renvoyer un entier.
- La fonction `TestIntMinBasic` doit tester la fonction `IntMin` pour des valeurs d'entrée de base.
- La fonction `TestIntMinTableDriven` doit tester la fonction `IntMin` en utilisant un style basé sur une table.
- La fonction `BenchmarkIntMin` doit mesurer les performances de la fonction `IntMin`.

## Exemple

```sh
# Exécutez tous les tests du projet actuel en mode verbeux.
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

# Exécutez tous les tests de performance du projet actuel. Tous les tests
# sont exécutés avant les tests de performance. Le drapeau `bench` filtre
# les noms de fonctions de test de performance avec une expression rationnelle.
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```
