# Command Line Subcommands

Vous êtes requis de créer un programme qui prend en charge deux sous-commandes, `foo` et `bar`, chacune avec son propre ensemble de drapeaux. La sous-commande `foo` devrait avoir deux drapeaux, `enable` et `name`, tandis que la sous-commande `bar` devrait avoir un drapeau, `level`.

## Exigences

- Le programme devrait utiliser le package `flag` pour définir et analyser les drapeaux.
- La sous-commande `foo` devrait avoir deux drapeaux, `enable` et `name`, tous deux de type chaîne de caractères.
- La sous-commande `bar` devrait avoir un drapeau, `level`, de type entier.
- Le programme devrait afficher un message d'erreur si une sous-commande invalide est fournie.
- Le programme devrait afficher les valeurs des drapeaux pour la sous-commande qui est invoquée.

## Exemple

```sh
$ go build command-line-subcommands.go

# Premièrement, invoquez la sous-commande foo.
$./command-line-subcommands foo -enable -name=joe a1 a2
sous-commande 'foo'
enable: true
name: joe
queue: [a1 a2]

# Maintenant, essayez bar.
$./command-line-subcommands bar -level 8 a1
sous-commande 'bar'
niveau: 8
queue: [a1]

# Mais bar n'acceptera pas les drapeaux de foo.
$./command-line-subcommands bar -enable a1
drapeau fourni mais non défini: -enable
Utilisation de bar:
-niveau int
niveau

# Ensuite, nous examinerons les variables d'environnement, une autre manière commune
# de paramétrer les programmes.
```
