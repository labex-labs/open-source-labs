# Développement guidé par les tests

Maintenant que nous avons extrait la logique dans `src/lib.rs` et laissé la collecte d'arguments et la gestion d'erreurs dans `src/main.rs`, il est beaucoup plus facile d'écrire des tests pour la fonctionnalité principale de notre code. Nous pouvons appeler directement des fonctions avec divers arguments et vérifier les valeurs de retour sans avoir à appeler notre binaire à partir de la ligne de commande.

Dans cette section, nous allons ajouter la logique de recherche au programme `minigrep` en utilisant le processus de développement guidé par les tests (TDD) avec les étapes suivantes :

1. Écrire un test qui échoue et le lancer pour vous assurer qu'il échoue pour la raison que vous attendez.
2. Écrire ou modifier juste assez de code pour que le nouveau test passe.
3. Refactoriser le code que vous venez d'ajouter ou de modifier et vous assurer que les tests continuent à passer.
4. Répéter à partir de l'étape 1!

Bien que ce soit une des nombreuses façons d'écrire du logiciel, le TDD peut aider à diriger la conception du code. Écrire le test avant d'écrire le code qui fait passer le test aide à maintenir une couverture de test élevée tout au long du processus.

Nous allons tester et développer l'implémentation de la fonctionnalité qui va réellement rechercher la chaîne de requête dans le contenu du fichier et produire une liste de lignes qui correspondent à la requête. Nous allons ajouter cette fonctionnalité dans une fonction appelée `search`.
