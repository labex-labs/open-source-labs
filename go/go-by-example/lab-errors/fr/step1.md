# Erreurs

Le laboratoire fournit deux fonctions qui renvoient une erreur si l'argument d'entrée est égal à 42. La première fonction renvoie une valeur d'erreur de base, tandis que la seconde fonction utilise un type personnalisé pour représenter l'erreur.

- Le package `errors` doit être importé.
- La fonction `f1` doit renvoyer une erreur si l'argument d'entrée est égal à 42.
- La fonction `f2` doit renvoyer une erreur de type `argError` si l'argument d'entrée est égal à 42.
- Le type `argError` doit avoir deux champs : `arg` et `prob`.
- Le type `argError` doit implémenter la méthode `Error()`.
- La fonction `main` doit appeler les deux fonctions `f1` et `f2` avec des arguments d'entrée de 7 et 42.
- La fonction `main` doit afficher le résultat de chaque appel de fonction, ainsi que toute erreur qui a été renvoyée.
- La fonction `main` doit démontrer comment utiliser programmatiquement les données dans une erreur personnalisée.

```sh
$ go run errors.go
f1 a fonctionné : 10
f1 a échoué : impossible de travailler avec 42
f2 a fonctionné : 10
f2 a échoué : 42 - impossible de travailler avec
42
impossible de travailler avec

# Consultez ce [super article](https://go.dev/blog/error-handling-and-go)
# sur le blog Go pour en savoir plus sur la gestion des erreurs.
```

Voici le code complet ci-dessous :

```go
// En Go, il est courant de communiquer les erreurs via une
// valeur de retour explicite et séparée. Cela contraste avec
// les exceptions utilisées dans des langages comme Java et Ruby et
// la valeur de résultat / erreur surchargée parfois utilisée
// en C. L'approche de Go facilite la visualisation des
// fonctions qui renvoient des erreurs et leur gestion en utilisant
// les mêmes constructions de langage employées pour toute autre
// tâche non d'erreur.

package main

import (
	"errors"
	"fmt"
)

// Par convention, les erreurs sont la dernière valeur de retour et
// ont le type `error`, une interface intégrée.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` construit une valeur de base `error`
		// avec le message d'erreur donné.
		return -1, errors.New("impossible de travailler avec 42")

	}

	// Une valeur `nil` dans la position d'erreur indique qu'il
	// n'y a eu aucune erreur.
	return arg + 3, nil
}

// Il est possible d'utiliser des types personnalisés comme `error` en
// implémentant la méthode `Error()` sur eux. Voici une
// variante de l'exemple ci-dessus qui utilise un type personnalisé
// pour représenter explicitement une erreur d'argument.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// Dans ce cas, nous utilisons la syntaxe `&argError` pour construire
		// un nouveau struct, en fournissant des valeurs pour les deux
		// champs `arg` et `prob`.
		return -1, &argError{arg, "impossible de travailler avec"}
	}
	return arg + 3, nil
}

func main() {

	// Les deux boucles ci-dessous testent chacune de nos
	// fonctions renvoyant des erreurs. Notez que l'utilisation d'un
	// contrôle d'erreur en ligne sur la ligne `if` est une forme
	// courante dans le code Go.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e!= nil {
			fmt.Println("f1 a échoué :", e)
		} else {
			fmt.Println("f1 a fonctionné :", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e!= nil {
			fmt.Println("f2 a échoué :", e)
		} else {
			fmt.Println("f2 a fonctionné :", r)
		}
	}

	// Si vous voulez utiliser programmatiquement les données dans
	// une erreur personnalisée, vous devrez obtenir l'erreur en tant
	// qu'instance du type d'erreur personnalisé via une assertion de type.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}

```
