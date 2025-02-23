# Command Line Subcommands

Vous êtes requis de créer un programme qui prend en charge deux sous-commandes, `foo` et `bar`, chacune avec son propre ensemble de drapeaux. La sous-commande `foo` devrait avoir deux drapeaux, `enable` et `name`, tandis que la sous-commande `bar` devrait avoir un drapeau, `level`.

- Le programme devrait utiliser le package `flag` pour définir et analyser les drapeaux.
- La sous-commande `foo` devrait avoir deux drapeaux, `enable` et `name`, tous deux de type chaîne de caractères.
- La sous-commande `bar` devrait avoir un drapeau, `level`, de type entier.
- Le programme devrait afficher un message d'erreur si une sous-commande invalide est fournie.
- Le programme devrait afficher les valeurs des drapeaux pour la sous-commande qui est invoquée.

```sh
$ go build command-line-subcommands.go

# Premièrement, invoquez la sous-commande foo.
$./command-line-subcommands foo -enable -name=joe a1 a2
sous-commande 'foo'
enable: true
name: joe
tail: [a1 a2]

# Maintenant, essayez bar.
$./command-line-subcommands bar -level 8 a1
sous-commande 'bar'
level: 8
tail: [a1]

# Mais bar n'acceptera pas les drapeaux de foo.
$./command-line-subcommands bar -enable a1
drapeau fourni mais non défini: -enable
Utilisation de bar:
-level int
niveau

# Ensuite, nous examinerons les variables d'environnement, une autre manière commune
# de paramétrer les programmes.
```

Voici le code complet ci-dessous :

```go
// Certains outils de ligne de commande, comme l'outil `go` ou `git`
// ont de nombreuses *sous-commandes*, chacune avec son propre ensemble de
// drapeaux. Par exemple, `go build` et `go get` sont deux
// sous-commandes différentes de l'outil `go`.
// Le package `flag` nous permet de définir facilement des
// sous-commandes simples qui ont leurs propres drapeaux.

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// Nous déclarons une sous-commande en utilisant la fonction `NewFlagSet`
	// et procédons à définir de nouveaux drapeaux spécifiques
	// à cette sous-commande.
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "activer")
	fooName := fooCmd.String("name", "", "nom")

	// Pour une sous-commande différente, nous pouvons définir différents
	// drapeaux pris en charge.
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "niveau")

	// La sous-commande est attendue en tant que premier argument
	// du programme.
	if len(os.Args) < 2 {
		fmt.Println("sous-commandes 'foo' ou 'bar' attendues")
		os.Exit(1)
	}

	// Vérifions quelle sous-commande est invoquée.
	switch os.Args[1] {

	// Pour chaque sous-commande, nous analysons ses propres drapeaux et
	// avons accès aux arguments positionnels de fin.
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("sous-commande 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("sous-commande 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("sous-commandes 'foo' ou 'bar' attendues")
		os.Exit(1)
	}
}

```
