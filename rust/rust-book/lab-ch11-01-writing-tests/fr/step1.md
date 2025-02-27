# Comment écrire des tests

Les tests sont des fonctions Rust qui vérifient que le code non de test fonctionne comme prévu. Les corps des fonctions de test effectuent généralement ces trois actions :

- Préparer toute les données ou l'état nécessaires.
- Exécuter le code que vous voulez tester.
- Vérifier que les résultats sont ceux que vous attendez.

Examnons les fonctionnalités que Rust offre spécifiquement pour écrire des tests qui effectuent ces actions, qui incluent l'attribut `test`, quelques macros et l'attribut `should_panic`.
