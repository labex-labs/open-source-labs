# Drapeaux de ligne de commande

Mettez en œuvre un programme Golang qui analyse les drapeaux de ligne de commande et affiche les options analysées et tous les arguments positionnels de fin. Le programme devrait prendre en charge les drapeaux suivants :

- `word` : un drapeau de chaîne avec une valeur par défaut de `"foo"`.
- `numb` : un drapeau entier avec une valeur par défaut de `42`.
- `fork` : un drapeau booléen avec une valeur par défaut de `false`.
- `svar` : un drapeau de chaîne qui utilise une variable existante déclarée ailleurs dans le programme.

## Exigences

- Le programme devrait utiliser le package `flag` pour analyser les drapeaux de ligne de commande.
- Le programme devrait afficher les options analysées et tous les arguments positionnels de fin.
- Le programme devrait prendre en charge les drapeaux `word`, `numb`, `fork` et `svar` tels que décrits ci-dessus.

## Exemple

```sh
# Pour expérimenter avec le programme de drapeaux de ligne de commande,
# il est recommandé de le compiler d'abord puis d'exécuter le binaire résultant directement.
$ go build command-line-flags.go

# Essayez le programme compilé en donnant d'abord des valeurs à
# tous les drapeaux.
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
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# Si vous fournissez un drapeau qui n'a pas été spécifié au
# package `flag`, le programme affichera un message d'erreur
# et montrera à nouveau le texte d'aide.
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```
