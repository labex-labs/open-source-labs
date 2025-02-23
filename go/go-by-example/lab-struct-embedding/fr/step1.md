# Imbrication de structs

Créez un struct nommé `container` qui imbrique un struct nommé `base`. Le struct `base` devrait avoir un champ nommé `num` de type `int` et une méthode nommée `describe()` qui renvoie une chaîne de caractères. Le struct `container` devrait avoir un champ nommé `str` de type `string`. Le struct `container` devrait être capable d'accéder au champ `num` et à la méthode `describe()` du struct `base`.

- Le struct `base` devrait avoir un champ nommé `num` de type `int`.
- Le struct `base` devrait avoir une méthode nommée `describe()` qui renvoie une chaîne de caractères.
- Le struct `container` devrait avoir un champ nommé `str` de type `string`.
- Le struct `container` devrait imbriquer le struct `base`.
- Le struct `container` devrait être capable d'accéder au champ `num` et à la méthode `describe()` du struct `base`.

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

Voici le code complet ci-dessous :

```go
// Go prend en charge l'_imbrication_ de structs et d'interfaces
// pour exprimer une composition plus transparente de types.
// Ne confondez pas cela avec [`//go:embed`](embed-directive) qui est
// une directive go introduite dans la version 1.16+ de Go pour intégrer
// des fichiers et des dossiers dans le binaire de l'application.

package main

import "fmt"

type base struct {
	num int
}

func (b base) describe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

// Un `container` _imbrique_ un `base`. Une imbrication ressemble
// à un champ sans nom.
type container struct {
	base
	str string
}

func main() {

	// Lors de la création de structs avec des littéraux, nous devons
	// initialiser l'imbrication explicitement ; ici le
	// type imbriqué sert de nom de champ.
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	// Nous pouvons accéder directement aux champs de base sur `co`,
	// par exemple `co.num`.
	fmt.Printf("co={num: %v, str: %v}\n", co.num, co.str)

	// Alternativement, nous pouvons écrire le chemin complet en utilisant
	// le nom du type imbriqué.
	fmt.Println("also num:", co.base.num)

	// Puisque `container` imbrique `base`, les méthodes de
	// `base` deviennent également des méthodes d'un `container`. Ici
	// nous appelons une méthode qui a été imbriquée à partir de `base`
	// directement sur `co`.
	fmt.Println("describe:", co.describe())

	type describer interface {
		describe() string
	}

	// L'imbrication de structs avec des méthodes peut être utilisée pour conférer
	// des implémentations d'interfaces à d'autres structs. Ici
	// nous voyons qu'un `container` implémente désormais l'interface
	// `describer` car il imbrique `base`.
	var d describer = co
	fmt.Println("describer:", d.describe())
}

```
