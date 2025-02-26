# Problem: Main Scripts

Exécuter un sous-module de package en tant que script principal ne fonctionne pas.

```bash
$ python porty/pcost.py # NE FONCTIONNE PAS
...
```

_Raison : Vous exécutez Python sur un seul fichier et Python ne voit pas correctement le reste de la structure du package (`sys.path` est incorrect)._

Toutes les importations ne fonctionnent pas. Pour résoudre ce problème, vous devez exécuter votre programme d'une manière différente, en utilisant l'option `-m`.

```bash
$ python -m porty.pcost # FONCTIONNE
...
```
