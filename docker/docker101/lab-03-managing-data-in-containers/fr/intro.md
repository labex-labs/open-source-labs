# Introduction

Par défaut, tous les fichiers créés à l'intérieur d'un conteneur sont stockés sur une couche de conteneur modifiable. Cela signifie que :

- Si le conteneur n'existe plus, les données sont perdues,
- La couche modifiable du conteneur est étroitement couplée à la machine hôte, et
- Pour gérer le système de fichiers, vous avez besoin d'un pilote de stockage qui fournit un système de fichiers union, utilisant le noyau Linux. Cette abstraction supplémentaire réduit les performances par rapport aux `data volumes` qui écrivent directement dans le système de fichiers.

Docker propose deux options pour stocker des fichiers dans la machine hôte : `volumes` et `bind mounts`. Si vous exécutez Docker sur Linux, vous pouvez également utiliser un `tmpfs mount`, et avec Docker sur Windows, vous pouvez également utiliser un `named pipe`.

![Types of Mounts](../assets/types-of-mounts.png)

- Les `Volumes` sont stockés dans le système de fichiers hôte géré par Docker.
- Les `Bind mounts` sont stockés n'importe où dans le système hôte.
- Les `tmpfs mounts` sont stockés uniquement en mémoire de l'hôte.

À l'origine, le drapeau `--mount` était utilisé pour les services Docker Swarm et le drapeau `--volume` était utilisé pour les conteneurs autonomes. Depuis Docker 17.06 et versions ultérieures, vous pouvez également utiliser `--mount` pour les conteneurs autonomes et il est généralement plus explicite et verbeux que `--volume`.
