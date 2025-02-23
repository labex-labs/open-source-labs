# Conversion d'une chaîne de requête en objet

Pour convertir une chaîne de requête ou une URL en objet, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `String.prototype.split()` pour extraire les paramètres de l'`url` donnée.
3. Utilisez le constructeur `URLSearchParams` pour créer un objet et le convertir en un tableau de paires clé-valeur à l'aide de l'opérateur de propagation (`...`).
4. Utilisez `Array.prototype.reduce()` pour convertir le tableau de paires clé-valeur en un objet.

Voici le code pour convertir la chaîne de requête :

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

Utilisation de l'exemple :

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
