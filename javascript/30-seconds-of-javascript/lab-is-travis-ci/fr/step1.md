# Vérification si l'environnement est Travis CI

Pour vérifier si vous exécutez sur Travis CI, utilisez la fonction `isTravisCI()`. Cette fonction vérifie si les variables d'environnement `TRAVIS` et `CI` sont présentes.

```js
const isTravisCI = () => "TRAVIS" in process.env && "CI" in process.env;
```

Pour commencer à coder sur Travis CI, ouvrez le Terminal/SSH et tapez `node`.
