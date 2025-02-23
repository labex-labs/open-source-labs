# Modèles de texte

Dans ce laboratoire, vous devez démontrer l'utilisation du package `text/template` pour générer du contenu dynamique.

- Utilisez le package `text/template` pour générer du contenu dynamique.
- Utilisez la fonction `template.Must` pour générer une panique si `Parse` renvoie une erreur.
- Utilisez l'action `{{.FieldName}}` pour accéder aux champs d'un struct.
- Utilisez l'action `{{if. -}} oui {{else -}} non {{end}}\n` pour fournir une exécution conditionnelle pour les modèles.
- Utilisez l'action `{{range.}}{{.}} {{end}}\n` pour parcourir des slices, des tableaux, des maps ou des canaux.

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

Voici le code complet ci-dessous :

```go
// Go offre une prise en charge intégrée pour créer du contenu dynamique ou afficher une sortie personnalisée
// à l'utilisateur avec le package `text/template`. Un package frère
// nommé `html/template` fournit l'API identique mais a des fonctionnalités de sécurité supplémentaires
// et devrait être utilisé pour générer du HTML.

package main

import (
	"os"
	"text/template"
)

func main() {

	// Nous pouvons créer un nouveau modèle et analyser son corps à partir d'une chaîne de caractères.
	// Les modèles sont un mélange de texte statique et d'"actions" encadrées par
	// `{{...}}` qui sont utilisées pour insérer dynamiquement du contenu.
	t1 := template.New("t1")
	t1, err := t1.Parse("Valeur est {{.}}\n")
	if err!= nil {
		panic(err)
	}

	// Alternativement, nous pouvons utiliser la fonction `template.Must` pour
	// générer une panique si `Parse` renvoie une erreur. Cela est particulièrement
	// utile pour les modèles initialisés dans la portée globale.
	t1 = template.Must(t1.Parse("Valeur : {{.}}\n"))

	// En "exécutant" le modèle, nous générons son texte avec des valeurs spécifiques pour ses actions.
	// L'action `{{.}}` est remplacée par la valeur passée en tant que paramètre à `Execute`.
	t1.Execute(os.Stdout, "du texte")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// Fonction d'aide que nous utiliserons plus bas.
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// Si les données sont un struct, nous pouvons utiliser l'action `{{.FieldName}}` pour accéder
	// à ses champs. Les champs doivent être exportés pour être accessibles lorsque
	// un modèle est exécuté.
	t2 := Create("t2", "Nom : {{.Nom}}\n")

	t2.Execute(os.Stdout, struct {
		Nom string
	}{"Jane Doe"})

	// Le même principe s'applique aux maps ; avec les maps, il n'y a pas de restriction
	// sur la casse des noms de clés.
	t2.Execute(os.Stdout, map[string]string{
		"Nom": "Mickey Mouse",
	})

	// if/else fournissent une exécution conditionnelle pour les modèles. Une valeur est considérée
	// comme fausse si elle est la valeur par défaut d'un type, telle que 0, une chaîne vide,
	// un pointeur nil, etc.
	// Ceci est un exemple montrant une autre
	// fonctionnalité des modèles : l'utilisation du `-` dans les actions pour supprimer les espaces blancs.
	t3 := Create("t3",
		"{{if. -}} oui {{else -}} non {{end}}\n")
	t3.Execute(os.Stdout, "non vide")
	t3.Execute(os.Stdout, "")

	// Les blocs range nous permettent de parcourir des slices, des tableaux, des maps ou des canaux.
	// À l'intérieur du bloc range, `{{.}}` est défini sur l'élément actuel de l'itération.
	t4 := Create("t4",
		"Plage : {{range.}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}

```
