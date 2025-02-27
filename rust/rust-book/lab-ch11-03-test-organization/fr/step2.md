# Tests unitaires

Le but des tests unitaires est de tester chaque unité de code isolément du reste du code pour localiser rapidement les parties du code qui fonctionnent ou ne fonctionnent pas comme prévu. Vous placerez les tests unitaires dans le répertoire `src` dans chaque fichier contenant le code qu'ils testent. La convention est de créer un module nommé `tests` dans chaque fichier pour contenir les fonctions de test et d'ajouter l'annotation `cfg(test)` au module.
