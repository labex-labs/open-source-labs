# Comment récupérer une valeur imbriquée dans un objet à l'aide d'un tableau de clés

Pour récupérer une valeur spécifique à partir d'un objet JSON imbriqué, vous pouvez utiliser la fonction `deepGet`. Cette fonction prend en entrée un objet et un tableau de clés, et renvoie la valeur cible si elle existe dans l'objet.

Pour utiliser la fonction `deepGet` :

- Créez un tableau des clés que vous souhaitez récupérer à partir de l'objet JSON imbriqué.
- Appelez la fonction `deepGet` avec l'objet et le tableau de clés.
- La fonction renverra la valeur cible si elle existe, ou `null` si elle n'existe pas.

Voici le code de la fonction `deepGet` :

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

Et voici un exemple de manière d'utiliser la fonction `deepGet` :

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // renvoie 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // renvoie null
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
