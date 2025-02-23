# Fehler

Das Lab bietet zwei Funktionen an, die einen Fehler zurückgeben, wenn das Eingabeargument 42 ist. Die erste Funktion gibt einen grundlegenden Fehlerwert zurück, während die zweite Funktion einen benutzerdefinierten Typ verwendet, um den Fehler darzustellen.

- Das Paket `errors` muss importiert werden.
- Die Funktion `f1` muss einen Fehler zurückgeben, wenn das Eingabeargument 42 ist.
- Die Funktion `f2` muss einen Fehler vom Typ `argError` zurückgeben, wenn das Eingabeargument 42 ist.
- Der Typ `argError` muss zwei Felder haben: `arg` und `prob`.
- Der Typ `argError` muss die Methode `Error()` implementieren.
- Die `main`-Funktion muss sowohl `f1` als auch `f2` mit Eingabeargumenten von 7 und 42 aufrufen.
- Die `main`-Funktion muss das Ergebnis jedes Funktionsaufrufs zusammen mit jedem zurückgegebenen Fehler ausgeben.
- Die `main`-Funktion muss demonstrieren, wie man programmgesteuert die Daten in einem benutzerdefinierten Fehler verwendet.

```sh
$ go run errors.go
f1 worked: 10
f1 failed: kann nicht mit 42 arbeiten
f2 worked: 10
f2 failed: 42 - kann nicht damit arbeiten
42
kann nicht damit arbeiten

# Siehe diesen [tollen Beitrag](https://go.dev/blog/error-handling-and-go)
# auf dem Go-Blog für mehr Informationen zur Fehlerbehandlung.
```

Hier ist der vollständige Code:

```go
// In Go ist es üblich, Fehler über einen expliziten, separaten Rückgabewert zu kommunizieren. Dies kontrastiert mit den Ausnahmen, die in Sprachen wie Java und Ruby verwendet werden, und der überladenen einzelnen Ergebnis-/Fehlerwert, der manchmal in C verwendet wird. Go's Ansatz macht es einfach, zu sehen, welche Funktionen Fehler zurückgeben, und sie mit denselben Sprachkonstrukten zu behandeln, die für jede andere, nicht fehlerbehaftete Aufgabe verwendet werden.

package main

import (
	"errors"
	"fmt"
)

// Konventionell sind Fehler der letzte Rückgabewert und haben den Typ `error`, ein eingebautes Interface.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` konstruiert einen grundlegenden `error`-Wert
		// mit der angegebenen Fehlermeldung.
		return -1, errors.New("kann nicht mit 42 arbeiten")

	}

	// Ein `nil`-Wert an der Fehlerposition gibt an, dass kein Fehler aufgetreten ist.
	return arg + 3, nil
}

// Es ist möglich, benutzerdefinierte Typen als `error`s zu verwenden, indem man die Methode `Error()` auf ihnen implementiert. Hier ist eine Variante des obigen Beispiels, das einen benutzerdefinierten Typ verwendet, um einen Argumentfehler explizit darzustellen.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// In diesem Fall verwenden wir die Syntax `&argError`, um ein neues Struct zu erstellen und die Werte für die beiden Felder `arg` und `prob` bereitzustellen.
		return -1, &argError{arg, "kann nicht damit arbeiten"}
	}
	return arg + 3, nil
}

func main() {

	// Die beiden Schleifen unten testen jede unserer
	// fehlerzurückgebenden Funktionen. Beachten Sie, dass die Verwendung einer
	// inline-Fehlerprüfung in der `if`-Zeile ein übliches
	// Idiom in Go-Code ist.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e!= nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e!= nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// Wenn Sie die Daten in einem benutzerdefinierten Fehler programmgesteuert verwenden möchten, müssen Sie den Fehler als Instanz des benutzerdefinierten Fehlertyps über eine Typbehauptung erhalten.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}

```
