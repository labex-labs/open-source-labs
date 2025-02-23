# Comment obtenir le premier élément d'un tableau en JavaScript

Pour obtenir le premier élément d'un tableau en JavaScript, vous pouvez utiliser la fonction `head`. Voici comment vous pouvez l'utiliser :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour commencer à pratiquer la programmation.
3. Utilisez le code suivant pour obtenir le premier élément d'un tableau :

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. Appelez la fonction `head` avec un tableau en tant qu'argument pour obtenir le premier élément. Si le tableau est vide ou faux, la fonction renverra `undefined`.

Voici quelques exemples :

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
