# Erros

O laboratório fornece duas funções que retornam um erro se o argumento de entrada for 42. A primeira função retorna um valor de erro básico, enquanto a segunda função usa um tipo personalizado para representar o erro.

- O pacote `errors` deve ser importado.
- A função `f1` deve retornar um erro se o argumento de entrada for 42.
- A função `f2` deve retornar um erro do tipo `argError` se o argumento de entrada for 42.
- O tipo `argError` deve ter dois campos: `arg` e `prob`.
- O tipo `argError` deve implementar o método `Error()`.
- A função `main` deve chamar `f1` e `f2` com argumentos de entrada 7 e 42.
- A função `main` deve imprimir o resultado de cada chamada de função, juntamente com qualquer erro que foi retornado.
- A função `main` deve demonstrar como usar programaticamente os dados em um erro personalizado.

```sh
# Veja esta [ótima publicação](https://go.dev/blog/error-handling-and-go)
# no blog do Go para mais informações sobre tratamento de erros.
```

Abaixo está o código completo:

```go
// Em Go, é idiomático comunicar erros por meio de um
// valor de retorno explícito e separado. Isso contrasta com
// as exceções usadas em linguagens como Java e Ruby e
// o único resultado sobrecarregado / valor de erro às vezes
// usado em C. A abordagem do Go facilita a visualização de quais
// funções retornam erros e tratá-los usando o
// mesmas construções de linguagem empregadas para qualquer outra,
// tarefas não relacionadas a erros.

package main

import (
	"errors"
	"fmt"
)

// Por convenção, os erros são o último valor de retorno e
// têm o tipo `error`, uma interface embutida.
func f1(arg int) (int, error) {
	if arg == 42 {

		// `errors.New` constrói um valor `error` básico
		// com a mensagem de erro fornecida.
		return -1, errors.New("can't work with 42")

	}

	// Um valor `nil` na posição de erro indica que
	// não houve erro.
	return arg + 3, nil
}

// É possível usar tipos personalizados como `error`s por
// implementar o método `Error()` neles. Aqui está uma
// variante do exemplo acima que usa um tipo personalizado
// para representar explicitamente um erro de argumento.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {

		// Neste caso, usamos a sintaxe `&argError` para construir
		// uma nova struct, fornecendo valores para os dois
		// campos `arg` e `prob`.
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {

	// Os dois loops abaixo testam cada uma de nossas
	// funções que retornam erros. Observe que o uso de um
	// verificação de erro embutida na linha `if` é um comum
	// idioma no código Go.
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}
	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// Se você deseja usar programaticamente os dados em
	// um erro personalizado, você precisará obter o erro como um
	// instância do tipo de erro personalizado via tipo
	// asserção.
	_, e := f2(42)
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
```
