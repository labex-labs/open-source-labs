# Panic

O laboratório exige que você use a função `panic` para falhar rapidamente em erros que não deveriam ocorrer durante a operação normal ou que você não está preparado para lidar de forma elegante.

- Conhecimento básico da linguagem de programação Golang.
- Familiaridade com o tratamento de erros em Golang.
- Compreensão da função `panic` em Golang.

```sh
# Executar este programa fará com que ele entre em pânico, imprima
# uma mensagem de erro e rastreamentos de goroutines, e saia com
# um status diferente de zero.

# Quando o primeiro panic em `main` dispara, o programa sai
# sem atingir o restante do código. Se você quiser
# ver o programa tentar criar um arquivo temporário, comente
# o primeiro panic.
$ go run panic.go
panic: a problem

goroutine 1 [running]:
main.main() /.../panic.go:12 +0x47
...
exit status 2

# Observe que, ao contrário de algumas linguagens que usam exceções
# para lidar com muitos erros, em Go é idiomático
# usar valores de retorno indicando erros sempre que possível.
```

Aqui está o código completo:

```go
// Um `panic` normalmente significa que algo deu errado inesperadamente.
// Principalmente, nós o usamos para falhar rapidamente em erros que
// não deveriam ocorrer durante a operação normal, ou que nós
// não estamos preparados para lidar de forma elegante.

package main

import "os"

func main() {

	// Usaremos panic em todo este site para verificar
	// erros inesperados. Este é o único programa no
	// site projetado para entrar em pânico.
	panic("a problem")

	// Um uso comum de panic é abortar se uma função
	// retorna um valor de erro que não sabemos como
	// (ou queremos) lidar. Aqui está um exemplo de
	// `panic`ando se obtivermos um erro inesperado ao criar um novo arquivo.
	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
```
