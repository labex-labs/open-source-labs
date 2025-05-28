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

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Ceci est un Guided Lab, qui fournit des instructions étape par étape pour vous aider à apprendre et à pratiquer. Suivez attentivement les instructions pour compléter chaque étape et acquérir une expérience pratique. Les données historiques montrent que c'est un laboratoire de niveau <span class="text-green-600 dark:text-green-400">débutant</span> avec un taux de réussite de <span class="text-green-600 dark:text-green-400">100%</span>.
</div>
