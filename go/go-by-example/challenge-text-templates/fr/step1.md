# Modèles de texte

Dans ce défi, vous devez démontrer l'utilisation du package `text/template` pour générer du contenu dynamique.

## Exigences

- Utiliser le package `text/template` pour générer du contenu dynamique.
- Utiliser la fonction `template.Must` pour générer une panique si `Parse` renvoie une erreur.
- Utiliser l'action `{{.FieldName}}` pour accéder aux champs de struct.
- Utiliser l'action `{{if. -}} oui {{else -}} non {{end}}\n` pour fournir une exécution conditionnelle pour les modèles.
- Utiliser l'action `{{range.}}{{.}} {{end}}\n` pour parcourir des slices, des tableaux, des cartes ou des canaux.

## Exemple

```sh
$ go run templates.go
Valeur : du texte
Valeur : 5
Valeur : [Go Rust C++ C#]
Nom : Jane Doe
Nom : Mickey Mouse
oui
non
Plage : Go Rust C++ C#
```
