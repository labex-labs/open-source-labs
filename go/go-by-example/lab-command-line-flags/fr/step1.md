# Drapeaux de ligne de commande

Implémentez un programme en Golang qui analyse les drapeaux de ligne de commande et affiche les options analysées et tous les arguments positionnels de fin. Le programme devrait prendre en charge les drapeaux suivants :

- `word` : un drapeau de chaîne de caractères avec une valeur par défaut de `"foo"`.
- `numb` : un drapeau entier avec une valeur par défaut de `42`.
- `fork` : un drapeau booléen avec une valeur par défaut de `false`.
- `svar` : un drapeau de chaîne de caractères qui utilise une variable existante déclarée ailleurs dans le programme.

- Le programme devrait utiliser le package `flag` pour analyser les drapeaux de ligne de commande.
- Le programme devrait afficher les options analysées et tous les arguments positionnels de fin.
- Le programme devrait prendre en charge les drapeaux `word`, `numb`, `fork` et `svar` tels que décrits ci-dessus.

```sh
# Pour expérimenter le programme de drapeaux de ligne de commande,
# il est préférable de le compiler d'abord puis d'exécuter le binaire
# résultant directement.
$ go build command-line-flags.go

# Essayez le programme compilé en donnant d'abord des valeurs
# pour tous les drapeaux.
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# Notez que si vous omettez les drapeaux, ils prennent automatiquement
# leurs valeurs par défaut.
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# Les arguments positionnels de fin peuvent être fournis après
# tous les drapeaux.
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# Notez que le package `flag` exige que tous les drapeaux apparaissent
# avant les arguments positionnels (sinon les drapeaux seront interprétés
# comme des arguments positionnels).
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# Utilisez les drapeaux `-h` ou `--help` pour obtenir le texte d'aide
# automatiquement généré pour le programme de ligne de commande.
$./command-line-flags -h
Usage de./command-line-flags:
-fork=false: un booléen
-numb=42: un entier
-svar="bar": une variable chaîne de caractères
-word="foo": une chaîne de caractères

# Si vous fournissez un drapeau qui n'a pas été spécifié au
# package `flag`, le programme affichera un message d'erreur
# et montrera à nouveau le texte d'aide.
$./command-line-flags -wat
flag fourni mais non défini : -wat
Usage de./command-line-flags:
...
```

Voici le code complet ci-dessous :

```go
// [_Les drapeaux de ligne de commande_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// sont un moyen courant de spécifier des options pour les programmes
// de ligne de commande. Par exemple, dans `wc -l`, le `-l` est un
// drapeau de ligne de commande.

package main

// Go fournit un package `flag` prenant en charge l'analyse de base
// des drapeaux de ligne de commande. Nous utiliserons ce package pour
// implémenter notre exemple de programme de ligne de commande.
import (
	"flag"
	"fmt"
)

func main() {

	// Les déclarations de drapeaux de base sont disponibles pour les
	// options de chaîne de caractères, d'entier et de booléen. Ici, nous
	// déclarons un drapeau de chaîne de caractères `word` avec une valeur
	// par défaut `"foo"` et une courte description. Cette fonction
	// `flag.String` renvoie un pointeur de chaîne de caractères (pas
	// une valeur de chaîne de caractères) ; nous verrons comment utiliser
	// ce pointeur ci-dessous.
	wordPtr := flag.String("word", "foo", "une chaîne de caractères")

	// Cela déclare les drapeaux `numb` et `fork`, en utilisant une
	// approche similaire au drapeau `word`.
	numbPtr := flag.Int("numb", 42, "un entier")
	forkPtr := flag.Bool("fork", false, "un booléen")

	// Il est également possible de déclarer une option qui utilise une
	// variable existante déclarée ailleurs dans le programme. Notez que
	// nous devons passer un pointeur à la fonction de déclaration de
	// drapeau.
	var svar string
	flag.StringVar(&svar, "svar", "bar", "une variable chaîne de caractères")

	// Une fois que tous les drapeaux sont déclarés, appelez `flag.Parse()`
	// pour exécuter l'analyse de ligne de commande.
	flag.Parse()

	// Ici, nous allons simplement afficher les options analysées et
	// tous les arguments positionnels de fin. Notez que nous devons
	// déréférencer les pointeurs avec par exemple `*wordPtr` pour obtenir
	// les valeurs d'option réelles.
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}

```
