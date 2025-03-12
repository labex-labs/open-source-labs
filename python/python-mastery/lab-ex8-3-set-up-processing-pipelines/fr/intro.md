# Introduction

Dans ce laboratoire, vous apprendrez à utiliser les coroutines pour construire des pipelines de traitement de données. Les coroutines, une fonctionnalité puissante de Python, prennent en charge le multitâche coopératif, permettant aux fonctions de suspendre et de reprendre leur exécution ultérieurement.

Les objectifs de ce laboratoire sont de comprendre le fonctionnement des coroutines en Python, de mettre en œuvre des pipelines de traitement de données basés sur les coroutines et de transformer les données à travers plusieurs étapes de coroutines. Vous allez créer deux fichiers : `cofollow.py`, un suivi de fichier basé sur les coroutines, et `coticker.py`, une application de suivi des cours boursiers utilisant les coroutines. On suppose que le programme `stocksim.py` de l'exercice précédent est toujours en cours d'exécution en arrière-plan, générant des données boursières dans un fichier journal.
