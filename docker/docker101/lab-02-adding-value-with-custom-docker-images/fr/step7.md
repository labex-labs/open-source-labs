# Nettoyer

La fin de ce laboratoire résulte d'un certain nombre de conteneurs en cours d'exécution sur votre hôte. Nettoyons-les.

Exécutez `docker container stop [id du conteneur]` pour chaque conteneur en cours d'exécution

Commencez par obtenir une liste des conteneurs en cours d'exécution en utilisant `docker container ls`.

```bash
$ docker container ls
```

Ensuite, exécutez la commande pour chaque conteneur de la liste.

```bash
$ docker container stop <id_du_conteneur>
```

Supprimez les conteneurs arrêtés

`docker system prune` est une commande très pratique pour nettoyer votre système. Elle supprimera tous les conteneurs arrêtés, les volumes et les réseaux inutilisés, et les images orphelines.

```bash
$ docker system prune
AVERTISSEMENT! Cela supprimera :
- tous les conteneurs arrêtés
- tous les volumes non utilisés par au moins un conteneur
- tous les réseaux non utilisés par au moins un conteneur
- toutes les images orphelines
Êtes-vous sûr de vouloir continuer? [y/N] y
Conteneurs supprimés :
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Espace total récupéré : 300,3 kB
```
