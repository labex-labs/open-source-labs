# Tests et tests de performance

Le problème à résoudre dans ce laboratoire est de tester et de mesurer les performances d'une implémentation simple d'une fonction de minimum d'entiers nommée `IntMin`.

- Le package `testing` doit être importé.
- La fonction `IntMin` doit prendre deux paramètres entiers et renvoyer un entier.
- La fonction `TestIntMinBasic` doit tester la fonction `IntMin` pour des valeurs d'entrée de base.
- La fonction `TestIntMinTableDriven` doit tester la fonction `IntMin` en utilisant un style table-driven.
- La fonction `BenchmarkIntMin` doit mesurer les performances de la fonction `IntMin`.

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

Voici le code complet ci-dessous :

```go
// Les tests unitaires sont une partie importante de la rédaction
// de programmes Go conformes aux principes. Le package `testing`
// fournit les outils dont nous avons besoin pour écrire des tests unitaires
// et la commande `go test` exécute les tests.

// Pour la démonstration, ce code est dans le package
// `main`, mais il pourrait être n'importe quel package. Le code de test
// réside généralement dans le même package que le code qu'il teste.
package main

import (
	"fmt"
	"testing"
)

// Nous allons tester cette implémentation simple d'un
// minimum d'entiers. Normalement, le code que nous testons
// serait dans un fichier source nommé par exemple
// `intutils.go`, et le fichier de test pour lui serait ensuite
// nommé `intutils_test.go`.
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Un test est créé en écrivant une fonction dont le nom
// commence par `Test`.
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans!= -2 {
		// `t.Error*` signalera les échecs de test mais continuera
		// d'exécuter le test. `t.Fatal*` signalera les échecs de test
		// et arrêtera immédiatement le test.
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// L'écriture de tests peut être répétitive, il est donc courant
// d'utiliser un *style table-driven*, où les entrées de test et
// les sorties attendues sont listées dans un tableau et une seule boucle
// parcourt le tableau et exécute la logique de test.
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run permet d'exécuter des "sous-tests", un pour chaque
		// entrée de tableau. Ils sont affichés séparément
		// lors de l'exécution de `go test -v`.
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans!= tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// Les tests de performance vont généralement dans des fichiers `_test.go` et sont
// nommés en commençant par `Benchmark`. Le lanceur de test `testing`
// exécute chaque fonction de test de performance plusieurs fois, en augmentant
// `b.N` à chaque exécution jusqu'à ce qu'il ait collecté une mesure précise.
func BenchmarkIntMin(b *testing.B) {
	// Normalement, le test de performance exécute une fonction que nous
	// mesurons dans une boucle `b.N` fois.
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}

```
