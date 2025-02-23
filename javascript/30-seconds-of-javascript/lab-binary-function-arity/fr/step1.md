# Fonction qui accepte jusqu'à deux arguments

Pour commencer à coder, ouvrez le Terminal/SSH et entrez `node`.

La fonction `binary` est créée avec la capacité d'accepter jusqu'à deux arguments tout en ignorant les autres.

La fonction `fn` fournie est appelée avec les deux premiers arguments donnés.

Voici le code :

```js
const binary = (fn) => (a, b) => fn(a, b);
```

Et voici un exemple d'utilisation :

```js
["2", "1", "0"].map(binary(Math.max)); // [2, 1, 2]
```
