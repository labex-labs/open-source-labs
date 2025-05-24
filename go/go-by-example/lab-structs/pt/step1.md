# Structs (Estruturas)

Neste laboratório, você precisa completar a função `newPerson` que constrói uma nova struct (estrutura) `person` com o nome fornecido. O tipo de struct `person` possui os campos `name` (nome) e `age` (idade).

- O tipo de struct `person` deve ter os campos `name` e `age`.
- A função `newPerson` deve construir uma nova struct `person` com o nome fornecido.
- A função `newPerson` deve retornar um ponteiro para a struct `person` recém-criada.
- A função `main` deve imprimir o seguinte:
  - Uma nova struct com o nome "Bob" e idade 20.
  - Uma nova struct com o nome "Alice" e idade 30.
  - Uma nova struct com o nome "Fred" e idade 0.
  - Um ponteiro para uma nova struct com o nome "Ann" e idade 40.
  - Uma nova struct construída usando a função `newPerson` com o nome "Jon" e idade 42.
  - O campo nome de uma struct com o nome "Sean" e idade 50.
  - O campo idade de um ponteiro para uma struct com o nome "Sean" e idade 50.
  - O campo idade de um ponteiro para uma struct com o nome "Sean" e idade 50 após o campo idade ter sido atualizado para 51.

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

A seguir, o código completo:

```go
// As _structs_ (estruturas) do Go são coleções tipadas de campos.
// Elas são úteis para agrupar dados e formar
// registros.

package main

import "fmt"

// Este tipo de struct `person` possui os campos `name` e `age`.
type person struct {
	name string
	age  int
}

// `newPerson` constrói uma nova struct person com o nome fornecido.
func newPerson(name string) *person {
	// Você pode retornar com segurança um ponteiro para uma variável local
	// pois uma variável local sobreviverá ao escopo da função.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// Esta sintaxe cria uma nova struct.
	fmt.Println(person{"Bob", 20})

	// Você pode nomear os campos ao inicializar uma struct.
	fmt.Println(person{name: "Alice", age: 30})

	// Campos omitidos terão o valor zero.
	fmt.Println(person{name: "Fred"})

	// Um prefixo `&` produz um ponteiro para a struct.
	fmt.Println(&person{name: "Ann", age: 40})

	// É idiomático encapsular a criação de novas structs em funções construtoras
	fmt.Println(newPerson("Jon"))

	// Acesse os campos da struct com um ponto.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// Você também pode usar pontos com ponteiros de struct - os
	// ponteiros são automaticamente desreferenciados.
	sp := &s
	fmt.Println(sp.age)

	// Structs são mutáveis.
	sp.age = 51
	fmt.Println(sp.age)
}
```
