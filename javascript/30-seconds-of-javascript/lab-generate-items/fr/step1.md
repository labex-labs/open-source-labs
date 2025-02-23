# Code Practice

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Ensuite, vous pouvez utiliser la fonction `generateItems` pour générer un tableau avec un nombre spécifique d'éléments.

- Appelez `generateItems` avec le nombre d'éléments souhaité et une fonction qui sera utilisée pour générer les éléments.
- `generateItems` utilise `Array.from()` pour créer un tableau vide de la longueur spécifiée, et appelle la fonction fournie avec l'index de chaque nouvel élément créé.
- La fonction fournie prend un argument - l'index de chaque élément.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

Voici un exemple d'utilisation de `generateItems` pour générer un tableau de 10 nombres aléatoires :

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
