# Fonction pour mapper les caractères dans une chaîne de caractères

Pour utiliser cette fonction pour mapper les caractères dans une chaîne de caractères, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `String.prototype.split()` et `Array.prototype.map()` pour appeler la fonction fournie, `fn`, pour chaque caractère dans la chaîne de caractères donnée.
- Utilisez `Array.prototype.join()` pour recombiner le tableau de caractères en une nouvelle chaîne de caractères.
- La fonction de rappel, `fn`, prend trois arguments : le caractère actuel, l'index du caractère actuel et la chaîne `mapString` sur laquelle la fonction a été appelée.

Voici le code de la fonction :

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Exemple d'utilisation :

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
