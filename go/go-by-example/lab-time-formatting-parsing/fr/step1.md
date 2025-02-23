# Formatage et analyse du temps

Le problème est de formater et d'analyser le temps en Golang en utilisant les formats de mise en page fournis.

- Utilisez le package `time` pour formater et analyser le temps.
- Utilisez le format de mise en page `time.RFC3339` pour formater et analyser le temps.
- Utilisez l'heure de référence `Mon Jan 2 15:04:05 MST 2006` pour montrer le modèle avec lequel formater/analyser une heure/chaîne donnée.
- Utilisez la fonction `Parse` pour analyser le temps.
- Utilisez la fonction `Format` pour formater le temps.
- Utilisez la fonction `fmt.Println` pour afficher l'heure formatée.
- Utilisez la fonction `fmt.Printf` pour afficher l'heure formatée avec les composants extraits.

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006":...
```

Voici le code complet ci-dessous :

```go
// Go prend en charge le formatage et l'analyse du temps via
// des formats de mise en page basés sur des modèles.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Voici un exemple de base de formatage d'une heure
	// selon RFC3339, en utilisant la constante de format de mise en page
	// correspondante.
	t := time.Now()
	p(t.Format(time.RFC3339))

	// L'analyse du temps utilise les mêmes valeurs de format de mise en page que `Format`.
	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	// `Format` et `Parse` utilisent des formats de mise en page basés sur des exemples. Généralement
	// vous utiliserez une constante de `time` pour ces formats de mise en page, mais
	// vous pouvez également fournir des formats de mise en page personnalisés. Les formats de mise en page doivent utiliser l'heure de référence `Mon Jan 2 15:04:05 MST 2006` pour montrer le modèle avec lequel formater/analyser une heure/chaîne donnée.
	// L'heure d'exemple doit être exactement comme montrée : l'année 2006,
	// 15 pour l'heure, lundi pour le jour de la semaine, etc.
	p(t.Format("3:04PM"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))
	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// Pour des représentations purement numériques, vous pouvez également
	// utiliser la mise en forme de chaîne standard avec les composants extraits
	// de la valeur de temps.
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// `Parse` renverra une erreur en cas d'entrée malformée
	// en expliquant le problème d'analyse.
	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}

```
