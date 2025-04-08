# Exécuter un seul test

Nous pouvons passer le nom de n'importe quelle fonction de test à `cargo test` pour exécuter seulement ce test :

```bash

```

Seul le test avec le nom `one_hundred` a été exécuté ; les deux autres tests ne correspondent pas à ce nom. La sortie du test nous informe qu'il y avait plus de tests qui n'ont pas été exécutés en affichant `2 filtrés` à la fin.

Nous ne pouvons pas spécifier les noms de plusieurs tests de cette manière ; seule la première valeur donnée à `cargo test` sera utilisée. Mais il existe un moyen d'exécuter plusieurs tests.
