# Introduction

Dans ce laboratoire, vous allez apprendre à connaître les générateurs gérés (managed generators) et comprendre comment les piloter de manière inhabituelle. Vous allez également construire un simple planificateur de tâches (task scheduler) et créer un serveur réseau en utilisant des générateurs.

Une fonction générateur en Python nécessite un code externe pour s'exécuter. Par exemple, un générateur d'itération ne fonctionne que lorsqu'il est itéré avec une boucle `for`, et les coroutines ont besoin que leur méthode `send()` soit appelée. Dans ce laboratoire, nous allons explorer des exemples pratiques de pilotage de générateurs dans des applications avancées. Les fichiers créés lors de ce laboratoire sont `multitask.py` et `server.py`.
