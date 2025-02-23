# Limitation de débit

Le problème consiste à limiter la gestion des requêtes entrantes pour maintenir la qualité de service et contrôler l'utilisation des ressources.

## Exigences

- Langage de programmation Go
- Compréhension de base des goroutines, des canaux et des minuteurs

## Exemple

```sh
# En exécutant notre programme, nous voyons que le premier lot de requêtes
# est traité une fois toutes les ~200 millisecondes comme prévu.
$ go run rate-limiting.go
requête 1 2012-10-19 00:38:18.687438 +0000 UTC
requête 2 2012-10-19 00:38:18.887471 +0000 UTC
requête 3 2012-10-19 00:38:19.087238 +0000 UTC
requête 4 2012-10-19 00:38:19.287338 +0000 UTC
requête 5 2012-10-19 00:38:19.487331 +0000 UTC

# Pour le second lot de requêtes, nous servons les 3 premières
# immédiatement en raison de la limitation de débit pouvant supporter des pics,
# puis nous servons les 2 restantes avec des délais d'environ 200 ms chacun.
requête 1 2012-10-19 00:38:20.487578 +0000 UTC
requête 2 2012-10-19 00:38:20.487645 +0000 UTC
requête 3 2012-10-19 00:38:20.487676 +0000 UTC
requête 4 2012-10-19 00:38:20.687483 +0000 UTC
requête 5 2012-10-19 00:38:20.887542 +0000 UTC
```
