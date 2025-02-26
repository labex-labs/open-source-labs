# Pourquoi utiliser les générateurs

- De nombreux problèmes sont bien plus clairs lorsqu'ils sont exprimés en termes d'itération.
  - Parcourir une collection d'éléments et effectuer une opération de quelque type (recherche, remplacement, modification, etc.).
  - Les pipelines de traitement peuvent être appliqués à une large gamme de problèmes de traitement de données.
- Meilleure efficacité mémoire.
  - Ne produisent des valeurs que lorsqu'elles sont nécessaires.
  - En contraste avec la construction de gigantesques listes.
  - Peuvent fonctionner sur des données en flux
- Les générateurs encouragent la réutilisation de code
  - Sépare l'_itération_ du code qui utilise l'itération
  - Vous pouvez construire une boîte à outils de fonctions d'itération intéressantes et les _combiner_.
