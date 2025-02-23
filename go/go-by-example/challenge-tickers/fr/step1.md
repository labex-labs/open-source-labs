# Horloges et tics (Timers and Tickers)

Dans ce défi, vous devez créer un tic (ticker) qui sonne tous les 500 ms jusqu'à ce que nous l'arrêtions. Vous utiliserez un canal pour attendre les valeurs à mesure qu'elles arrivent.

## Exigences

- Utilisez le package `time` pour créer un tic (ticker).
- Utilisez un canal pour attendre les valeurs à mesure qu'elles arrivent.
- Utilisez l'instruction `select` pour recevoir les valeurs du canal.
- Arrêtez le tic (ticker) après 1600 ms.

## Exemple

```sh
# Lorsque nous exécutons ce programme, le tic (ticker) devrait sonner 3 fois
# avant que nous ne l'arrêtions.
$ go run tickers.go
Tick at 2012-09-23 11:29:56.487625 -0700 PDT
Tick at 2012-09-23 11:29:56.988063 -0700 PDT
Tick at 2012-09-23 11:29:57.488076 -0700 PDT
Ticker stopped
```
