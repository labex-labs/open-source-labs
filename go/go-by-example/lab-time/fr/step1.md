# Time

Le code ci-dessous contient des exemples de manipulation du temps et de la durée en Go. Cependant, certaines parties du code sont manquantes. Votre tâche est de compléter le code pour qu'il fonctionne comme prévu.

- Connaissance de base du langage de programmation Go.
- Familiarité avec le support du temps et de la durée en Go.

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# Ensuite, nous examinerons l'idée liée du temps par rapport à
# l'époque Unix.
```

Voici le code complet :

```go
// Go offre un large support pour les temps et les durées ;
// voici quelques exemples.

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Nous commencerons par obtenir l'heure actuelle.
	now := time.Now()
	p(now)

	// Vous pouvez construire une structure `time` en fournissant
	// l'année, le mois, le jour, etc. Les temps sont toujours associés
	// à un `Location`, c'est-à-dire une zone horaire.
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// Vous pouvez extraire les différents composants de la valeur de temps
	// comme prévu.
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// Le `Weekday` de lundi au dimanche est également disponible.
	p(then.Weekday())

	// Ces méthodes comparent deux temps, en testant si le
	// premier se produit avant, après ou en même temps
	// que le second, respectivement.
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// La méthode `Sub` renvoie une `Duration` représentant
	// l'intervalle entre deux temps.
	diff := now.Sub(then)
	p(diff)

	// Nous pouvons calculer la longueur de la durée en
	// différents unités.
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// Vous pouvez utiliser `Add` pour avancer un temps d'une durée donnée,
	// ou avec un `-` pour reculer d'une durée.
	p(then.Add(diff))
	p(then.Add(-diff))
}

```
