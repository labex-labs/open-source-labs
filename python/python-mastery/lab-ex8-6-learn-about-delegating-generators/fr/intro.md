# Introduction

**Objectifs :**

- Découvrir les générateurs délégués

**Fichiers modifiés** : `cofollow.py`, `server.py`

Un problème potentiel dans le code qui repose sur les générateurs est celui de cacher les détails aux utilisateurs et en écrivant des bibliothèques. Beaucoup de mécanismes de bas niveau sont généralement nécessaires pour piloter tout et il est souvent assez gênant de l'exposer directement aux utilisateurs.

À partir de Python 3.3, une nouvelle instruction `yield from` peut être utilisée pour déléguer des générateurs à une autre fonction. C'est un moyen utile de nettoyer le code qui repose sur les générateurs.
