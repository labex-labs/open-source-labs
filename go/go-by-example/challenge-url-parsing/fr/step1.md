# Analyse d'URL

Le défi consiste à analyser une URL d'échantillonnage qui inclut un schéma, des informations d'authentification, un hôte, un port, un chemin, des paramètres de requête et un fragment de requête. L'URL analysée doit être utilisée pour extraire les composants individuels de l'URL.

## Exigences

- Les packages `url` et `net` doivent être importés.
- L'URL d'échantillonnage doit être analysée et vérifiée sur erreurs.
- Le schéma, les informations d'authentification, l'hôte, le port, le chemin, les paramètres de requête et le fragment de requête doivent être extraits de l'URL analysée.
- La fonction `SplitHostPort` doit être utilisée pour extraire le nom d'hôte et le port du champ `Host`.
- La fonction `ParseQuery` doit être utilisée pour analyser les paramètres de requête dans une carte.

## Exemple

```sh
# Exécution de notre programme d'analyse d'URL montre tous les différents
# éléments que nous avons extraits.
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
