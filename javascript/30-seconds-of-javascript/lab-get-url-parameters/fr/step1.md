# Objet avec les paramètres d'URL

Pour créer un objet qui contient les paramètres de l'URL actuelle, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.match()` avec une expression régulière appropriée pour extraire toutes les paires clé-valeur.
3. Utilisez `Array.prototype.reduce()` pour mapper et combiner les paires en un seul objet.
4. Passez `location.search` en argument pour l'appliquer à l'URL actuelle.

Voici le code :

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)),
      a
    ),
    {}
  );
```

Vous pouvez utiliser cette fonction avec n'importe quelle URL pour obtenir un objet avec ses paramètres. Voici quelques exemples :

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
