# Structs

Dans ce laboratoire, vous devez compléter la fonction `newPerson` qui construit un nouveau struct `person` avec le nom donné. Le type de struct `person` a les champs `name` et `age`.

- Le type de struct `person` doit avoir les champs `name` et `age`.
- La fonction `newPerson` doit construire un nouveau struct `person` avec le nom donné.
- La fonction `newPerson` doit retourner un pointeur vers le nouveau struct `person` créé.
- La fonction `main` doit afficher les informations suivantes :
  - Un nouveau struct avec le nom "Bob" et l'âge 20.
  - Un nouveau struct avec le nom "Alice" et l'âge 30.
  - Un nouveau struct avec le nom "Fred" et l'âge 0.
  - Un pointeur vers un nouveau struct avec le nom "Ann" et l'âge 40.
  - Un nouveau struct construit à l'aide de la fonction `newPerson` avec le nom "Jon" et l'âge 42.
  - Le champ `name` d'un struct avec le nom "Sean" et l'âge 50.
  - Le champ `age` d'un pointeur de struct vers un struct avec le nom "Sean" et l'âge 50.
  - Le champ `age` d'un pointeur de struct vers un struct avec le nom "Sean" et l'âge 50 après que le champ `age` ait été mis à jour à 51.

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

Voici le code complet :

```go
// Les _structs_ de Go sont des collections typées de champs.
// Ils sont utiles pour regrouper des données pour former
// des enregistrements.

package main

import "fmt"

// Ce type de struct `person` a les champs `name` et `age`.
type person struct {
	name string
	age  int
}

// `newPerson` construit un nouveau struct `person` avec le nom donné.
func newPerson(name string) *person {
	// Vous pouvez retourner en toute sécurité un pointeur vers une variable locale
	// car une variable locale survivra à la portée de la fonction.
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// Cette syntaxe crée un nouveau struct.
	fmt.Println(person{"Bob", 20})

	// Vous pouvez nommer les champs lors de l'initialisation d'un struct.
	fmt.Println(person{name: "Alice", age: 30})

	// Les champs omis seront initialisés avec leur valeur par défaut.
	fmt.Println(person{name: "Fred"})

	// Un préfixe `&` produit un pointeur vers le struct.
	fmt.Println(&person{name: "Ann", age: 40})

	// Il est courant d'encapsuler la création de nouveaux structs dans des fonctions constructeurs
	fmt.Println(newPerson("Jon"))

	// Accédez aux champs d'un struct avec un point.
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// Vous pouvez également utiliser des points avec des pointeurs de struct - les
	// pointeurs sont automatiquement déréférencés.
	sp := &s
	fmt.Println(sp.age)

	// Les structs sont mutables.
	sp.age = 51
	fmt.Println(sp.age)
}

```
