# Bind Mounts

La syntaxe `mount` est recommandée par Docker plutôt que la syntaxe `volume`. Les bind mounts ont une fonctionnalité limitée par rapport aux volumes. Un fichier ou un répertoire est référencé par son chemin complet sur la machine hôte lorsqu'il est monté dans un conteneur. Les bind mounts dépendent de la structure de répertoire spécifique du système de fichiers de la machine hôte et vous ne pouvez pas utiliser l'interface de ligne de commande Docker pour gérer les bind mounts. Notez que les bind mounts peuvent modifier le système de fichiers hôte via des processus exécutés dans un conteneur.

Au lieu d'utiliser la syntaxe `-v` avec trois champs séparés par le séparateur deux-points (:), la syntaxe `mount` est plus verbeuse et utilise plusieurs paires `clé-valeur` :

- type : bind, volume ou tmpfs,
- source : chemin vers le fichier ou le répertoire sur la machine hôte,
- destination : chemin dans le conteneur,
- readonly,
- bind-propagation : rprivate, private, rshared, shared, rslave, slave,
- cohérence : cohérente, déléguée, mise en cache,
- montage.

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

Tapez la commande dans le conteneur :

```
echo "hello busybox" > /data/hi.txt
exit
```

Vérifiez que le fichier a été créé sur la machine hôte.

```
cat data/hi.txt
```
