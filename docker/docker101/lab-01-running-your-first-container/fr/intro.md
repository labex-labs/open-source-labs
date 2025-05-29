# Introduction

Dans ce laboratoire, vous exécuterez votre premier conteneur Docker.

Les conteneurs ne sont qu'un processus (ou un groupe de processus) s'exécutant en isolation. L'isolation est obtenue grâce aux espaces de noms Linux, aux groupes de contrôle (cgroups), à seccomp et à SELinux. Notez que les espaces de noms Linux et les groupes de contrôle sont intégrés au noyau Linux! En dehors du noyau Linux lui-même, il n'y a rien de spécial dans les conteneurs.

Ce qui rend les conteneurs utiles, c'est l'outil qui les entoure. Pour ces laboratoires, nous utiliserons Docker, qui est un outil largement adopté pour utiliser des conteneurs pour construire des applications. Docker fournit aux développeurs et aux opérateurs une interface conviviale pour construire, expédier et exécuter des conteneurs dans n'importe quel environnement doté d'un moteur Docker. Comme le client Docker nécessite un moteur Docker, une alternative est d'utiliser [Podman](https://podman.io/), qui est un moteur de conteneurs sans démon pour développer, gérer et exécuter des conteneurs [OCI](https://opencontainers.org/) et est capable d'exécuter des conteneurs en tant que root ou en mode sans root. Pour ces raisons, nous recommandons Podman, mais en raison de son adoption, ce laboratoire utilise toujours Docker.

Dans la première partie de ce laboratoire, nous exécuterons notre premier conteneur et apprendrons à l'inspecter. Nous pourrons constater l'isolation d'espace de noms que nous obtenons à partir du noyau Linux.

Après avoir exécuté notre premier conteneur, nous plongerons dans d'autres utilisations des conteneurs. Vous pouvez trouver de nombreux exemples de cela sur le Docker Store, et nous exécuterons plusieurs types différents de conteneurs sur le même hôte. Cela nous permettra de voir l'avantage de l'isolation - où nous pouvons exécuter plusieurs conteneurs sur le même hôte sans conflits.

Nous utiliserons quelques commandes Docker dans ce laboratoire. Pour la documentation complète des commandes disponibles, consultez la [documentation officielle](https://docs.docker.com/).

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Ceci est un Guided Lab, qui fournit des instructions étape par étape pour vous aider à apprendre et à pratiquer. Suivez attentivement les instructions pour compléter chaque étape et acquérir une expérience pratique. Les données historiques montrent que c'est un laboratoire de niveau <span class="text-green-600 dark:text-green-400">débutant</span> avec un taux de réussite de <span class="text-green-600 dark:text-green-400">89.29%</span>. Il a reçu un taux d'avis positifs de <span class="text-primary-600 dark:text-primary-400">92.31%</span> de la part des apprenants.
</div>
