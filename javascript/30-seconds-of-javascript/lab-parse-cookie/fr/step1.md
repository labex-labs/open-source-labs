# Fonction JavaScript pour analyser les cookies HTTP

Pour analyser une chaîne d'en-tête de cookie HTTP en JavaScript et retourner un objet de toutes les paires nom-valeur de cookies, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `String.prototype.split()` pour séparer les paires clé-valeur les unes des autres.
- Utilisez `Array.prototype.map()` et `String.prototype.split()` pour séparer les clés des valeurs dans chaque paire.
- Utilisez `Array.prototype.reduce()` et `decodeURIComponent()` pour créer un objet avec toutes les paires clé-valeur.

Voici un exemple de la fonction `parseCookie()` qui met en œuvre les étapes ci-dessus :

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

Vous pouvez tester la fonction comme suit :

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
