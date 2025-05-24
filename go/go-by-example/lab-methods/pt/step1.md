# Métodos

O código fornecido define um tipo de struct chamado `rect` com dois campos, `width` e `height`. Dois métodos são definidos para este tipo de struct, `area` e `perim`. O método `area` calcula a área do retângulo, e o método `perim` calcula o perímetro do retângulo. A função `main` chama esses dois métodos e imprime seus resultados.

- O método `area` deve ter um tipo de receptor `*rect`.
- O método `perim` deve ter um tipo de receptor `rect`.
- O método `area` deve retornar a área do retângulo.
- O método `perim` deve retornar o perímetro do retângulo.
- A função `main` deve chamar ambos os métodos e imprimir seus resultados.

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Em seguida, veremos o mecanismo do Go para agrupar e
# nomear conjuntos relacionados de métodos: interfaces.
```

A seguir, o código completo:

```go
// Go suporta _métodos_ definidos em tipos de struct.

package main

import "fmt"

type rect struct {
	width, height int
}

// Este método `area` tem um _tipo de receptor_ de `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Métodos podem ser definidos para tipos de receptor de ponteiro ou valor.
// Aqui está um exemplo de um receptor de valor.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Aqui chamamos os 2 métodos definidos para nossa struct.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go lida automaticamente com a conversão entre valores
	// e ponteiros para chamadas de método. Você pode querer usar
	// um tipo de receptor de ponteiro para evitar a cópia nas chamadas de método
	// ou para permitir que o método mute a
	// struct receptora.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}
```
