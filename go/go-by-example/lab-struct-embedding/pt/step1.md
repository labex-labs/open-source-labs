# _Struct Embedding_ (Incorporação de Estruturas)

Crie uma _struct_ chamada `container` que incorpora uma _struct_ chamada `base`. A _struct_ `base` deve ter um campo chamado `num` do tipo `int` e um método chamado `describe()` que retorna uma _string_. A _struct_ `container` deve ter um campo chamado `str` do tipo `string`. A _struct_ `container` deve ser capaz de acessar o campo `num` e o método `describe()` da _struct_ `base`.

- A _struct_ `base` deve ter um campo chamado `num` do tipo `int`.
- A _struct_ `base` deve ter um método chamado `describe()` que retorna uma _string_.
- A _struct_ `container` deve ter um campo chamado `str` do tipo `string`.
- A _struct_ `container` deve incorporar a _struct_ `base`.
- A _struct_ `container` deve ser capaz de acessar o campo `num` e o método `describe()` da _struct_ `base`.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

Abaixo está o código completo:

```go
// Go suporta a _incorporação_ de structs e interfaces
// para expressar uma _composição_ mais fluida de tipos.
// Isso não deve ser confundido com [`//go:embed`](embed-directive) que é
// uma diretiva go introduzida na versão 1.16+ do Go para incorporar
// arquivos e pastas no binário da aplicação.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// Um `container` _incorpora_ um `base`. Uma incorporação se parece
// com um campo sem nome.
type container struct {
	base
	str string
}

func main() {

	// Ao criar structs com literais, temos que
	// inicializar a incorporação explicitamente; aqui o
	// tipo incorporado serve como o nome do campo.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// Podemos acessar os campos de base diretamente em `co`,
	// por exemplo, `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Alternativamente, podemos soletrar o caminho completo usando
	// o nome do tipo incorporado.
	fmt.Println("also num:", co.base.num)

	// Como `container` incorpora `base`, os métodos de
	// `base` também se tornam métodos de um `container`. Aqui
	// invocamos um método que foi incorporado de `base`
	// diretamente em `co`.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// A incorporação de structs com métodos pode ser usada para conceder
	// implementações de interface a outras structs. Aqui
	// vemos que um `container` agora implementa a
	// interface `describer` porque incorpora `base`.
	var d describer = co
	fmt.Println("describer:", d.describe())
}
```
