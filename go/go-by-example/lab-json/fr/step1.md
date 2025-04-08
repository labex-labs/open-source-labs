# JSON

Vous êtes requis de compléter le code fourni pour encoder et décoder des données JSON en Golang. Le code contient des exemples d'encodage et de décodage de types de données de base, ainsi que de types de données personnalisés.

- Connaissance de base du langage de programmation Golang.
- Familiarité avec l'encodage et le décodage de données JSON en Golang.
- Capacité à lire et à comprendre le code Golang existant.

```sh


# Nous avons couvert les bases du JSON en Go ici, mais consultez
# l'article de blog [JSON and Go](https://go.dev/blog/json)
# et la documentation du package [JSON](https://pkg.go.dev/encoding/json)
# pour en savoir plus.
```

Voici le code complet ci-dessous :

```go
// Go offre une prise en charge intégrée de l'encodage et
// du décodage JSON, y compris pour les types de données
// de base et personnalisés.

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// Nous utiliserons ces deux structs pour démontrer
// l'encodage et le décodage de types personnalisés ci-dessous.
type response1 struct {
	Page   int
	Fruits []string
}

// Seuls les champs exportés seront encodés/décodés en JSON.
// Les champs doivent commencer par une lettre majuscule
// pour être exportés.
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// Tout d'abord, nous allons examiner l'encodage de types
	// de données de base en chaînes JSON. Voici quelques
	// exemples pour des valeurs atomiques.
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// Et voici quelques exemples pour des slices et des maps,
	// qui s'encodent en tableaux JSON et en objets comme
	// vous l'attendez.
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// Le package JSON peut encoder automatiquement vos
	// types de données personnalisés. Il ne inclura que les
	// champs exportés dans la sortie encodée et utilisera
	// par défaut ces noms comme clés JSON.
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// Vous pouvez utiliser des balises dans les déclarations
	// de champs de struct pour personnaliser les noms de
	// clés JSON encodés. Consultez la définition de
	// `response2` ci-dessus pour voir un exemple de telles
	// balises.
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// Maintenant, examinons le décodage de données JSON
	// en valeurs Go. Voici un exemple pour une structure
	// de données générique.
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// Nous devons fournir une variable où le package JSON
	// peut placer les données décodées. Ce
	// `map[string]interface{}` contiendra une carte de
	// chaînes vers des types de données arbitraires.
	var dat map[string]interface{}

	// Voici le décodage réel, et une vérification des
	// erreurs associées.
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// Pour utiliser les valeurs dans la carte décodée,
	// nous devrons les convertir en leur type approprié.
	// Par exemple, ici nous convertissons la valeur dans
	// `num` en type `float64` attendu.
	num := dat["num"].(float64)
	fmt.Println(num)

	// Accéder à des données imbriquées nécessite une
	// série de conversions.
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// Nous pouvons également décoder JSON dans des types
	// de données personnalisés. Cela a l'avantage d'ajouter
	// une sécurité de type supplémentaire à nos programmes
	// et d'éliminer la nécessité d'assertions de type
	// lors de l'accès aux données décodées.
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// Dans les exemples ci-dessus, nous avons toujours
	// utilisé des bytes et des chaînes comme intermédiaires
	// entre les données et la représentation JSON sur la
	// sortie standard. Nous pouvons également diffuser
	// des encodages JSON directement vers des `os.Writer`
	// comme `os.Stdout` ou même des corps de réponse HTTP.
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```
