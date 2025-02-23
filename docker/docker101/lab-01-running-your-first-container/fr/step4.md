# Nettoyage

La fin de ce laboratoire a entraîné la création d'un certain nombre de conteneurs en cours d'exécution sur votre hôte. Nettoyons-les.

Tout d'abord, obtenez la liste des conteneurs en cours d'exécution en utilisant `docker container ls`.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." Il y a 3 minutes Up il y a 3 minutes 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." Il y a 3 minutes Up il y a 3 minutes 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" Il y a 8 minutes Up il y a 8 minutes priceless_kepler
```

Ensuite, exécutez `docker container stop [container id]` pour chaque conteneur de la liste. Vous pouvez également utiliser les noms des conteneurs que vous avez spécifiés précédemment.

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**Note** : Vous n'avez qu'à référencer suffisamment de chiffres de l'ID pour qu'il soit unique. Trois chiffres sont presque toujours suffisants.

Supprimez les conteneurs arrêtés

`docker system prune` est une commande très pratique pour nettoyer votre système. Elle supprimera tous les conteneurs arrêtés, tous les volumes inutilisés et les réseaux, ainsi que les images orphelines.

```bash
$ docker system prune
AVERTISSEMENT! Cela supprimera :
- tous les conteneurs arrêtés
- tous les volumes non utilisés par au moins un conteneur
- tous les réseaux non utilisés par au moins un conteneur
- toutes les images orphelines
Êtes-vous sûr de vouloir continuer? [y/N] y
Conteneurs supprimés :
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Espace récupéré au total : 12B
```
