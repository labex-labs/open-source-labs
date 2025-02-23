# Directive d'insertion

Votre tâche consiste à modifier le code donné pour insérer des fichiers et des dossiers dans le binaire Go et à afficher leur contenu.

## Exigences

- Vous devez utiliser le package `embed` pour insérer des fichiers et des dossiers.
- Vous devez utiliser les types `string` et `[]byte` pour stocker le contenu des fichiers insérés.
- Vous devez utiliser le type `embed.FS` pour insérer plusieurs fichiers ou dossiers avec des caractères joker.
- Vous devez afficher le contenu des fichiers insérés.

## Exemple

```sh
# Utilisez ces commandes pour exécuter l'exemple.
# (Note: en raison des limitations de la plateforme de démonstration Go,
# cet exemple ne peut être exécuté que sur votre ordinateur local.)
$ mkdir -p dossier
$ echo "bonjour go" > dossier/fichier_unique.txt
$ echo "123" > dossier/fichier1.hash
$ echo "456" > dossier/fichier2.hash

$ go run embed-directive.go
bonjour go
bonjour go
123
456
```
