# Introduction

Dans ce laboratoire, nous nous appuyons sur les connaissances acquises dans le laboratoire 1 où nous avons utilisé des commandes Docker pour exécuter des conteneurs. Nous allons créer une image Docker personnalisée à partir d'un Dockerfile. Une fois que nous aurons construit l'image, nous la pousserons vers un registre central où elle pourra être extraite pour être déployée dans d'autres environnements. Nous décrirons également brièvement les couches d'image, et la manière dont Docker incorpore le "copy-on-write" et le système de fichiers union pour stocker efficacement les images et exécuter les conteneurs.

Nous utiliserons quelques commandes Docker dans ce laboratoire. Pour la documentation complète des commandes disponibles, consultez la [documentation officielle](https://docs.docker.com/).

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Ceci est un Guided Lab, qui fournit des instructions étape par étape pour vous aider à apprendre et à pratiquer. Suivez attentivement les instructions pour compléter chaque étape et acquérir une expérience pratique. Les données historiques montrent que c'est un laboratoire de niveau <span class="text-green-600 dark:text-green-400">débutant</span> avec un taux de réussite de <span class="text-green-600 dark:text-green-400">82.35%</span>. Il a reçu un taux d'avis positifs de <span class="text-primary-600 dark:text-primary-400">100%</span> de la part des apprenants.
</div>
