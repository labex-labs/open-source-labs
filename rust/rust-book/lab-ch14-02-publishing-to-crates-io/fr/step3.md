# Sections couramment utilisées

Nous avons utilisé le titre Markdown `# Exemples` dans la liste 14-1 pour créer une section dans le HTML avec le titre "Exemples". Voici quelques autres sections que les auteurs de boîtes à outils (crates) utilisent couramment dans leur documentation :

- **Panics** : Les scénarios dans lesquels la fonction documentée pourrait générer une panique. Les appelants de la fonction qui ne veulent pas que leur programme plante doivent s'assurer de ne pas appeler la fonction dans ces situations.
- **Erreurs** : Si la fonction renvoie un `Result`, décrire les types d'erreurs qui pourraient survenir et quelles conditions pourraient entraîner la renvoi de ces erreurs peut être utile pour les appelants afin qu'ils puissent écrire du code pour gérer les différents types d'erreurs de différentes manières.
- **Sécurité** : Si la fonction est `unsafe` à appeler (nous discutons de l'insécurité au chapitre 19), il devrait y avoir une section expliquant pourquoi la fonction est insécurisée et couvrant les invariants que la fonction attend des appelants pour les maintenir.

La plupart des commentaires de documentation n'ont pas besoin de toutes ces sections, mais c'est une bonne liste de contrôle pour vous rappeler les aspects de votre code qui intéresseront les utilisateurs.
