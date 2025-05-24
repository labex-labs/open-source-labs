# Mapas (Maps)

Neste laboratório, você precisará criar um mapa (map) que armazena o número de vezes que cada palavra aparece em uma determinada string. Você precisará dividir a string em palavras e, em seguida, iterar sobre cada palavra, adicionando-a ao mapa se ela ainda não existir, ou incrementando sua contagem se ela já existir.

- Você deve usar um mapa para armazenar as contagens de palavras.
- Você deve dividir a string de entrada em palavras.
- Você deve iterar sobre cada palavra na string de entrada.
- Você deve adicionar cada palavra ao mapa se ela ainda não existir, ou incrementar sua contagem se ela já existir.

```sh
# Note that maps appear in the form `map[k:v k:v]` when
# printed with `fmt.Println`.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

Aqui está o código completo:

```go
// _Maps_ são o [tipo de dado associativo](https://en.wikipedia.org/wiki/Associative_array) embutido do Go
// (às vezes chamado de _hashes_ ou _dicts_ em outras linguagens).

package main

import "fmt"

func main() {

	// Para criar um mapa vazio, use o `make` embutido:
	// `make(map[key-type]val-type)`.
	m := make(map[string]int)

	// Defina pares chave/valor usando a sintaxe típica `name[key] = val`
	m["k1"] = 7
	m["k2"] = 13

	// Imprimir um mapa com, por exemplo, `fmt.Println` mostrará todos os
	// seus pares chave/valor.
	fmt.Println("map:", m)

	// Obtenha um valor para uma chave com `name[key]`.
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// Se a chave não existir, o
	// [valor zero](https://go.dev/ref/spec#The_zero_value) do
	// tipo de valor é retornado.
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// O `len` embutido retorna o número de pares chave/valor
	// quando chamado em um mapa.
	fmt.Println("len:", len(m))

	// O `delete` embutido remove pares chave/valor de
	// um mapa.
	delete(m, "k2")
	fmt.Println("map:", m)

	// O segundo valor de retorno opcional ao obter um
	// valor de um mapa indica se a chave estava presente
	// no mapa. Isso pode ser usado para desambiguar
	// entre chaves ausentes e chaves com valores zero
	// como `0` ou `""`. Aqui não precisávamos do valor
	// em si, então o ignoramos com o _identificador em branco_
	// `_`.
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// Você também pode declarar e inicializar um novo mapa na
	// mesma linha com esta sintaxe.
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}
```
