# Introduction

Dans ce laboratoire (lab), vous allez apprendre à déléguer des générateurs en Python en utilisant l'instruction `yield from`. Cette fonctionnalité, introduite en Python 3.3, simplifie le code qui dépend de générateurs et de coroutines.

Les générateurs sont des fonctions spéciales qui peuvent mettre en pause et reprendre leur exécution, tout en conservant leur état entre les appels. L'instruction `yield from` offre un moyen élégant de déléguer le contrôle à un autre générateur, améliorant ainsi la lisibilité et la maintenabilité du code.

**Objectifs :**

- Comprendre le but de l'instruction `yield from`
- Apprendre à utiliser `yield from` pour déléguer à d'autres générateurs
- Appliquer ces connaissances pour simplifier le code basé sur les coroutines
- Comprendre le lien avec la syntaxe moderne async/await

**Fichiers avec lesquels vous allez travailler :**

- `cofollow.py` - Contient des fonctions utilitaires pour les coroutines
- `server.py` - Contient une implémentation simple d'un serveur réseau
