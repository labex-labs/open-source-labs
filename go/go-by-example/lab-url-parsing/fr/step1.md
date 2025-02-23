# Analyse d'URL

Le laboratoire nécessite d'analyser une URL d'exemple qui inclut un schéma, des informations d'authentification, un hôte, un port, un chemin, des paramètres de requête et un fragment de requête. L'URL analysée devrait être utilisée pour extraire les composants individuels de l'URL.

- Les packages `url` et `net` doivent être importés.
- L'URL d'exemple devrait être analysée et vérifiée sur des erreurs.
- Le schéma, les informations d'authentification, l'hôte, le port, le chemin, les paramètres de requête et le fragment de requête devraient être extraits de l'URL analysée.
- La fonction `SplitHostPort` devrait être utilisée pour extraire le nom d'hôte et le port du champ `Host`.
- La fonction `ParseQuery` devrait être utilisée pour analyser les paramètres de requête dans une carte.

```sh
# Exécution de notre programme d'analyse d'URL montre tous les différents
# morceaux que nous avons extraits.
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```

Voici le code complet ci-dessous :

```go
// Les URL fournissent un [moyen uniforme de localiser des ressources](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Voici comment analyser les URL en Go.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// Nous allons analyser cette URL d'exemple, qui inclut un
	// schéma, des informations d'authentification, un hôte, un port, un chemin,
	// des paramètres de requête et un fragment de requête.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// Analyse l'URL et assurez-vous qu'il n'y a pas d'erreurs.
	u, err := url.Parse(s)
	if err!= nil {
		panic(err)
	}

	// Accéder au schéma est simple.
	fmt.Println(u.Scheme)

	// `User` contient toutes les informations d'authentification ; appelez
	// `Username` et `Password` sur ceci pour obtenir les valeurs individuelles.
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// Le `Host` contient à la fois le nom d'hôte et le port,
	// s'il est présent. Utilisez `SplitHostPort` pour les extraire.
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// Ici, nous extrayons le `path` et le fragment après
	// le `#`.
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// Pour obtenir les paramètres de requête au format chaîne de caractères `k=v`,
	// utilisez `RawQuery`. Vous pouvez également analyser les paramètres de requête
	// dans une carte. Les cartes de paramètres de requête analysées sont de
	// chaînes de caractères à des slices de chaînes de caractères, donc accédez à `[0]`
	// si vous ne voulez que la première valeur.
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```
