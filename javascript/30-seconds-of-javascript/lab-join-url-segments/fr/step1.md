# Joindre et normaliser les segments d'URL

Pour joindre les segments d'URL donnés et normaliser l'URL résultante, suivez les étapes suivantes :

1. Utilisez `Array.prototype.join()` pour combiner les segments d'URL.
2. Utilisez une série d'appels à `String.prototype.replace()` avec diverses expressions régulières pour normaliser l'URL résultante en :
   - Enlevant les doubles barres obliques
   - Ajoutant les barres obliques appropriées pour le protocole
   - Enlevant les barres obliques avant les paramètres
   - Combinant les paramètres avec `'&'` et normalisant le premier délimiteur de paramètres.

Utilisez le extrait de code ci-dessous pour joindre et normaliser les segments d'URL :

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

Utilisation de l'exemple :

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
