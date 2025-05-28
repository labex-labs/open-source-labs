# Introduction

Dans ce laboratoire, vous allez apprendre à connaître les générateurs gérés (managed generators) et comprendre comment les piloter de manière inhabituelle. Vous allez également construire un simple planificateur de tâches (task scheduler) et créer un serveur réseau en utilisant des générateurs.

Une fonction générateur en Python nécessite un code externe pour s'exécuter. Par exemple, un générateur d'itération ne fonctionne que lorsqu'il est itéré avec une boucle `for`, et les coroutines ont besoin que leur méthode `send()` soit appelée. Dans ce laboratoire, nous allons explorer des exemples pratiques de pilotage de générateurs dans des applications avancées. Les fichiers créés lors de ce laboratoire sont `multitask.py` et `server.py`.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Ceci est un Guided Lab, qui fournit des instructions étape par étape pour vous aider à apprendre et à pratiquer. Suivez attentivement les instructions pour compléter chaque étape et acquérir une expérience pratique. Les données historiques montrent que c'est un laboratoire de niveau <span class="text-green-600 dark:text-green-400">débutant</span> avec un taux de réussite de <span class="text-green-600 dark:text-green-400">84.21%</span>.
</div>
